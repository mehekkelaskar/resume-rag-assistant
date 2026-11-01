#entry point for the project
import streamlit as st
from model import agent

st.title("ASK ANY QUERY RELATED TO THE RESUME MEHAK")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    role=msg["role"]
    content=msg["content"]
    st.chat_message(role).markdown(content)

query=st.chat_input("Ask your query here")



if query:
    st.chat_message("user").markdown(query)
    st.session_state.messages.append({"role":"user","content":query})
    result = agent.invoke({
    "messages": [{"role": "user", "content": query}]})
    res = result["messages"][-1].content

    if isinstance(res, str):
        response = res
    else:
        response = "\n".join(
        block["text"]
        for block in res
        if isinstance(block, dict) and block.get("type") == "text"
    )

    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
   




