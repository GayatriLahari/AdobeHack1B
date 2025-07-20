import os
import json
from datetime import datetime
from document_parser import extract_chunks
from persona_matcher import match_relevant_sections

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

def load_context():
    with open(os.path.join(INPUT_DIR, "persona.json"), "r") as f:
        return json.load(f)

def main():
    context = load_context()
    documents = [f for f in os.listdir(INPUT_DIR) if f.endswith(".pdf")]

    all_chunks = []
    for doc in documents:
        path = os.path.join(INPUT_DIR, doc)
        chunks = extract_chunks(path, doc)
        all_chunks.extend(chunks)

    top_sections, sub_analysis = match_relevant_sections(context, all_chunks)

    result = {
        "metadata": {
            "input_documents": documents,
            "persona": context["persona"],
            "job_to_be_done": context["job"],
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": top_sections,
        "subsection_analysis": sub_analysis
    }

    with open(os.path.join(OUTPUT_DIR, "output.json"), "w") as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
