import streamlit as st
from chatbot import chatbot
from langchain_core.messages import HumanMessage

# with st.chat_message("user"):
#     st.text("Hello!")

# with st.chat_message("assistant"):
#     st.text("Hello! How can I assist you today?")

# with st.chat_message("user"):
#     st.text("Hello, My name is Rushikesh")

# user_input = st.chat_input("Type your message here...")

# if user_input:
#     with st.chat_message("user"):
#         st.text(user_input)

# st.session_state -> dict ->

config = {"configurable": {"thread_id": "thread-1"}}

if "messages_history" not in st.session_state:
    st.session_state["messages_history"] = []

# loading the conversion history
for msg in st.session_state["messages_history"]:
    with st.chat_message(msg["role"]):
        st.text(msg["content"])

user_input = st.chat_input("Type here")

if user_input:
    # first add the msg to the history
    st.session_state["messages_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)

    response = chatbot.invoke(
        {"messages": [HumanMessage(content=user_input)]}, config=config
    )
    ai_message = response["messages"][-1].content

    st.session_state["messages_history"].append(
        {"role": "assistant", "content": ai_message}
    )
    with st.chat_message("assistant"):
        st.text(ai_message)
