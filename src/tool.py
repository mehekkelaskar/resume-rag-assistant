
from langchain_core.tools import tool
from store_data import vectors_store
@tool
def search_resume(query: str) -> str:
    """Find relevant information in Mehak's resume PDF."""
    matches = vectors_store.similarity_search(query, k=4)
    if not matches:
        return "No relevant information found."
    return "\n\n".join(doc.page_content for doc in matches)
    