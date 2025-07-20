from sentence_transformers import util, SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')


def match_relevant_sections(context, chunks):
    query = f"{context['persona']} - Task: {context['job']}"
    query_vec = model.encode(query)

    ranked = []
    for chunk in chunks:
        score = util.cos_sim(query_vec, chunk["embedding"]).item()
        ranked.append((chunk, score))

    ranked.sort(key=lambda x: x[1], reverse=True)

    top_sections = []
    sub_analysis = []

    for i, (chunk, score) in enumerate(ranked[:10]):
        top_sections.append({
            "document": chunk["document"],
            "page_number": chunk["page"],
            "section_title": chunk["title"],
            "importance_rank": i + 1
        })

        sub_analysis.append({
            "document": chunk["document"],
            "page_number": chunk["page"],
            "section_title": chunk["title"],
            "refined_text": chunk["text"]
        })

    return top_sections, sub_analysis
