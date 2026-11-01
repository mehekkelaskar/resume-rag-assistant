from tool import search_resume

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

agent = create_agent(
    model=ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0),
    tools=[search_resume],
    system_prompt=(
        "Answer questions using the resume search tool. "
        "If the resume does not contain the answer, say so."
    ),
)

