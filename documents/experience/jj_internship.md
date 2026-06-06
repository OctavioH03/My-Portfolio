---
section: experience
title: Software Engineer Intern
last_reviewed: 2026-05-01
organization: Johnson & Johnson
location: Raritan, New Jersey
employment_type: Internship
date_start: 2025-05
date_end: 2025-08 
stack:
  - Python
  - Oracle SQL
  - Windows Scheduling
skills:
  - Python
  - scikit-learn
  - K-Means Clustering
  - Text Embedding
  - Multithreading
  - Oracle SQL
  - openpyxl
  - Excel automation
  - pygrok
tags:
  - experience
summary: Built an end-to-end Python automation pipeline for J&J's ERP Application Maintenance and Automation team that parsed, embedded, and clustered 400+ OMP log files daily — reducing log noise by 99% and increasing throughput 4x via multithreading.
source_path: experience/jj_internship.md
---

# J&J Software Engineer Intern

**Dates:** May 2025 – Aug 2025   
**Location:** Raritan, New Jersey

## Role summary

Octavio interned on the ERP Application Maintenance and Automation team at Johnson & Johnson. The team maintains and automates tooling around J&J's enterprise resource planning systems. His project focused on OMP — a planning and forecasting system used to manage manufacturing demands, supply needs, and production scheduling across J&J's product lines. When OMP jobs fail, they produce log files that engineers and analysts have to manually review to diagnose the issue. The volume and noise in these logs made that process slow and tedious. A couple weeks into his internship, Octavio was assigned to build a solution to automate and streamline that review process. He owned the project end-to-end, holding weekly stand-ups with his mentor to review design decisions and surface any blockers.

## What Octavio Did
- Interviewed two to three analysts performing manual log reviews to understand the process and gather domain knowledge that informed clustering decisions throughout the project
- Designed and built a fully automated pipeline to parse, embed, cluster, and report on OMP log files
- Authored custom Grok patterns using pygrok primitives to handle the structural variance across different job types and product branches
- Deployed and scheduled the pipeline on a remote server for daily automated execution
- Reduced the manual review burden when OMP job failures occur

## Technical approach

The pipeline retrieves OMP log files for a given day, parses their content, generates text embeddings, applies K-Means clustering to group semantically similar log messages, and outputs a structured Excel report with separate sheets per job using openpyxl. The report is saved to a shared NAS folder accessible to the team.

One constraint was the high variance in log file structure across different job types. Octavio handled this by scoping the pipeline to four branches of J&J products and authoring custom Grok patterns using pygrok primitives to match each format. Rather than relying on built-in patterns alone, he analyzed the actual log structures and wrote patterns tailored to J&J's specific job output formats. This gave the parser reliable, predictable extraction across daily, weekly, and monthly job variants without requiring a fully generalized solution. To scale beyond this scope, an LLM-based parsing layer could handle arbitrary log formats, though that would introduce additional latency and a new point of failure — a tradeoff worth evaluating if coverage is extended.

A significant performance issue emerged early: the single-threaded pipeline would block on extremely large log files, causing the entire run to time out before completing. Octavio resolved this by introducing multithreading across the parsing, embedding, and clustering stages. After the fix, all jobs for a given day completed in approximately one hour consistently.
The pipeline was scheduled via Windows Task Scheduler on a remote server, accessed through Remote Desktop.

## Impact (use metrics where you can)

- Reduced log noise by 99% — measured by comparing the average daily log volume (files × lines per file) against the average number of clusters per job in the output report
- Increased pipeline throughput 4x by implementing multithreading, eliminating timeout failures caused by large file blocking
- Covered 4 branches of J&J products across daily, weekly, and monthly job variants, processing 400+ log files per day consisting of thousands of lines each
- Pipeline delivered to the team before internship end; mentor acknowledged the result and the team plans to extend coverage to additional job types

## Challenges

### Log structure variance
OMP log files don't follow a single consistent format — structure varies across job types, product branches, and run frequencies (daily vs. weekly vs. monthly). Rather than attempting a fully generalized parser upfront, Octavio scoped the pipeline to a defined set of jobs and handled variance through targeted parsing logic per format. This was a deliberate tradeoff: get something accurate and reliable in production rather than a fragile general solution. The architecture leaves room to extend — an LLM parsing layer is the natural next step for broader coverage.

### Single-threaded timeout failures
Before multithreading, the pipeline ran sequentially and would get stuck on extremely large log files, blocking smaller files from completing and eventually hitting the scheduler's time limit. Octavio parallelized the parsing, embedding, and clustering stages across files using multithreading. After the change the full daily run completed reliably in roughly one hour.

### Domain knowledge gap
OMP log files carry domain-specific terminology and patterns that aren't obvious from the file content alone. To improve clustering quality, Octavio worked directly with the analysts doing manual reviews, using their feedback to refine how he was parsing and grouping messages. Getting useful signal out of subject matter experts who aren't engineers — and translating that into technical decisions — was a skill he developed through this project.
