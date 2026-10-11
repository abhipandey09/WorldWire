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

# Copy application source code
COPY . .

# Inject GoatCounter analytics & Google AdSense scripts into Streamlit static index.html and copy ads.txt
RUN python3 -c "import streamlit, os, shutil; \
    p = os.path.join(os.path.dirname(streamlit.__file__), 'static', 'index.html'); \
    c = open(p).read(); \
    gc = '<script data-goatcounter=\"https://mytomboy360.goatcounter.com/count\" async src=\"//gc.zgo.at/count.js\"></script>'; \
    ads = '<script async src=\"https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6145233805932455\" crossorigin=\"anonymous\"></script>'; \
    open(p, 'w').write(c.replace('</head>', gc + ads + '</head>')); \
    s = os.path.join(os.path.dirname(streamlit.__file__), 'static'); \
    shutil.copy('ads.txt', os.path.join(s, 'ads.txt')) if os.path.exists('ads.txt') else None"

# Expose standard Streamlit port (Render dynamically sets $PORT)
EXPOSE 8501

# Healthcheck
HEALTHCHECK CMD curl --fail http://localhost:${PORT:-8501}/_stcore/health || exit 1

# Launch Streamlit with dynamic port binding for Render ($PORT)
CMD ["sh", "-c", "streamlit run app.py --server.port=${PORT:-8501} --server.address=0.0.0.0 --server.headless=true --browser.gatherUsageStats=false"]
