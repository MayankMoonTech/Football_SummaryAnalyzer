import requests

def generate_analysis(prompt):

    url="http://localhost:11434/api/generate"

    payload={
        "model":"phi3",
        "prompt":prompt,
        "stream":False
    }

    response=requests.post(url,json=payload)

    return response.json()["response"]