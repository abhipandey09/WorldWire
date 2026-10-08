# 🌐 WorldWire — International News Portal

**WorldWire** is a real-time, consumer-facing international news portal built with an editorial design inspired by **BBC News** and **Reuters**, powered behind the scenes by **Google Gemini** with live Google Search Grounding and **Neon Serverless PostgreSQL**.

The website is 100% reader-facing with zero admin clutter, technical dials, or settings exposed to the public. Behind the scenes, an autonomous 5-hour background engine continuously tracks breaking and trending world events, synthesizes journalistic reports, attaches high-resolution editorial imagery, and persists them into PostgreSQL. When a user visits or refreshes the page, the site automatically reflects the newest developments.

---

## 🌟 Key Reader & System Features

- **Consumer-First News Experience (BBC / Reuters Style)**:
  - Clean editorial masthead with global edition date bar.
  - Live **BREAKING NEWS** red banner ticker.
  - **Lead / Splash Story**: Prominent hero card with high-resolution photo, headline, executive summary, and byline.
  - **Category Navigation**: *Top Stories*, *World*, *Technology*, *Business & Economy*, *Science*, *Geopolitics*, *Politics*.
  - **Distraction-Free Reader Mode**: Click "Read Full Story" on any dispatch to open a serif reader layout with full multi-paragraph reporting, photo captions, and original press citations.
  - Clean public media footer (Editorial guidelines, Privacy Policy, Terms).
- **Autonomous 5-Hour News Pipeline**:
  - Automatically runs in the background in code using APScheduler.
  - Uses `gemini-3.8-flash` with official Google Search tool grounding to discover and verify real-time events from the live web.
  - Uses `gemini-2.5-flash-image` to generate custom photojournalistic visuals (with high-res editorial photo fallback), compressed and stored directly into PostgreSQL as base64 URIs.
- **Silent Background Synchronization**:
  - Automatically updates on browser refresh without manual intervention.
  - Silent background auto-polling every 60 seconds keeps the reader's screen live and up to date.
- **Zero Hardcoded Secrets**:
  - All credentials (`DATABASE_URL` and `GOOGLE_GEMINI_API_KEY`) are read strictly from `.env`.

---

## 🏛️ System Architecture

```mermaid
flowchart TD
    subgraph Autonomous Background Engine
        SCHED["⏱️ APScheduler (5-Hour Cycle)"] --> AGENT["🤖 Gemini 3.8 Flash + Web Search"]
        AGENT --> IMG["📸 Gemini 2.5 Flash Image Model"]
        IMG --> DB[("🗄️ Neon PostgreSQL (news_articles)")]
    end

    subgraph Consumer-Facing News Portal
        DB --> UI["📰 WorldWire Reader Portal (BBC / Reuters Style)"]
        UI --> AUTO["🔄 Silent 60s Auto-Sync & Instant Refresh"]
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
