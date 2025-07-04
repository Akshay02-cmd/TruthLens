# 🧠 TruthLens – Fake News Detection App

TruthLens is an AI-powered web application designed to **detect fake news and misinformation** using Natural Language Processing and Machine Learning.

In an era where misinformation spreads faster than facts, this project aims to bring **truth to the surface** by helping users identify whether a news headline or article is likely **REAL** or **FAKE**.

---

## ✨ Inspiration

During a real terrorist incident, my family received a **fake message about an explosion** in our city — where my cousin was traveling. That false alert caused panic, health issues, and emotional trauma in our home.

**One fake message. So much real damage.**  
This motivated me to build **TruthLens** — to fight misinformation with machine learning.

---

## 🔍 Features

- ✅ Paste any news headline or article
- 🧠 ML model predicts whether it’s **Real** or **Fake**
- 📊 Trained on thousands of verified news articles
- 🌐 Simple, clean web interface
- ⚡ Fast and lightweight

---

## 🚀 Demo

Paste your news and click "Check"  
🔮 It tells you if it's:  
**✅ Likely Real** or **⚠️ Likely Fake**

---

## 📂 File Structure

TruthLens/
│
├── app.py # Flask backend
├── model/
│ ├── fake_news_model.pkl
│ └── vectorizer.pkl
├── static/
│ ├── css/style.css
│ └── js/script.js
├── templates/
│ └── index.html
├── dataset/
│ └── news.csv
├── notebook/
│ └── model_training.ipynb
├── requirements.txt
└── README.md


---

## 🛠️ Built With

- **Python** – Core language
- **Flask** – Web framework
- **Scikit-learn** – ML model
- **TfidfVectorizer + Logistic Regression** – Text classification
- **Pandas / NumPy** – Data processing
- **HTML / CSS / Bootstrap** – UI
- **Jupyter Notebook** – Model training
- [Fake News Dataset (Kaggle)](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)

---

## 📚 How to Run Locally

```bash
git clone https://github.com/Akshay02-cmd/truthlens.git
cd truthlens
pip install -r requirements.txt
python app.py


🧠 What I Learned
How NLP can be used to solve real-world problems

Training, testing, and evaluating ML models

Deploying models using Flask

Creating full-stack AI-powered web apps

📈 Future Scope
Add Chrome Extension to detect fake news on websites

Use advanced models (BERT, LLMs) for deeper analysis

Integrate WhatsApp/Telegram fact-check bots

🙌 Acknowledgements
Kaggle for the dataset

Scikit-learn and Flask communities

Hackathon mentors and reviewers

📬 Contact
Created by: Akshay Patil
📧 Email: [your-email@example.com]
