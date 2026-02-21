from agents.gemini_client import ask_gemini

def detect_anomaly(logs):
    prompt = f"""
You are an AIOps anomaly detection system.

Analyze the following logs and identify anomalies.

Logs:
{logs}

Return:
1. Detected anomaly
2. Root cause
3. Severity
"""

    return ask_gemini(prompt)