---
id: github_insights_tool
section: project
title: GitHub Repository Insights Tool
last_reviewed: 2026-05-25
status: shipped
date_start: 2025-12
date_end: 2025-12
stack:
  - Python
  - Flask
  - OpenAI API
  - GitHub REST API
  - HTML
  - CSS
  - JavaScript
skills:
  - Agentic LLM workflow design
  - Prompt engineering
  - REST API integration
  - Flask backend development
  - Frontend development
tags:
  - project
  - ai
  - llm
links:
  repo: https://github.com/OctavioH03/github-repo-insights
summary: Built a full-stack agentic tool that uses a two-stage LLM pipeline to let users analyze any GitHub repository or find one using natural language — receiving AI-generated insight cards covering what it does, its tech stack, risks, and quick start steps.
---

# GitHub Repository Insights Tool

## Elevator pitch

A full-stack tool that makes any GitHub repository immediately understandable. Users can either paste a repo URL or describe what they're looking for in plain English. The backend fetches repository metadata, languages, topics, and a README snippet from the GitHub REST API, then passes that data to OpenAI to generate structured Insight Cards covering what the repo does, its tech stack, risks and limitations, and quick start steps. Built solo for CSC 180 Intelligent Systems at CSUS (Fall 2025). Received an A.

## Problem

Finding and evaluating GitHub repositories is tedious. Searching on GitHub returns results ranked by stars, not by relevance to what you actually need, and understanding whether a repo is worth using requires reading through READMEs, issues, and code manually. The goal was to build a tool that compresses that process — letting users describe what they need in natural language and getting a structured, AI-generated summary back in seconds.

## What Octavio built

Octavio designed and built the entire project solo. The course objective was to build a server that communicates with an LLM to create an agentic workflow — every architectural and design decision was Octavio's own.

### Two-stage agentic pipeline
The core of the project is a two-stage LLM pipeline orchestrated by a Flask backend. In the first stage, when a user submits a natural language query, an initial LLM call converts the description into concise GitHub search keywords. Those keywords are passed to the GitHub Search API to retrieve the most relevant repository. In the second stage, the backend fetches full repository details — metadata, languages, topics, and a truncated README — and sends everything to a second LLM call to generate structured Insight Cards. The two calls serve distinct purposes: one reasons about the query, one generates structured output from data.

For direct URL analysis, the first stage is skipped and the pipeline starts at data retrieval.

### Prompt engineering
Octavio iterated on both prompts to improve output quality. The keyword extraction prompt was tuned to return concise, GitHub-compatible search strings rather than verbose descriptions. The insight generation prompt was structured around fixed section headings to ensure the output could be parsed and rendered as individual cards in the frontend. Formatting and section descriptions were refined across iterations to produce clean, consistent output.

### Flask backend
Built a Flask API with a single `POST /api/insights` endpoint that handles both query modes, orchestrates the GitHub and OpenAI API calls, decodes base64-encoded README content, and returns a structured JSON response. Includes error handling for invalid URLs, missing repos, GitHub rate limits, and OpenAI failures. CORS enabled for frontend compatibility.

### Frontend
Built a static HTML/CSS/JS frontend with two input modes switchable via radio buttons. Insight Cards are rendered by splitting the markdown response on section headings and building individual card elements dynamically. Repository metadata, languages, and topics are displayed as labeled fields and pill tags. Frontend is deployed to GitHub Pages; backend runs locally or can be hosted separately.

## Technical approach

The natural language search mode works as follows: the user's description is sent to the backend, which makes a low-temperature LLM call to extract search keywords, queries the GitHub Search API ranked by stars, takes the top result, fetches its full details across three additional API calls (repo metadata, languages, topics, README), then sends the combined data to a second LLM call for insight generation. The README is truncated to approximately 4KB before being included in the prompt to keep token usage predictable.

The URL mode skips the keyword extraction step and goes directly to data retrieval and insight generation.

## Results

- Received an A in CSC 180 Intelligent Systems (combined undergrad course, Fall 2025).
- Tool works end-to-end for both URL analysis and natural language search.
- Personally useful for discovering repositories — the natural language search mode surfaces relevant results faster than manually browsing GitHub.

## Planned improvements

- Deploy backend to Railway or Render so the tool is fully accessible without a local server
- Return multiple ranked results instead of a single top match, with LLM ranking by relevance to the original query rather than stars alone
- Add a "Why this matches your query" explanation to each result
- Stream insight generation so cards appear progressively
- Add filter controls (language, minimum stars, recently updated) using GitHub search API parameters
- Simple caching for recently analyzed repositories to reduce API calls and latency
