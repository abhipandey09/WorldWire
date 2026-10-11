# 🌐 WorldWire — International News Portal

**WorldWire** is a real-time, consumer-facing international news portal built with an editorial design inspired by **BBC News** and **Reuters**, powered behind the scenes by **Google Gemini** with live Google Search Grounding and **Neon Serverless PostgreSQL**.

The website is consumer-facing with high-standard editorial design. An editorial news-gathering pipeline assists in tracking breaking and trending international events from primary press agencies. Stories are reviewed, fact-checked, and approved by the lead editor in the dedicated Editorial Admin Portal before public dissemination.

---

## 🌟 Key Reader & System Features

- **Consumer-First News Experience (BBC / Reuters Style)**:
  - Clean editorial masthead with global edition date bar.
  - Live **BREAKING NEWS** red banner ticker.
  - **Lead / Splash Story**: Prominent hero card with high-resolution photo, headline, executive summary, and byline.
  - **Category Navigation**: *Top Stories*, *World*, *Technology*, *Business & Economy*, *Science*, *Geopolitics*, *Politics*.
  - **Distraction-Free Reader Mode**: Click "Read Full Story" on any dispatch to open a serif reader layout with full multi-paragraph reporting, photo captions, and original press citations.
  - Clean public media footer (Editorial guidelines, Privacy Policy, Terms, Contact).
- **Editorial Review & Publishing Pipeline**:
  - Lead editor dashboard (`?page=admin`) with password-authenticated access (`abhishek`).
  - Wire stories are queued into an "In Review" staging pipeline for human review, editing, and authorization.
  - Ability to compose original dispatches directly through the editorial desk.
- **Silent Background Synchronization**:
  - Automatically updates on browser refresh without manual intervention.
  - Silent background auto-polling every 60 seconds keeps the reader's screen live and up to date.
- **Zero Hardcoded Secrets**:
  - All credentials (`DATABASE_URL` and `GOOGLE_GEMINI_API_KEY`) are read strictly from `.env`.

---

## 🏛️ System Architecture

```mermaid
flowchart TD
    subgraph Editorial Newsroom Engine
        SCHED["⏱️ APScheduler Wire Intake"] --> AGENT["📰 Primary Wire Intelligence"]
        AGENT --> QUEUE[("🗄️ In-Review Queue (news_articles)")]
        QUEUE --> ADMIN["✍️ Human Editorial Approval (Abhishek Pandey)"]
    end

    subgraph Consumer-Facing News Portal
        ADMIN --> PUB[("🗄️ Published Dispatches")]
        PUB --> UI["📰 WorldWire Reader Portal (mytomboy360.com)"]
        UI --> AUTO["🔄 Silent 60s Auto-Sync"]
    end
```

---

## 📁 Project Structure

- `app.py`: Clean, consumer-facing Streamlit website (no admin dials, pure reader UI).
- `database.py`: Neon PostgreSQL connection manager with cold-start retry mechanisms.
- `news_agent.py`: Gemini search grounding, article structuring, and image generation.
- `scheduler.py`: 5-hour background scheduler daemon.
- `requirements.txt`: Python dependencies.
- `.env`: Environment variables (API key and Database connection string).
- `.gitignore`: Excludes `.env` and compiled cache files.

---

## 🚀 Running WorldWire

1. Ensure `.env` is configured:
```env
GOOGLE_GEMINI_API_KEY=your_key
DATABASE_URL=postgresql://neondb_owner:...@...neon.tech/neondb?sslmode=require
```

2. Start the site:
```bash
streamlit run app.py
```
Open **[http://localhost:8501](http://localhost:8501)** in your browser.
