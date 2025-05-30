Lead Scoring System

This is a simple project where I built a Lead Scoring System using Python. It takes information about a lead (like name, email, job title, company size, etc.) and gives a score between 0 to 100. The score shows how good or useful the lead is, along with a short reason.
The scoring is done using an LLM (Language Model). You can use OpenAI’s GPT models, or set up a free local model like `llama-cpp` so you don’t need to pay for anything.

🔧 Features:
- Generates dummy leads using `Faker` library
- Sends lead info to an LLM which gives:
  - A score- (0–100)
  - A short explanation
- Built using FastAPI to create two main routes:
  - `/generate-lead` – to create a fake lead
  - `/score-lead` – to score that lead using the LLM

🧠 Tools Used:
- Python
- FastAPI
- Faker (for lead data)
- LLM (OpenAI or free local model like llama-cpp)
- `.env` file (for storing API key if needed)

▶️ How to Run the Project

Step 1: Download or clone the project folder

bash:
git clone https://github.com/your-username/Lead-Scoring-System.git
cd Lead-Scoring-System

Step 2: Install the required libraries

Install these one by one in your terminal:

pip install fastapi
pip install uvicorn
pip install faker
pip install python-dotenv
pip install openai

(You can skip openai if you’re using a free local model.)

Step 3: Add .env file (if using OpenAI)

Create a .env file and add:

OPENAI_API_KEY=your-api-key-here

Step 4: Run the app

uvicorn app:app --reload

Then open this in your browser:
http://127.0.0.1:8000/docs

You can test the API there.

🆓 Using Without OpenAI
If you don’t want to use OpenAI API, you can use a free local model like llama-cpp. It runs on your laptop and doesn’t need internet or payment or you can use dummpy implementation.

💡 Ideas for Improvement
	•	Store leads and scores in a database
	•	Add a basic web interface
	•	Add login/signup
	•	Score many leads together
	•	Improve the scoring rules

🙋‍♀️ Made By
Minal Rane
Project: Intelligent Lead Scoring System
