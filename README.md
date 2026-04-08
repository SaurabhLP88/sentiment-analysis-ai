# 🧠 AI Sentiment Analyzer (Flask + HuggingFace)

## 🚀 Project Overview
This is an AI-powered Sentiment Analysis web application built using Flask. The app allows users to input text and instantly receive sentiment classification as **Positive, Negative, or Neutral**, along with a confidence score. It integrates with HuggingFace's NLP model for real-time analysis and includes fallback handling to ensure the app remains functional even if the external API fails.

---

## ✨ Features
- 🔍 Real-time sentiment analysis
- 🤖 Integration with HuggingFace NLP model
- ⚡ Fast and responsive Flask backend
- 🎯 Confidence score output
- 🔄 Graceful error handling & fallback logic
- ⏳ Loading animation for better UX
- 🌐 Simple and clean UI

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3 (Bootstrap)
- JavaScript (AJAX / XMLHttpRequest)

### Backend
- Python
- Flask

### AI / NLP
- HuggingFace Inference API
  - Model: `cardiffnlp/twitter-roberta-base-sentiment`

### Tools & Concepts
- REST API Integration
- JSON handling
- Async request handling
- Error handling (try/catch)
- Unit testing & mocking

---

## 📂 Project Structure
```
flask_project_one/
│
├── server.py
├── requirements.txt
├── Procfile
├── SentimentAnalysis/
│   ├── __init__.py
│   └── sentiment_analysis.py
├── templates/
│   └── index.html
├── static/
│   └── mywebscript.js
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/flask-transaction-app.git
cd flask_project_one
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add HuggingFace Token
Create a `.env` file:
```
HF_TOKEN=your_token_here
```

---

## ▶️ Run the Application
```bash
python server.py
```

Open in browser:
```
http://localhost:5000
```

---

## 🧪 Example Usage
Input:
```
I love working with Python
```

Output:
```
The given text has been identified as POSITIVE with a score of 0.98
```

---

## ⚠️ Known Issues & Handling
- External API may fail → fallback logic ensures app still works
- HuggingFace model may take time to load → loading animation added
- Token permissions required for inference API

---

## 🔐 Security Note
- Do NOT expose API tokens in code
- Use `.env` file for storing sensitive keys

---

## 🚀 Future Improvements
- 🌈 UI enhancements (colors, charts, emojis)
- 📊 Sentiment history tracking
- ⚛️ React frontend integration
- ☁️ Deployment with Render / Netlify
- 🤖 Switch to OpenAI or multi-model support

---

## 👨‍💻 About the Developer

**Sentiment Analyzer** is designed and developed by **Saurabh Lakhanpal** – Full Stack & Front-End Developer.  
📧 Email: [firsty111@gmail.com]  
🔗 GitHub: [GitHub Profile](https://github.com/SaurabhLP88/)

---

## ⭐ If you like this project
Give it a star ⭐ on GitHub!

