import streamlit as st
from store_mistake import store_mistake
from search_mistake import search_similar

st.title("Smart Mistake Pattern Finder")

mistake = st.text_input("Describe your mistake")
fix = st.text_input("How did you fix it?")

if st.button("Store Mistake"):
    if mistake.strip() and fix.strip():
        try:
            store_mistake(mistake, fix)
            st.success("Mistake stored successfully!")
        except Exception as e:
            st.error(f"Error storing mistake: {e}")
    else:
        st.warning("Please enter both a mistake and its fix.")

query = st.text_input("Check similar mistake")

if st.button("Find Similar"):
    if query.strip():
        try:
            results = search_similar(query)
            if results:
                for r in results:
                    st.write("Similar mistake:", r["metadata"].get("mistake", "N/A"))
                    st.write("Fix:", r["metadata"].get("fix", "N/A"))
            else:
                st.info("No similar mistakes found.")
        except Exception as e:
            st.error(f"Error searching for similar mistakes: {e}")
    else:
        st.warning("Please enter a query to search.")