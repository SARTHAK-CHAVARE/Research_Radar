# 📡 ResearchRadar

ResearchRadar is an autonomous AI-powered research digest agent built for the OpenClaw Hackathon 2026.

It automatically fetches the latest AI research papers, trending GitHub repositories, and AI news articles, summarizes them using Groq LLMs, generates a professional DOCX digest, and delivers it through Telegram and Email.

---

# 🚨 Problem Statement

AI researchers, developers, and students face information overload.

Every day:
- Hundreds of new AI papers are published on ArXiv
- Trending AI repositories constantly appear on GitHub
- Important AI news gets buried under noise
- Researchers spend hours filtering relevant content manually

There is no simple autonomous system that:
- Curates relevant GenAI research
- Summarizes technical papers into readable insights
- Tracks trending repositories
- Delivers everything in one concise digest

---

# ✅ Solution

ResearchRadar solves this problem by acting as an autonomous AI research assistant.

The system:
1. Fetches latest AI papers from ArXiv
2. Fetches trending AI repositories from GitHub
3. Fetches latest AI news headlines
4. Filters already-seen papers using memory
5. Summarizes papers using Groq LLM
6. Picks the most novel paper ("Top Pick")
7. Generates a professional DOCX digest
8. Sends the digest through Telegram and Email

---

# ✨ Features

- 📡 ArXiv AI paper monitoring
- 🔥 Trending GitHub repository tracking
- 🧠 Groq LLM-powered summarization
- ⭐ Automatic “Top Pick” selection
- 📄 DOCX digest generation
- 📬 Telegram delivery
- 📧 Gmail SMTP integration
- 💾 Memory system to avoid duplicate papers
- ⏰ Autonomous weekly execution

---

# 🏗️ Project Architecture

```text
                ┌──────────────────┐
                │   ArXiv API      │
                └────────┬─────────┘
                         │
                ┌────────▼─────────┐
                │ GitHub API       │
                └────────┬─────────┘
                         │
                ┌────────▼─────────┐
                │ Google News RSS  │
                └────────┬─────────┘
                         │
                ┌────────▼─────────┐
                │ Data Fetch Layer │
                └────────┬─────────┘
                         │
                ┌────────▼─────────┐
                │ Memory Filter    │
                └────────┬─────────┘
                         │
                ┌────────▼─────────┐
                │ Groq Summarizer  │
                └────────┬─────────┘
                         │
                ┌────────▼─────────┐
                │ DOCX Builder     │
                └────────┬─────────┘
                         │
          ┌──────────────┴──────────────┐
          │                             │
   ┌──────▼──────┐              ┌──────▼──────┐
   │ Telegram    │              │ Gmail SMTP  │
   └─────────────┘              └─────────────┘