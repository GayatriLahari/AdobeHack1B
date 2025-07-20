FROM --platform=linux/amd64 python:3.10

WORKDIR /app

COPY ./app /app/app
COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    build-essential \
    libpoppler-cpp-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"

CMD ["python", "app/main.py"]
