---
id: faq
section: faq
title: Frequently Asked Questions
last_reviewed: 2026-05-25
tags:
  - faq
summary: Short factual answers to common recruiter questions about Octavio's background, preferences, and goals.
---

# Frequently Asked Questions

## Why are you looking for a new role?

Octavio graduated from CSU Sacramento in December 2025 and is actively pursuing full-time software engineering roles. He is looking for a team where he can grow alongside experienced engineers in a culture that encourages learning. He enjoys backend and full-stack work and is drawn to teams where there is room to take on new challenges and work with emerging technologies.

## What size company do you prefer?

Octavio does not have a strong preference on company size. Smaller companies tend to offer more ownership and breadth, while larger companies offer the ability to specialize and learn from a deeper talent pool. What matters more to him is the engineering culture and the quality of work he can contribute to.

## Remote, hybrid, or on-site?

Octavio prefers hybrid or on-site arrangements. As a new grad, he finds he learns best working directly with teammates in person and values the mentorship and collaboration that comes with it. He is open to remote opportunities as well. Order of preference: hybrid, on-site, remote.

## What is your strongest technical area?

Octavio's strongest area is backend systems and data pipelines in Python. His most substantial work — a multithreaded log processing pipeline at Johnson & Johnson and a full C#/.NET REST API layer on AiRise — both involved owning backend components end-to-end under real constraints. He also has practical experience integrating external APIs and third-party services into production-facing features, which is a growing area of focus.

## Describe a difficult technical problem you solved

Multiple examples below, each with a category tag and a pointer to the full story.

### J&J pipeline — threading bottleneck
`Technical` `Performance` `Problem Solving` (see `jj_internship.md`)

The single-threaded pipeline was timing out on large log files, blocking smaller files from completing. Octavio fixed this by parallelizing the parsing, embedding, and clustering stages across files using multithreading. The full daily run completed in approximately one hour consistently after the fix.

### AiRise — Google Sign-In rescue
`Technical` `Leadership` `Teamwork` (see `airise.md`)

A teammate was unable to finish OAuth across two sprints and only surfaced the blocker the weekend the sprint was closing. Octavio stepped in, built the iOS-side implementation using the Kotlin expect/actual pattern, fixed the key management setup, and resolved the OAuth API integration. Both platforms were working by end of sprint. He followed up privately with the teammate to address the root cause of the repeated blocking.

### OS kernel — scheduler timing bug
`Technical` `Systems` `Debugging` (see `os_project.md`)

Two variables tracking process CPU time had incorrect reset behavior — the lifetime counter was resetting when it should have been accumulating, and the per-slice counter was not resetting after expiry. Combined effect: all processes lost the CPU after their first timeslice and never recovered, leaving the idle process running indefinitely. Caught and fixed before submission.

### AiRise — Gemini token efficiency
`Technical` `Optimization` `API Integration` (see `airise.md`)

During development, the regeneration-on-every-visit behavior quickly exhausted free-tier token limits, signaling it would be costly at scale. Octavio scoped generation to once on app launch and once per hour if the app remained open, reducing API usage without degrading the user experience.

## What do you want to learn next?

Octavio wants to deepen his experience with cloud infrastructure and services, build and work on scalable backend systems and microservices, and continue developing his understanding of how emerging technologies — including current tools like LLMs — can be applied effectively in production environments.

## Are you open to relocation?

Yes. Octavio is based in Sacramento, CA and is open to relocation, with a preference for staying within California. He is open to opportunities elsewhere in the US as well.

## What is your work authorization status?

Octavio is a US citizen and is authorized to work in the United States without sponsorship. He does not hold a security clearance.

## What is your target role?

Octavio is targeting new grad or junior Software Engineer roles with a backend or full-stack focus, particularly on teams working on data-intensive systems or products that incorporate emerging technologies. He is interested in owning features end-to-end and growing within his team over time.

## What industries are you interested in?

Octavio is open to software engineering roles across the tech industry. He has particular interest in fintech, data/analytics platforms, and developer tools given the overlap with his backend and data pipeline experience, but is genuinely open to other domains — the quality of the engineering culture and the type of work matter more than the industry. He is especially drawn to teams building products where backend systems and emerging technologies are core to what the product does.

## When are you available to start?

Octavio is available to start immediately.

## What are you currently working on?

Octavio is building a RAG-powered chatbot embedded in his portfolio website that allows recruiters to ask questions about his background and experience directly. He is also continuing to study data structures and algorithms, actively applying to full-time roles, and conducting mock interviews to prepare.
