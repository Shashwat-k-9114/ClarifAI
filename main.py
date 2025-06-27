import requests
import json
import re

API_KEY = "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"  # Your OpenRouter or other key
MODEL = "mistralai/mixtral-8x7b-instruct"

def load_prompt_template():
    with open("prompt_template.txt", "r") as f:
        return f.read()

def extract_first_json(text):
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        return match.group(0)
    return None

def get_structured_output(vague_input):
    prompt = load_prompt_template().replace("{input}", vague_input)

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://chat.openai.com"
    }

    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )

    try:
        result = response.json()
        message = result["choices"][0]["message"]["content"]
        json_part = extract_first_json(message)
        return json.loads(json_part)
    except Exception as e:
        print("\n❌ API Error or Unexpected Response:")
        print(json.dumps(result, indent=2))
        print(f"\nException: {e}")
        return None
    raw_response = call_llm(user_input)  # assume this returns a string
    try:
        # Try direct JSON parse
        if isinstance(raw_response, str):
            response_data = json.loads(raw_response)
        elif isinstance(raw_response, dict):
            response_data = raw_response
        else:
            raise ValueError("Unsupported response format")

        # Validate that required keys exist
        if "intent" in response_data and "entities" in response_data:
            return response_data
        else:
            print("❌ Missing required keys in response.")
            return None

    except Exception as e:
        print(f"❌ API Error or Unexpected Response:\n{raw_response}")
        print(f"Exception: {e}")
        return None