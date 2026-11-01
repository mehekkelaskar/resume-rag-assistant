# Resume Q&A Assistant

A retrieval-augmented generation (RAG) chat app that answers questions about a resume PDF. It uses Streamlit for the chat interface, Chroma for vector storage, and Google Gemini for embeddings and responses.

## Requirements

- Python 3.10 or later
- A Google AI Studio API key with access to the Gemini models used by this project
- A resume PDF that you are allowed to process

## Setup

1. Clone the repository and open its folder:

   ```powershell
   git clone <repository-url>
   cd RAG_Agent
   ```

2. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Create your local environment file and add your API key:

   ```powershell
   Copy-Item .env_example .env
   ```

   Edit `.env` and replace `your_google_api_key_here` with your Google API key.

5. Put your PDF at `data/resume.pdf`, or set `RESUME_PDF_PATH` in `.env` to another path. Relative paths are resolved from the project folder; absolute paths are also supported.

## Run

From the project folder, start the app with:

```powershell
streamlit run src/app.py
```

The app loads the PDF, creates embeddings, and stores the Chroma database in `data_storage/`. Ask questions in the chat interface.

## Configuration

| Variable | Required | Default | Description |
|---|---|---|---|
| `GOOGLE_API_KEY` | Yes | — | Google API key used by Gemini |
| `RESUME_PDF_PATH` | No | `data/resume.pdf` | Path to the PDF to search |

Gemini API usage may incur charges. Resume content is sent to Google to generate embeddings and responses. Do not process or publish personal information unless you have permission.

## Keep private files out of Git

`.env`, resume PDFs, and the generated `data_storage/` database are excluded by `.gitignore`. Do not commit API keys, personal documents, or generated vector data. If a key has already been pushed to a public repository, revoke it and create a new one.