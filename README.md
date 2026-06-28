# 🚀 AI Resume & Interview Coach

An AI-powered web application that analyzes resumes against job descriptions, provides ATS-style feedback, and helps users improve their chances of landing interviews.

Built using **Python**, **Flask**, and **Google Gemini AI**, this project demonstrates the use of Large Language Models (LLMs) in career intelligence and recruitment.

---

## 📌 Features

### ✅ Resume Analysis
- Upload resume in PDF format
- Extracts resume text automatically
- Compares resume with a job description
- Provides AI-powered resume feedback

### ✅ ATS Review
- ATS Compatibility Score
- Missing Skills
- Resume Strengths
- Weaknesses
- Actionable Improvement Suggestions

### 🔄 Upcoming Features
- AI Mock Interview
- Personalized Interview Questions
- Speech Confidence Analysis
- Video Interview Analysis
- Resume Score Dashboard
- PDF Report Generation
- Interview Performance Tracking

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask

### AI
- Google Gemini API
- Prompt Engineering

### Resume Processing
- pdfplumber

### Frontend
- HTML
- CSS
- JavaScript (Upcoming)

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```
AI_Resume_Coach/
│
├── app.py
├── gemini_service.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
├── uploads/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Haamid619/AI-Resume-Coach.git
```

### Move into the project folder

```bash
cd AI-Resume-Coach
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📖 How It Works

1. User uploads a resume (PDF).
2. Resume text is extracted using `pdfplumber`.
3. User enters a job description.
4. Resume and job description are sent to Google Gemini.
5. Gemini analyzes the resume and returns:
   - ATS Score
   - Missing Skills
   - Strengths
   - Weaknesses
   - Improvement Suggestions
6. Results are displayed in the browser.

---

## 💡 Future Improvements

- User Authentication
- Resume History
- Dashboard Analytics
- AI Mock Interviews
- Voice Feedback
- Eye Contact Detection
- Facial Expression Analysis
- Company-Specific Interview Preparation
- Resume PDF Export
- Resume Builder

---

## 📷 Screenshots

### Home Page

*(Add screenshot here)*

### Resume Analysis

*(Add screenshot here)*

---

## 🎯 Learning Outcomes

This project helped me learn:

- Flask Web Development
- REST API Integration
- Google Gemini API
- Environment Variables
- Prompt Engineering
- PDF Processing
- Git & GitHub
- Python Project Structure

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

## 👨‍💻 Author

**Haamid Ali**

- GitHub: https://github.com/Haamid619
- LinkedIn: https://linkedin.com/in/haamidali619

