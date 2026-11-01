import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


project_root = Path(__file__).resolve().parents[1]
load_dotenv(project_root / ".env")

resume_path = Path(os.getenv("RESUME_PDF_PATH", "data/resume.pdf"))
if not resume_path.is_absolute():
    resume_path = project_root / resume_path

loader = PyPDFLoader(str(resume_path))
pdf_doc=loader.load()

#split the data into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splitted_data=text_splitter.split_documents(pdf_doc)



