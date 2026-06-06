---
section: project
title: SPEDE Operating System
last_reviewed: 2026-05-25
status: shipped
date_start: 2025-08
date_end: 2025-12
stack:
  - C
  - x86 Assembly
  - QEMU
  - SPEDE
  - GDB
  - Make
  - Git
skills:
  - Systems programming in C
  - x86 interrupt handling
  - Memory-mapped I/O
  - Hardware driver development
  - Interrupt descriptor table (IDT)
  - PIC programming
  - Process scheduling
  - Context switching
  - System call infrastructure
  - Kernel concurrency primitives
  - Bit manipulation
  - GDB debugging
  - Inline assembly
tags:
  - project
  - systems
  - os
links:
  repo: https://github.com/OctavioH03/spede-os
summary: Built a functional x86 OS kernel from scratch in C and assembly as team lead on a 3-person team in a combined undergrad/grad OS course at CSUS, implementing hardware drivers, interrupt handling, process scheduling, system calls, and mutex-based concurrency.
source_path: projects/os.md
---

# SPEDE Operating System

## Elevator pitch

A functional x86 operating system kernel built from scratch in C and x86 assembly as part of Operating System Pragmatics, a combined undergraduate and graduate course at CSUS. The OS runs on QEMU via the SPEDE virtual development environment and implements everything from hardware drivers and interrupt handling up through process scheduling, system calls, and kernel concurrency primitives. Built as team lead on a 3-person team over Fall 2025.

## Problem

This project exists because reading about operating systems and building one are completely different things. The SPEDE environment strips away every abstraction — no standard library, no existing kernel, no safety net — and requires the programmer to interact directly with hardware, manage CPU state by hand, and reason carefully about what happens at every level between powering on a machine and running code. The goal was to understand those layers by implementing them.

## What Octavio built

### VGA display driver
Implemented the full VGA text mode driver in C, writing characters directly to the memory-mapped hardware buffer at `0xB8000`. Each character on screen is a 16-bit value encoding both the ASCII character and a color attribute byte — background and foreground colors packed via bit shifting. The driver tracks cursor position, handles special characters (`\n`, `\r`, `\t`, `\b`), scrolls text when the display fills, and controls the hardware cursor by writing to VGA controller registers via direct port I/O.

### Kernel logging and bit utilities
Implemented a kernel logging system with configurable log levels (error, warn, info, debug, trace) that could be toggled at runtime during development. Implemented `kernel_panic`, which logs the message, forces a GDB breakpoint for live inspection, then exits — useful when hitting unrecoverable states during debugging. Implemented the full suite of bit manipulation utilities used throughout the kernel.

### Interrupt handling infrastructure
Implemented the interrupt handling layer: programming the PIC (Intel 8259) directly via port I/O to enable and dismiss hardware IRQs, registering ISR entry points in the IDT, and building the central dispatch function that routes each interrupt to the correct handler. This is the foundation that keyboard input, the timer, and eventually system calls all run through.

### TTY display latency fix
After interrupt-driven keyboard input was working, the TTY had noticeable lag — on some VMs bad enough to register keystrokes multiple times. Tracked the root cause to the TTY refresh callback running at too slow an interval. Fixed it by tuning the interval constant and removing the compensating workaround code that had accumulated around the issue. Also restored a cursor toggle shortcut that had been dropped, so the display defaults to cursor-off on startup as intended.

### System call infrastructure and handlers
Implemented the mechanism that lets user processes communicate with the kernel: a dedicated software interrupt (`int 0x80`) that transitions from process context into kernel context, an ISR entry point in assembly that saves CPU state into the trapframe, an init function that registers the handler, and the central dispatch loop that decodes the syscall identifier from the `EAX` register and routes to the correct handler. Every system call in the OS flows through this infrastructure.

Implemented end-to-end both the system call API and the kernel-side handler for the following system calls: `proc_get_name`, `sys_get_name`, and `sys_get_time`. Also implemented `io_write` end-to-end to validate TTY output from user processes. The remaining handlers (`proc_exit`, `proc_get_pid`, `io_read`, `io_flush`) were handed off to teammates once the infrastructure and pattern were established.

### Mutex lock and unlock
Implemented `kmutex_lock` and `kmutex_unlock` along with their system call APIs. When a process calls `mutex_lock` and the mutex is already held, it gets moved to a WAITING state, pulled from the scheduler, and queued. When the owner calls `mutex_unlock`, the next waiter is dequeued, assigned ownership, and re-added to the scheduler.

The initial implementation used `lock_count` as the ownership signal and incremented it for every process that touched the mutex — which matched the suggested template approach. During code review, a teammate correctly pointed out that processes entering the wait queue shouldn't increment the count since they don't actually hold the lock. Octavio agreed on the fix — checking `queue_is_empty` instead — and the teammate updated the unlock path accordingly.

## What Octavio did not build

- Keyboard driver
- Timer system and ring buffer data structure
- Process management core (process create/destroy)
- Process scheduler
- Context switch assembly
- TTY driver
- System call handlers for `proc_exit`, `proc_get_pid`, `io_read`, `io_flush` (handed off after infrastructure was complete)
- Mutex destroy and all semaphore functions (init, wait, post, destroy)

## My role

Team lead on a 3-person team. Responsible for PR reviews, submission coordination, and keeping work divided so no one was blocked or duplicating effort. Beyond the specific implementations above, the lead role meant staying close enough to all the code — including parts teammates owned — to catch integration issues and correctness problems before they mattered.

## Technical approach

All hardware interaction is either memory-mapped (VGA) or via direct port I/O — no OS abstractions to lean on. Interrupts are handled by programming the PIC directly and registering ISR entry points in the IDT. Context switching works by saving the full CPU register state into a `trapframe_t` struct on the process's own stack, so the kernel can restore any process exactly where it left off.

The scheduler uses a FIFO run queue with fixed timeslices tracked in timer ticks. When a process exhausts its slice it is re-queued and the next one runs. An idle process runs only when the queue is empty.

System calls use `int 0x80` to enter kernel context. The syscall ID goes in `EAX`, up to three parameters in `EBX`/`ECX`/`EDX`, and the return value is written back to `EAX` in the trapframe before returning to the process — so from the process's perspective it looks like a regular function call.

Mutexes combine a lock count, an owner pointer, and a wait queue. Processes that cannot acquire the lock are moved to WAITING state and removed from the scheduler entirely until the owner releases it.

## Results

- Received an A in a combined undergraduate/graduate course — one of the more rigorous courses in the CSUS CS program.
- All phase submissions delivered and tagged on time across the full semester.
- OS boots, schedules multiple concurrent processes across virtual TTYs, handles hardware interrupts, executes system calls from user processes, and enforces mutex locking — full end-to-end functionality across every implemented layer.
- Ping/pong semaphore test passed, confirming correct concurrent inter-process communication behavior across processes using the semaphore implementation.

## Challenges

### Scheduler timing bug
During final verification before one submission, the OS was exhibiting a symptom where all created processes would lose the CPU after their first timeslice and never get it back — leaving the idle process running indefinitely. Tracking it down revealed two separate bugs in the same area of the scheduler. First, the variable tracking a process's total lifetime CPU usage was being incorrectly reset to zero after each timeslice instead of accumulating. Second, the current-slice counter was not being reset after the slice expired, so every process immediately hit its limit on the next selection and was booted again before doing any useful work. Both variables existed for distinct purposes and required different reset behavior; conflating them produced a failure mode that looked like a single bug but was actually two. Catching it required understanding both variables, their relationship to the scheduler loop, and what the idle process behavior was signaling about the underlying state.

### Tracking down the TTY input lag
The TTY latency bug was tricky because it presented differently across machines — barely noticeable on some, bad enough to duplicate keystrokes on others. That variance made it easy to dismiss as a VM configuration issue rather than a code issue. Pinning it to the refresh rate required measuring the interval against input arrival rate rather than accepting "it's probably the VM" as the answer. The fix was a single constant change once the cause was clear, along with removing the compensating workaround code that had built up around the symptom.

### Mutex design review
The initial mutex lock implementation incremented an ownership counter for every process that touched the mutex, including those entering the wait queue — consistent with the suggested template approach. During code review a teammate flagged that processes waiting for the lock don't actually hold it and shouldn't increment the count. The right fix was to check whether the wait queue was empty in the unlock path instead of relying on the counter. Octavio agreed immediately, the change was small, and the teammate made it. The value of the exchange was catching a logical inconsistency before it shipped — which is what code review is for.