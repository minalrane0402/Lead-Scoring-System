import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def score_lead(lead: dict) -> dict:
    prompt = f"""
You are an AI assistant that scores sales leads between 0 and 100 based on quality, intent, and fit.
Return the score and an explanation.

Lead Details:
Name: {lead.get("name")}
Email: {lead.get("email")}
Company: {lead.get("company")}
Title: {lead.get("title")}
Industry: {lead.get("industry")}
Source: {lead.get("source_channel")}
Message: {lead.get("inquiry_message")}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a lead scoring assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    content = response.choices[0].message.content

    try:
        lines = content.strip().splitlines()
        score_line = next(line for line in lines if "score" in line.lower())
        score = int(''.join(filter(str.isdigit, score_line)))
        explanation = "\n".join(lines)
    except Exception:
        score = -1
        explanation = content

    return {
        "score": score,
        "explanation": explanation
    }

