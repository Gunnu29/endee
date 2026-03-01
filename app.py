import streamlit as st
from analyzer import analyze_and_store

st.set_page_config(page_title="Smart Mistake Finder", layout="wide")

st.title("🧠 Smart Mistake Pattern Finder")

st.markdown("Paste error text or code snippet. The system will analyze and suggest fixes.")

input_text = st.text_area("Paste code or error", height=250)

threshold = st.slider(
    "Similarity confidence threshold",
    0.0,
    1.0,
    0.25,
    0.05
)

auto_store = st.checkbox("Store for future learning", value=True)

if st.button("Analyze"):
    if input_text.strip():

        result = analyze_and_store(
            input_text,
            auto_store=auto_store,
            threshold=threshold
        )

        st.success("Analysis Complete")

        st.subheader("Suggested Fix")
        st.write(result["suggestion"])

        st.subheader("Confidence")
        st.write(result["confidence"])

        if result["problem_lines"]:
            st.subheader("⚠ Suspected Problem Lines")
            for ln, txt in result["problem_lines"]:
                st.code(f"Line {ln}: {txt}", language="python")

    else:
        st.warning("Please enter input.")