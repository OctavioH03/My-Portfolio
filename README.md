# 🗂️ Portfolio — Octavio Hernandez

> CS graduate · Software Engineer · RAG Chatbot Builder

---

## 👋 About

CS graduate from CSU Sacramento (Dec 2025, 3.92 GPA, Summa Cum Laude) and current software engineer. This repo contains the knowledge base documents, project context, and supporting materials that power a RAG chatbot built to answer questions about my background, projects, and experience.

---

## 🤖 The Chatbot

The centerpiece of this portfolio is a RAG-powered chatbot that lets you ask questions about me directly — my projects, experience, skills, and background — and get accurate, grounded answers pulled from a structured knowledge base.

No hallucinations. Just retrieval.

---

## 🛠️ Stack

| Layer | Tech |
|---|---|
| 🧠 AI | OpenAI API (embeddings + completions) |
| ⚙️ Backend | FastAPI |
| 🗄️ Database | Supabase + pgvector |
| 🎨 Frontend | React + Vite + Tailwind CSS |
| 🚀 Deployment | Railway (backend) · Vercel (frontend) |

---

## 📁 Repo Structure

```
portfolio/
├── 📄 documents/     # Markdown knowledge base (bio, resume, projects...)
├── ⚙️ backend/       # FastAPI app + RAG pipeline (coming soon)
└── 🎨 frontend/      # React portfolio site (coming soon)
```

---

## 📚 Knowledge Base

The `/documents` folder contains structured markdown files with YAML frontmatter. These are chunked, embedded, and stored in Supabase with pgvector to power semantic search at query time.

Files include: `bio.md`, `resume.md`, `jj_internship.md`, `airise.md`, `contact.md`, and more.

---

## 🚧 Status

- [X] Knowledge base documents
- [ ] RAG pipeline (FastAPI + OpenAI + Supabase)
- [ ] Portfolio frontend (React + Vite + Tailwind)
- [ ] Deployment (Railway + Vercel)

---

## 📬 Contact

- 🐙 GitHub: https://github.com/OctavioH03
- 💼 LinkedIn: https://linkedin.com/in/octavio-h-8o8
- 📧 Email: octaviohernandez.h2@gmail.com