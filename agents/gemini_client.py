import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")

URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={API_KEY}"

def ask_gemini(prompt):
    headers = {"Content-Type": "application/json"}

    data = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    response = requests.post(URL, headers=headers, json=data)

    if response.status_code != 200:
        return f"Error: {response.text}"

    return response.json()["candidates"][0]["content"]["parts"][0]["text"]