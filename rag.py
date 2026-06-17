import os
import chromadb

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

db = chromadb.PersistentClient(
    path="chroma_db"
)

collection = db.get_collection(
    "real_estate_docs"
)

def generate_answer(question):

    results = collection.query(
        query_texts=[question],
        n_results=5
    )

    context = "\n".join(
        results["documents"][0]
    )

    prompt = f"""
    You are a professional Real Estate Assistant.

    Use ONLY the following context.

    Context:
    {context}

    Question:
    {question}

    Answer clearly and professionally.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content