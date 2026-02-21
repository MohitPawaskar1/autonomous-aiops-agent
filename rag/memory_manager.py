from rag.vector_store import add_text, search_text


def store_incident(report_text):
    meta = {
        "Root Cause": extract_root_cause(report_text),
        "Severity": extract_severity(report_text),
    }

    add_text(report_text, meta)


def search_similar_incidents(logs):
    results = search_text(logs, top_k=1)
    return results[0] if results else "No past incidents found."


def extract_root_cause(text):
    text_lower = text.lower()

    if "high memory" in text_lower:
        return "High memory usage"

    if "database" in text_lower:
        return "Database connection issue"

    if "cpu" in text_lower:
        return "High CPU usage"

    if "disk" in text_lower:
        return "Disk issue"

    return "Unknown"


def extract_severity(text):
    text_lower = text.lower()

    if "critical" in text_lower:
        return "Critical"

    if "high" in text_lower:
        return "High"

    if "medium" in text_lower:
        return "Medium"

    return "Unknown"