import re
from search_mistake import search_similar
from store_mistake import store_mistake


# ---------------- RULE BASED SUGGESTIONS ----------------

RULES = [
    (r"ModuleNotFoundError", "Package not installed or wrong environment. Activate venv and reinstall package."),
    (r"JSONDecodeError", "Invalid JSON format. Check for trailing commas or missing quotes."),
    (r"Address already in use", "Port already used. Kill process or change port."),
    (r"Connection refused", "Service not running or wrong host/port."),
    (r"KeyError", "Dictionary key missing. Use .get() or check key existence."),
    (r"IndexError", "Index out of range. Check list size before accessing."),
]


def rule_based_suggestion(text):
    for pattern, suggestion in RULES:
        if re.search(pattern, text, re.IGNORECASE):
            return suggestion, 0.8
    return "", 0.0


# ---------------- EXTRACT CORE ERROR TEXT ----------------

def extract_core_text(text: str):
    """
    Extract most relevant error line for better similarity search.
    """
    lines = text.split("\n")

    for line in reversed(lines):
        if "Error" in line or "Exception" in line:
            return line.strip()

    return text.strip()


# ---------------- HIGHLIGHT PROBLEM LINES ----------------

def highlight_problem_lines(text: str):
    lines = text.split("\n")
    suspects = []

    keywords = [
        "error",
        "exception",
        "traceback",
        "import",
        "failed",
        "not found",
        "KeyError",
        "IndexError",
        "TypeError",
    ]

    for i, line in enumerate(lines):
        if any(k.lower() in line.lower() for k in keywords):
            suspects.append((i + 1, line))

    # Avoid duplicate last line
    if lines and (len(lines), lines[-1]) not in suspects:
        suspects.append((len(lines), lines[-1]))

    return suspects


# ---------------- MAIN ANALYSIS FUNCTION ----------------

def analyze_and_store(input_text: str,
                      auto_store=True,
                      top_k=3,
                      threshold=0.25):

    if not input_text.strip():
        raise ValueError("Input cannot be empty")

    # 1️⃣ Rule suggestion
    rule_fix, confidence = rule_based_suggestion(input_text)

    # 2️⃣ Extract core text for similarity
    core_text = extract_core_text(input_text)

    # 3️⃣ Search similar mistakes
    hits = search_similar(core_text, top_k=top_k) or []

    # 4️⃣ Apply similarity threshold
    hits = [h for h in hits if h.get("score", 0) >= threshold]

    # 5️⃣ Use similarity score as confidence if available
    if hits:
        confidence = max(h["score"] for h in hits)

    # 6️⃣ Build suggestion output
    suggestion_parts = []

    if rule_fix:
        suggestion_parts.append(f"Quick suggestion:\n{rule_fix}")

    if hits:
        suggestion_parts.append("\nSimilar past mistakes:")

        for h in hits:
            md = h["metadata"]
            suggestion_parts.append(
                f"- {md.get('content','')}\n  Fix: {md.get('fix','')}"
            )

    if not suggestion_parts:
        suggestion_parts.append("No strong matches found. Provide more details.")

    final_suggestion = "\n\n".join(suggestion_parts)

    # 7️⃣ Highlight suspected lines
    problem_lines = highlight_problem_lines(input_text)

    # 8️⃣ Store clean fix (IMPORTANT — no recursion)
    if auto_store:
        try:
            clean_fix = rule_fix if rule_fix else "Analyzed mistake"

            store_mistake(
                input_text,
                clean_fix,
                {"auto": True}
            )
        except Exception as e:
            print("Store failed:", e)

    return {
        "suggestion": final_suggestion,
        "confidence": round(confidence, 3),
        "matches": hits,
        "problem_lines": problem_lines
    }