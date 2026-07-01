# Frontend — Portfolio + Eight

The React frontend for Octavio Hernandez's portfolio site. It serves as both a personal portfolio (projects, experience, about) and the interface for **Eight** — a RAG-powered AI assistant that answers questions about Octavio's background and work directly in the browser.

Deployed to Vercel. Talks to the FastAPI backend on Railway.

---

## Stack

| Tool | Purpose |
|------|---------|
| React 19 + TypeScript | UI framework |
| Vite 8 | Dev server + build |
| Tailwind CSS | Styling |
| Framer Motion | Animations |
| Zustand | Chat state management |

---

## Getting started

```bash
# From the frontend/ directory
npm install
npm run dev
```

Requires the backend to be running locally (or pointing to Railway) for the chat feature. Set the API base URL in `.env`:

```env
VITE_API_URL=http://localhost:8000
```

---

## Project structure

Feature Sliced Design (FSD) — layers flow strictly top to bottom (app → pages → widgets → features → entities → shared). Lower layers must not import from higher ones.

```
src/
├── main.tsx                        Entry point
│
├── app/                            App layer — initialization only
│   ├── App.tsx                     Root component (mounts providers + home page)
│   ├── providers.tsx               Global context providers
│   └── styles/
│       ├── index.css               Global reset + CSS design tokens
│       ├── fonts.css               Font imports
│       └── color_palette.md        Design token reference (gold/navy palette)
│
├── pages/
│   └── home/
│       └── index.tsx               Portfolio page — assembles all section widgets
│
├── widgets/                        Independent, self-contained page sections
│   ├── nav/navbar.tsx              Fixed navigation bar with scroll behavior
│   ├── hero/index.tsx              Name, title, CTA, background animation
│   ├── about/index.tsx             Bio and background story
│   ├── projects/index.tsx          Project cards (AiRise, GitHub Insights, OS...)
│   ├── experience/index.tsx        Work and teaching experience
│   ├── contact/index.tsx           Email, GitHub, LinkedIn links
│   └── chat/index.tsx              Eight chat panel — wraps features/chat
│
├── features/
│   └── chat/                       The only user interaction with stateful logic
│       ├── api/sendMessage.ts      POST /api/v1/chat/ with ChatRequest
│       ├── model/useChatStore.ts   Message history + loading state (Zustand)
│       └── ui/
│           ├── ChatInput.tsx       Text input + submit
│           ├── ChatBubble.tsx      Single user or assistant message bubble
│           └── SourceCard.tsx      Retrieved source citation below answers
│
├── entities/                       Shared domain types + base display components
│   ├── message/
│   │   ├── types.ts                ChatMessage, ChatRequest, ChatResponse
│   │   └── index.tsx               Base message display component
│   └── source/
│       ├── types.ts                RetrievalChunk, ChunkMetadata
│       └── index.tsx               Base source citation component
│
└── shared/                         No business logic — reusable across everything
    ├── ui/
    │   ├── Button.tsx              Primary / secondary / ghost button
    │   ├── Card.tsx                Surface card with warm or navy variant
    │   ├── Tag.tsx                 Tech stack / skill pill
    │   └── Spinner.tsx             Loading indicator
    ├── api/client.ts               Base fetch wrapper (API base URL from env)
    ├── config/env.ts               Typed import.meta.env wrappers
    └── lib/utils.ts                cn() helper and general utilities
```

---

## Design system

Dark gold and navy palette. All colors are defined as CSS variables in `app/styles/index.css` and documented with usage notes in `app/styles/color_palette.md`.

Key tokens:

| Token | Value | Used for |
|-------|-------|---------|
| `--background` | `#120D08` | Page base |
| `--surface-navy` | `#0F1C2E` | Project cards, nav on scroll |
| `--text-primary` | `#EDE0C8` | Headings, names |
| `--accent` | `#C4956A` | Gold — logo, CTA borders, labels |
| `--accent-navy` | `#8BA8C4` | Tech tags, active nav, secondary CTAs |

---

## Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start Vite dev server |
| `npm run build` | Type-check + production build |
| `npm run preview` | Preview production build locally |
| `npm run lint` | Run ESLint |
