import pdfplumber
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
 # use pre-downloaded model

def extract_chunks(file_path, doc_name):
    chunks = []
    with pdfplumber.open(file_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            if not text:
                continue
            for para in text.split("\n\n"):
                para_clean = para.strip()
                if len(para_clean) < 40:
                    continue
                embedding = model.encode(para_clean)
                chunks.append({
                    "document": doc_name,
                    "page": page_num,
                    "title": para_clean.split("\n")[0][:100],
                    "text": para_clean,
                    "embedding": embedding
                })
    return chunks
