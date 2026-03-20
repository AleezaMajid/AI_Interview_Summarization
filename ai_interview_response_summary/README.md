🚀 AI Interview Insight Engine

An AI-powered system that analyzes interview transcripts to generate structured summaries and extract key technical insights.

This module is designed as part of an AI Interview & Assessment System, focusing on transforming raw interview responses into meaningful, structured data for evaluation.

---

📌 Features

✅ Response Summarization using LLMs

✅ Technical Insight Extraction (keywords & concepts)

✅ Topic Clustering using Machine Learning

✅ Structured JSON Output for easy integration

✅ Modular Architecture for system integration

---

🏗️ Project Structure
AI_INTERVIEW_RESPONSE_SUMMARY
│
├── app.py                         # Main entry point
├── requirements.txt               # Dependencies
├── .env                           # API keys (ignored)
├── .gitignore                     # Ignore sensitive files
│
├── prompts
│   └── summarization_prompt.txt   # Prompt for LLM
│
├── schemas
│   └── summary_schema.json        # Output schema
│
├── engine
│   ├── summarizer.py              # LLM summarization logic
│   ├── insight_extractor.py       # Keyword extraction
│   └── topic_cluster.py           # ML-based clustering
│
├── sample_data
│   └── transcript.txt             # Sample input
│
└── README.md

---

⚙️ Tech Stack

Language: Python

LLM API: Google Gemini

Libraries:

google-genai

scikit-learn

nltk

python-dotenv

---

🚀 How It Works

📥 Input interview transcript

🧠 Summarization using Gemini API

🔍 Extract technical concepts (keywords)

📊 Cluster responses into topics

📤 Generate structured JSON output

---

🧠 Core Modules
🔹 Summarizer (engine/summarizer.py)

Uses Gemini API to generate structured summaries from transcripts.

🔹 Insight Extractor (engine/insight_extractor.py)

Extracts technical keywords using rule-based matching.

🔹 Topic Clustering (engine/topic_cluster.py)

Uses TF-IDF + KMeans to group responses into topics.

---

📦 Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/ai-interview-insight-engine.git
cd ai-interview-insight-engine

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Setup Environment Variables

Create a .env file:

GEMINI_API_KEY=your_api_key_here

---

▶️ Run the Project
python app.py
📥 Sample Input
Interviewer: Explain overfitting.
 Candidate: Overfitting occurs when a model performs well on training data but poorly on unseen data.

📤 Sample Output
{
  "domain": "Machine Learning",
  "technical_concepts": ["overfitting", "cnn", "tensorflow"],
  "strengths": ["Good conceptual understanding"],
  "weaknesses": ["Lacks depth"],
  "final_summary": "Candidate shows basic ML knowledge."
}

---

🔐 Security

.env is ignored to protect API keys

Virtual environments and cache files are excluded

---

🎯 Use Cases

AI-based interview evaluation

Candidate screening automation

HR analytics systems

LLM-based text analysis projects

---

🚀 Future Enhancements

📊 Candidate scoring system (1–10)

🌐 FastAPI backend integration

📈 Advanced clustering with embeddings

🖥️ Frontend dashboard

---

👨‍💻 Author

Developed as part of the AI Interview & Assessment System integration project.
