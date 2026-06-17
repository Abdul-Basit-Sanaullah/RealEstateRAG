import os
import chromadb
from pypdf import PdfReader

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="real_estate_docs"
)

doc_id = 0

for file in os.listdir("data"):

    if file.endswith(".pdf"):

        print(f"Processing {file}")

        reader = PdfReader(
            os.path.join("data", file)
        )

        text = ""

        for page in reader.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted

        chunks = [
            text[i:i+1000]
            for i in range(0, len(text), 1000)
        ]

        for chunk in chunks:

            collection.add(
                documents=[chunk],
                ids=[str(doc_id)]
            )

            doc_id += 1

print("Database Created Successfully!")