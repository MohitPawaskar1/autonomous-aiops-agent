from rag.vector_store import add_to_vector_store, search_vector_store


def store_incident(text):
    add_to_vector_store(text)
    print("\n✅ Incident stored in memory")


def summarize_text(text, max_chars=120):
    # Clean and shorten
    clean = text.replace("\n", " ").strip()
    return clean[:max_chars] + "..." if len(clean) > max_chars else clean


def search_similar_incidents(query):
    results = search_vector_store(query, top_k=1)

    if isinstance(results, str):
        return results

    # Return short preview
    short_results = [summarize_text(r) for r in results]
    return short_results