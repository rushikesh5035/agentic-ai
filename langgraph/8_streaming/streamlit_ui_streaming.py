import streamlit as st
from chatbot import chatbot
from langchain_core.messages import HumanMessage

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

    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            message_chunk.content
            for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config={"configurable": {"thread_id": "thread-1"}},
                stream_mode="messages",
            )
        )

    st.session_state["messages_history"].append(
        {"role": "assistant", "content": ai_message}
    )
