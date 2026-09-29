import requests

def generate_answer(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3:latest",
                "prompt": prompt,
                "stream": False
            },
            timeout=180
        )

        if response.status_code == 200:
            return response.json().get("response", "").strip()
        else:
            return f"⚠ Ollama Error: {response.text}"

    except Exception as e:
        return f"⚠ Exception: {str(e)}"
