from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def generate_mcqs(text, count=5):
    prompt = f"""
    Generate {count} MCQs from the following text:

    TEXT:
    {text}

    Format for each MCQ:
    Q: <question>
    A) option1
    B) option2
    C) option3
    D) option4
    Correct Answer: <option letter>
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
