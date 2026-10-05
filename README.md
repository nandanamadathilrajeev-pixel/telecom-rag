# Telecom RAG Assistant

A customer-support chatbot for telecom issues, built as a retrieval-augmented generation (RAG) app. It answers questions by searching a knowledge base made of FAQs, resolved support tickets, and telecom guide PDFs, then uses an LLM to respond with grounded answers.

## Overview

This project is designed to help users troubleshoot common telecom problems such as:

- slow mobile internet
- dropped calls
- international roaming questions
- billing or plan issues
- SIM detection errors
- Wi-Fi calling setup
- network unlock and device compatibility concerns

The app combines:

- Chroma vector database for semantic retrieval
- Hugging Face embeddings for search
- LangChain orchestration for the RAG pipeline
- Groq-hosted LLM for answer generation
- Streamlit for a simple support chat interface

## Features

- RAG-powered responses grounded in telecom knowledge
- Retrieval across multiple data sources:
  - FAQ entries
  - resolved support tickets
  - PDF support guide content
- Conversation-friendly chat UI
- Sample questions for quick testing
- Local vector storage in the `chroma_store/` directory

## Project structure

```text
telecom-rag/
├── README.md
├── pyproject.toml
├── chroma_store/
├── src/
│   └── telecom_rag/
│       ├── app.py
│       ├── main.py
│       ├── rag_chain.py
│       ├── retriever.py
│       ├── ingest_faq.py
│       ├── ingest_pdf.py
│       ├── ingest_tickets.py
│       └── data/
│           ├── faq.csv
│           └── telecom_guide.pdf
└── ...
```

## Tech stack

- Python 3.14+
- LangChain
- Chroma
- Hugging Face sentence-transformers
- Streamlit
- Groq LLM
- pandas / PyPDF / FPDF

## Prerequisites

- Python 3.14 or newer
- A Groq API key
- Access to a terminal or VS Code integrated terminal

## Setup

1. Create and activate a virtual environment:

```bash
cd telecom-rag
python -m venv .venv
source .venv/bin/activate
```

2. Install the project dependencies:

```bash
pip install --upgrade pip
pip install -e .
```

3. Set your Groq API key:

```bash
export GROQ_API_KEY="your_api_key_here"
```

You can also place it in a `.env` file if your local environment supports that pattern for LangChain/Groq initialization.

## Build the knowledge base

This project expects the vector store to be generated before first use.

Run the ingestion scripts from the package directory:

```bash
cd src/telecom_rag
python ingest_faq.py
python ingest_tickets.py
python ingest_pdf.py
```

These scripts create and populate the Chroma collections:

- `faq`
- `tickets`
- `guides`

## Run the app

Start the Streamlit chat assistant:

```bash
cd src/telecom_rag
streamlit run app.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Run the CLI version

A terminal-based version is also available:

```bash
cd src/telecom_rag
python main.py
```

Type your question and press Enter. Use `quit` or `exit` to leave the chat.

## How it works

The app follows a standard RAG flow:

1. User asks a telecom question.
2. The retriever searches the Chroma collections.
3. Relevant FAQ, ticket, and guide passages are merged.
4. The model receives the question plus the retrieved context.
5. The LLM produces a grounded, customer-facing answer based only on retrieved material.

## Notes

- The knowledge base is stored locally in `chroma_store/`.
- If your data changes, rerun the ingestion scripts.
- If you want to add more support content, place new FAQ data or documents into the appropriate source and re-index.

## License

This project is intended for learning and demonstration purposes. Check your organization’s policy before deploying it in production environments.
