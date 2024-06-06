import openai
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

class GPTAgent:
    def __init__(self):
        self.history = []

    def get_response(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        message = response['choices'][0]['message']['content']
        self.history.append({
            'prompt': prompt,
            'response': message,
            'timestamp': datetime.now().isoformat()
        })
        return message

    def save_history(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.history, f, indent=4)

    def load_history(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                self.history = json.load(f)

# Example usage
if __name__ == "__main__":
    agent = GPTAgent()
    agent.load_history('history.json')

    prompt = input("Enter your prompt: ")
    response = agent.get_response(prompt)
    print("Response:", response)

    agent.save_history('history.json')
