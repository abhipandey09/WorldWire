FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install curl for container health check
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy and install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Inject GoatCounter analytics tracking script into Streamlit static index.html
RUN python3 -c "import streamlit, os; p = os.path.join(os.path.dirname(streamlit.__file__), 'static', 'index.html'); c = open(p).read(); open(p, 'w').write(c.replace('</head>', '<script data-goatcounter=\"https://worldwire.goatcounter.com/count\" async src=\"//gc.zgo.at/count.js\"></script></head>'))"


# Copy application source code
COPY . .

# Expose standard Streamlit port (Render dynamically sets $PORT)
EXPOSE 8501

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:${PORT:-8501}/_stcore/health || exit 1

# Launch Streamlit with dynamic port binding for Render ($PORT)
CMD ["sh", "-c", "streamlit run app.py --server.port=${PORT:-8501} --server.address=0.0.0.0 --server.headless=true --browser.gatherUsageStats=false"]
