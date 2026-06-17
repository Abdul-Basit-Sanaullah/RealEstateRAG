import os
from pypdf import PdfReader
from groq import Groq
import streamlit as st

client = Groq(
api_key=st.secrets["GROQ_API_KEY"]
)

documents = []

for file in os.listdir("data"):
if file.endswith(".pdf"):

```
    reader = PdfReader(
        os.path.join("data", file)
    )

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    documents.append(text)
```

knowledge_base = "\n".join(documents)

def generate_answer(question):

```
prompt = f"""
You are a professional Real Estate Assistant.

Use ONLY the information below.

Context:
{knowledge_base[:15000]}

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
```
