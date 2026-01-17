FROM python:3.13-slim

WORKDIR /app

# --- Streamlit configuration defaults ---
ENV STREAMLIT_SERVER_PORT=8501 \
STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
STREAMLIT_SERVER_HEADLESS=true \
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/Master-Nox/MawaeNet-Website.git .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["sh", "-c", "streamlit run 0_MultiPage.py --server.port=${STREAMLIT_SERVER_PORT} --server.address=${STREAMLIT_SERVER_ADDRESS}"]