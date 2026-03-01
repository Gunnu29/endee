# 🧠 Smart Mistake Pattern Finder (AI Debug Assistant)

An AI-powered debugging assistant that analyzes **code snippets** or **error messages**, suggests fixes, and learns from previous mistakes using semantic similarity.

The system stores past mistakes and retrieves similar ones in the future to help developers solve problems faster.

✅ Fully local
✅ No paid APIs
✅ Semantic AI embeddings
✅ Confidence-based retrieval

---

# 🚀 Features

### 🔍 AI Error & Code Analysis

* Paste terminal error or code snippet
* Automatic rule-based + semantic analysis
* Suggested fix generated instantly

### 🧠 Memory of Past Mistakes

* Stores analyzed mistakes automatically
* Retrieves similar previous errors using vector search
* Improves over time with more data

### 🎯 Confidence Threshold Control

* Adjustable similarity threshold
* Filters weak matches
* Improves relevance

### ⚠ Problem Line Highlighting

* Detects suspicious lines in code or stack traces
* Displays line numbers for quick debugging

### 🤖 Semantic Similarity (Local AI)

Uses:

```
sentence-transformers/all-MiniLM-L6-v2
```

* Fast
* Lightweight (~90MB)
* Runs offline
* High accuracy

---

# 🏗️ Architecture

```
Streamlit UI (app.py)
        ↓
Analyzer Engine (analyzer.py)
        ↓
Embedding Generator (embedding.py)
        ↓
FastAPI Backend (backend.py)
        ↓
Vector Similarity Database (in-memory)
```

---

# 📂 Project Structure

```
.
├── app.py              # Streamlit frontend UI
├── analyzer.py         # AI analysis + retrieval logic
├── embedding.py        # Semantic embeddings
├── backend.py          # FastAPI vector database
├── store_mistake.py    # Store client
├── search_mistake.py   # Search client
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Gunnu29/endee.git
cd endee
```

## 2️⃣ Create Virtual Environment

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

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

You need **two terminals**.

## Terminal 1 — Start Backend

```bash
uvicorn backend:app --reload
```

Runs at:

```
http://localhost:8000
```

## Terminal 2 — Start Frontend

```bash
streamlit run app.py
```

---

# 🧪 Usage

1. Paste **code snippet** OR **error message**
2. Adjust **confidence threshold** (default 0.30 recommended)
3. Click **Analyze**
4. View:

   * Suggested fix
   * Similar past mistakes
   * Confidence score
   * Highlighted problem lines
5. Mistake is stored automatically for future learning

---

# 📊 Confidence Threshold Guide

| Threshold | Behavior               |
| --------- | ---------------------- |
| 0.20      | Loose matching         |
| 0.30      | Balanced (recommended) |
| 0.50      | Strict                 |
| 0.70+     | Very strict            |

Default recommended: **0.30**

---

# 📌 Example

### Input

```
ModuleNotFoundError: No module named 'flask'
```

### Output

```
Quick suggestion:
Package not installed or wrong environment.

Similar past mistakes:
- ModuleNotFoundError: No module named 'requests'
  Fix: Activate virtual environment and reinstall package

Confidence: 0.82
```

---

# 🔮 Future Improvements

* Persistent database (SQLite / Vector DB)
* Language auto-detection
* Multiple fix ranking
* Confidence visualization graph
* Code AST analysis
* Cloud deployment

---

# 👨‍💻 Author

Garvita Batra

---

# 📜 License

This project is for educational and demonstration purposes.
