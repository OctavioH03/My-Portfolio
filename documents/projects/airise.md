---
section: project
title: AiRise
last_reviewed: 2026-05-01
status: shipped
date_start: 2025-01
date_end: 2025-12
stack:
  - Kotlin Multiplatform
  - C#
  - .NET 9
  - Azure
  - MongoDB
  - Supabase
  - Firebase
  - Gemini
skills:
  - Kotlin
  - C#
  - RESTful APIs
  - Layered backend architecture
  - Frontend ViewModels
  - Ktor (Kotlin HTTP Client)
  - Gemini
  - MongoDB
  - aggregation pipelines
  - Firebase Authentication
  - Supabase BLOB storage
tags:
  - project
  - AI
  - Backend
  - Full-stack
links:
  repo: https://github.com/OctavioH03/AiRise
summary: Cross-platform AI fitness app where I owned the C#/.NET API layer, Gemini-powered personalization, and KMP health-data integration on an 8-person Agile team.
source_path: projects/airise.md
---

# AiRise

## Elevator pitch

AiRise is a cross-platform AI-powered fitness and wellness app built with Kotlin Multiplatform, published to the App Store for real users. It delivers personalized workout programming, nutrition guidance, and health tracking by integrating with Apple Health and Google Health Connect. An AI Coach powered by Google Gemini enables natural language coaching, goal setting, and adaptive recommendations that adjust based on user activity trends. Gamified challenges, streaks, leaderboards, and social features drive accountability across a community of users.

## Problem

Personal trainers and coaching programs are expensive and inaccessible for most people who are just starting their fitness journey. Beginners who want to work out often don't know where to start, and generic fitness apps offer static plans that don't adapt to individual progress or preferences. Our client wanted to enter the fitness app market by offering AI-powered coaching as an affordable alternative — giving users personalized guidance, adaptive recommendations, and accountability features at a fraction of the cost of a human trainer.

## What Octavio built

- Implemented the admin authorization system using a custom ASP.NET Core authorization handler with a fresh-token plus boolean admin-field approach, balancing security with a low-friction experience for the client. Validated the approach with the client before building.
- Built fitness challenge management endpoints, enabling clients to create, modify, and delete challenges through protected admin routes.
- Built the welcome, signup, and login screens using Compose Multiplatform in the shared commonMain module across Android and iOS, implementing screen state and navigation logic via Kotlin ViewModels and API communication via Ktor HTTP client.
- Set up BuildKonfig for the entire project to allow secure storage and retrieval of API keys via the local.properties file, making key management consistent and safe across the team.
- Stepped in to complete Google Sign-In after a teammate was unable to finish. The Android side had solid groundwork; Octavio built the iOS-side implementation using the Kotlin expect/actual pattern and fixed the key integration and OAuth API communication that was blocking both platforms.
- Integrated Gemini into the frontend through a KMP-compatible wrapper around Google's generative AI SDK. Fed live database context to the LLM to generate fresh fitness summaries through the AiRise Coach. Resolved a token efficiency issue where summaries were regenerating on every screen visit — fixed by running once on launch and refreshing on a one-hour interval.
- Wrote unit and integration tests for every backend feature Octavio personally built, including user health data collection, workout program personalization, and social features, plus partial coverage where contributions overlapped with teammates. Tested the service layer and controller independently using xUnit, then ran integration tests against an in-memory MongoDB instance using Mongo2Go to validate real query behavior without requiring a live connection.
- Led Jira ticket creation and distribution across the team, creating and assigning over 100 tickets throughout the project.

## What Octavio did not build

- Octavio did not own the Azure deployment — that was managed by a teammate.
- Octavio did not do frontend testing.
- Apple Sign-In was implemented by the co-lead after App Store review required it.

## My role

Co-lead on an 8-person Agile team. Responsible for creating and distributing Jira tickets, unblocking teammates, and filling integration gaps between features. Primarily focused on delivering and owning end-to-end RESTful endpoints with full test coverage, while also integrating those endpoints into the frontend via ViewModels, repositories, and the Ktor HTTP client. Also owned the Gemini AI integration — selecting a KMP-compatible SDK wrapper, feeding live database context to the model, and optimizing token usage for production efficiency.


## Technical approach

Kotlin Multiplatform was chosen over React Native or separate native codebases to allow the team to work primarily in one language while still making platform-specific adjustments for Android and iOS where needed.

C#/.NET 9 was used for the API layer. It allowed smooth hosting on Azure and was familiar to several team members, avoiding the overhead of learning a new backend language mid-project.

MongoDB fit naturally because most of the app's data — workouts, health logs, user profiles, challenges — is document-shaped with no complex joins required. The team considered a relational database specifically for the social features but determined the added complexity wasn't warranted given how well the rest of the app fit the NoSQL model. MongoDB's schema flexibility also allowed the team to evolve data structures as features were added mid-sprint without costly migrations. The tradeoff of eventual consistency in some reads was acceptable for a fitness context where millisecond accuracy on leaderboards or streaks isn't critical.

BuildKonfig was used to manage API keys securely across the project via the local.properties file, keeping credentials out of source control and giving the whole team a consistent retrieval pattern.

Mongo2Go was used for integration testing, spinning up an in-memory MongoDB instance to validate real query behavior without a live database connection. This made tests faster and self-contained compared to mocking the full data layer.

## Results

- Octavio achieved full unit and integration test coverage of every backend feature he personally built.
- Octavio created and distributed over 100 Jira tickets across the team.
- App published to the Apple App Store and available to real users.


## Challenges

### Google Sign-In and teammate support
A teammate was assigned OAuth (Google and Apple Sign-In) but was unable to finish across two sprints, and did not surface his blockers until the weekend the second sprint was closing. Octavio stepped in that weekend to complete the feature. The Android groundwork was mostly in place — Octavio built the iOS-side implementation using the expect/actual pattern, fixed the OAuth API integration, and resolved the key management issues using BuildKonfig. The root cause of the teammate's struggle turned out to be over-reliance on LLMs to generate code without understanding it, which created a cycle of copy-pasting without being able to debug effectively. Octavio addressed this in a private conversation, encouraging him to engage with the code directly and surface blockers earlier. After that sprint, the teammate finished his assigned tickets consistently for the rest of the project. Apple Sign-In was later completed by the co-lead when App Store review required it.

### App Store submission cycle
Getting the app published to the Apple App Store required three submission rounds. Apple's review process only flags the first issue found per review, so each round meant making a fix, resubmitting, and waiting — compressing the timeline significantly. The rejections included missing Google or email sign-in options, no account deletion feature, and a missing privacy manifest. The challenge was managing these iterative review cycles against real deadlines.

### Admin authorization design
Before building the admin authorization system, Octavio spent time reasoning through different approaches to find the right balance between security and usability. The concern was building something secure enough to protect admin routes without making the client's experience tedious. After evaluating options and confirming the approach with the client, Octavio settled on a fresh-token plus boolean admin-field pattern that satisfied both constraints.

### Gemini token efficiency
The initial Gemini integration refreshed the AI Coach summary every time a user returned to the home screen, which would have resulted in unnecessary token consumption at scale. Octavio fixed this by scoping the summary generation to once on app launch and once per hour if the app remained open — reducing token usage without degrading the user experience.
