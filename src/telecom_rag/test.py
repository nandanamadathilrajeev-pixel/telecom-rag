from retriever import build_retriever

retriever = build_retriever()

question = "How do I protect myself from SIM swap fraud?"

docs = retriever.invoke(question)

print(f"\nRetrieved {len(docs)} documents\n")

for i, doc in enumerate(docs, 1):
    print("=" * 60)
    print(f"DOCUMENT {i}")
    print("SOURCE:", doc.metadata.get("source"))
    print(doc.page_content)