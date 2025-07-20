# Approach Explanation – Adobe India Hackathon Round 1B
## Challenge: Persona-Driven Document Intelligence

### 🧠 Objective
We aim to build an intelligent system that extracts the most relevant sections and subsections from a set of documents based on:
- A **user persona** (e.g., researcher, student)
- A **job-to-be-done** (e.g., literature review, exam prep)

---

### 🛠️ Solution Overview

#### 1. Input Handling
- Accepts 3–10 PDFs and a `persona.json` file containing:
  - The user persona
  - The task to be done (job)
- The system reads all `.pdf` files from `/app/input` and loads the `persona.json` context.

#### 2. Document Parsing
- We use `pdfplumber` to extract text from each PDF.
- Text is chunked into paragraphs or heading-based segments.
- Each chunk is tagged with metadata: document name, page number, and a short title (usually the first sentence).

#### 3. Embedding Generation
- We use a small, CPU-friendly transformer model (`sentence-transformers`, e.g., `MiniLM`) to embed:
  - Each document chunk
  - The combined persona + job description query
- All embedding work is done offline inside the Docker container.

#### 4. Semantic Matching
- Cosine similarity is used to rank all document chunks based on their relevance to the persona’s task.
- Top sections are selected, and their metadata (title, page, doc name) is stored with an `importance_rank`.

#### 5. Subsection Refinement
- The top-ranked sections are further broken down and stored in a `subsection_analysis` block, which contains:
  - Cleaned text
  - Source info (doc name, page number)
  - A human-readable short title

---

### 📤 Output Format
The system generates `output.json` in this structure:
- `metadata`: documents, persona, job, timestamp
- `extracted_sections`: ranked sections
- `subsection_analysis`: clean summaries for top sections

---

### ✅ Constraints Handling
- **Offline compatible**: All models and dependencies are stored inside the container. No internet required.
- **Model size < 1GB**: Uses compact sentence transformer.
- **Execution time < 60s** for up to 5 documents.
- **CPU-only** processing.

---

### 🧪 Example Use Cases
| Persona | Task |
|--------|------|
| PhD Researcher | Literature review |
| Investment Analyst | Compare R&D and revenue trends |
| Chemistry Student | Summarize exam topics |

---

### 🧩 Key Tools & Libraries
- `pdfplumber` – for PDF parsing
- `sentence-transformers` – for semantic embeddings
- `torch` – lightweight CPU inference
- `Docker` – for reproducibility and platform compliance

---

### 🔒 Modularity
This system is designed with modular Python scripts so it can be easily extended in Round 2 (interactive webapp).

