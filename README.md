# 🧠 Smart Mistake Pattern Finder

A lightweight AI-powered tool that helps developers **store mistakes**, **learn from them**, and **find similar past mistakes** instantly using semantic search.

This project uses **local embeddings (Sentence Transformers)** — completely **free** with no paid APIs.

---

## 🚀 Features

* ✅ Store mistakes and their fixes
* ✅ Semantic similarity search (AI-powered)
* ✅ Prevention by learning from past errors
* ✅ Streamlit-based simple UI
* ✅ FastAPI backend for vector storage & search
* ✅ Fully local — no external API cost

---

## 🏗️ Architecture

```
Streamlit UI (app.py)
        ↓
Embedding Generator (embedding.py)
        ↓
FastAPI Backend (backend.py)
        ↓
Vector Similarity Search
```

---

## 📂 Project Structure

```
.
├── app.py              # Streamlit frontend
├── backend.py          # FastAPI backend server
├── embedding.py        # Semantic embedding generation
├── store_mistake.py    # Store mistakes API client
├── search_mistake.py   # Search API client
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Gunnu29/endee.git
cd endee
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install streamlit fastapi uvicorn sentence-transformers scikit-learn numpy requests
```

---

## ▶️ Running the Project

You need **two terminals**.

### Terminal 1 — Start Backend

```bash
uvicorn backend:app --reload
```

Backend runs at:

```
http://localhost:8000
```

---

### Terminal 2 — Start Streamlit App

```bash
streamlit run app.py
```

App opens in browser automatically.

---

## 🧪 Usage

1. Enter a mistake description
2. Enter how you fixed it
3. Click **Store Mistake**
4. Search similar mistakes using different wording
5. Learn from previous solutions

---

## 🧠 Embedding Model

This project uses:

```
sentence-transformers/all-MiniLM-L6-v2
```

* Small (~90MB)
* Fast
* Runs locally
* No API cost

---

## 📌 Example

**Mistake**

```
ModuleNotFoundError when importing library
```

**Search**

```
python package not found
```

The system finds related mistakes using semantic similarity.

---

## 🔮 Future Improvements

* Persistent database (SQLite / Vector DB)
* User authentication
* Mistake categorization
* Cloud deployment
* Confidence score visualization

---

## 👨‍💻 Author

Garvita Batra

---

## 📜 License

This project is for educational and demonstration purposes.
