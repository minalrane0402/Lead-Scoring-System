from fastapi import FastAPI
from lead_generator import generate_lead
from scorer import score_lead

app = FastAPI()

@app.get("/generate_lead")
def generate():
    return generate_lead()

@app.post("/score_lead")
def score(input_lead: dict):
    return score_lead(input_lead)