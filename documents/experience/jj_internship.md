---
id: jj_internship 
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
  - Embedding
  - Clustering
  - SQL
tags:
  - experience
summary: One line: scope + impact focus for retrieval.
---

# J&J Software Engineer Intern

**Dates:** May 2025 – Aug 2025   
**Location:** Raritan, New Jersey

## Role summary

2–4 sentences: team, product, your mandate.

I owned this project end-to-end, however I held weekly stand-ups with my mentor to help go over design decisions and any blockers I've encountered. I produced a Python automation pipeline that retrieves OMP log files, parses and embeds their content, clusters messages, and produces a strucutred Excel report. This effectively reduced log noise by 99%.

## Responsibilities

- Reduce the manual review time needed when job failures occur
- Communicate with the people handling manual reviews to get domain knowledge
- Build a fully automated pipeline to help reduce log noise

## Impact (use metrics where you can)

- Increased throughput by 4x by implementing multithreading for parsing and clustering
- Reduced log noise by 99% through K-means clustering

## Tech notes (optional)

One constraint was having to account for the varing structures present within the OMP logs. I handled this by reducing my scope to a more limited set of jobs allowing me to handle the variance in hard coded formats. To scale this an LLM could help parse and embed the logs however this will introduce another point of failure and uncertainty. 

