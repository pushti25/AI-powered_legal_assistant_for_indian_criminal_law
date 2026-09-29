import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "phi3:latest",
        "prompt": "Say hello in one sentence.",
        "stream": False
    }
)

print("Status:", response.status_code)
print("Response:", response.text)
