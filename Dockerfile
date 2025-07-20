FROM --platform=linux/amd64 python:3.10

WORKDIR /app

# Copy code and requirements
COPY ./app /app/app
COPY requirements.txt .

# Optional: install system tools (for pdfplumber/poppler)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpoppler-cpp-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 🧠 Download model during build so it's cached in the image
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"

# Run the main script
CMD ["python", "app/main.py"]
