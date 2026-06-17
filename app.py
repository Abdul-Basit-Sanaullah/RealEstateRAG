import streamlit as st
from rag import generate_answer
from property_search import search_property

st.set_page_config(
    page_title="Real Estate Assistant",
    page_icon="🏠"
)

st.title("🏠 Real Estate Assistant")
st.subheader(
    "Ask about mortgages, home buying, property investment, or property prices"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

question = st.chat_input("Ask a real estate question...")

if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    try:
        answer = search_property(question)

        if answer is None:
            answer = generate_answer(question)

    except Exception as e:
        answer = f"Error: {str(e)}"

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.markdown(answer)
