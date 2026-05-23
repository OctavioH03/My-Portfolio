---
id: airise
section: project
title: AiRise
last_reviewed: 2026-05-01
status: shipped  # shipped | in-progress | archived | learning
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
links:
  repo: https://github.com/OctavioH03/AiRise
summary: Cross-platform AI fitness app where I owned the C#/.NET API layer, Gemini-powered personalization, and KMP health-data integration on an 8-person Agile team.
---

# AiRise

## Elevator pitch

AiRise is a cross-platform AI-powered fitness and wellness app built with Kotlin Multiplatform, published to the App Store for real users. It delivers personalized workout programming, nutrition guidance, and health tracking by integrating with Apple Health and Google Health Connect. An AI Coach powered by Google Gemini enables natural language coaching, goal setting, and adaptive recommendations that adjust based on user activity trends. Gamified challenges, streaks, leaderboards, and social features drive accountability across a community of users.

## Problem

Personal trainers and coaching programs are expensive and inaccessible for most people who are just starting their fitness journey. Beginners who want to work out often don't know where to start, and generic fitness apps offer static plans that don't adapt to individual progress or preferences. Our client wanted to enter the fitness app market by offering AI-powered coaching as an affordable alternative — giving users personalized guidance, adaptive recommendations, and accountability features at a fraction of the cost of a human trainer.

## What Octavio built

- Octavio implemented the admin authorization system and fitness challenge management feature, enabling clients to create, modify, and delete challenges through protected admin routes secured by the custom ASP.NET Core authorization handler.
- Octavio built the welcome, signup, and login screens using Compose Multiplatform in the shared commonMain module, implementing screen state and navigation logic via Kotlin ViewModels and API communication via Ktor HTTP client.
- Octavio wrote unit and integration tests for the backend entities he personally built on AiRise, including user health data collection, workout program personalization, and social features. He also wrote partial test coverage for user data and challenges where his contributions overlapped with teammates. For each entity he tested the service layer and controller independently using xUnit to validate business logic in isolation, then used Mongo2Go to run integration tests against an in-memory MongoDB instance, validating real database query behavior without requiring a live connection.

## What Octavio did not build

- Octavio did not own the Azure deployment — that was managed by a teammate.
- Octavio did not do frontend testing.
- Apple Sign-In was implemented by the co-lead after App Store review required it.

## My role

I helped co-lead the team through creating and assigning Jira tickets, filling any gaps in integration between features, and helping others get unblocked.

Octavio was a full-stack developer focused mainly on delivering and owning end-to-end RESTful endpoints including testing in the backend, while also integrating them into the frontend ViewModels using repositories and the Ktor HTTP client to communicate with our Azure server.

Octavio integrated Gemini with the frontend through the use of a library that converts Google's generative AI SDK functions to usable versions within Kotlin Multiplatform. Octavio used data from the database to give relevant context to the LLM providing fresh and insightful fitness summaries from the AiRise Coach throughout the day.


## Technical approach

Kotlin Multiplatform was used over other languages like React Native or Kotlin + Swift because it allowed us to focus mostly on one language while having the ability to make domain specific changes when needed for both Andriod and iOS.

C#/.NET 9 allowed us to smoothly host our API endpoints on Azure giving responsive access to both iOS and Android mobile apps while also being familiar to some of our team members avoiding having to learn completely new languages and frameworks for both the backend and frontend.

The team decided to use MongoDB because our usecase did not involve complex relationships between collections allowing NoSQL to be beneficial with less drawbacks. Additionally,...

## Results

- Over 70% test coverage of the backend and frontend as a team.
- Octavio's completed full coverage test of backend features including unit and integration tests.
- Octavio created and distributed over 100 Jira tickets to the team


## Challenges (optional)

Hard problems and how you solved them — good for interview-style questions.
