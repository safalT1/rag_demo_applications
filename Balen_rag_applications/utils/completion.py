import requests
from config import RAG_API_KEY, COMPLETION_MODEL, COMPLETION_URL


def generate_completion(prompt):
    """
    Send a prompt to the LLM and return the generated text response.

    Args:
        prompt (str): The full prompt including context and question.

    Returns:
        str: The model's text response.
    """
    headers = {
        "Authorization": f"Bearer {RAG_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": COMPLETION_MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 200,
        "temperature": 0.2,
    }

    response = requests.post(COMPLETION_URL, json=payload, headers=headers)

    if response.status_code != 200:
        raise ValueError(f"Completion error {response.status_code}: {response.text}")

    data = response.json()
    return data["choices"][0]["message"]["content"].strip()