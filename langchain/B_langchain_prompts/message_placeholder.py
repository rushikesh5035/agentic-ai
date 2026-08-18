from langchain_core.prompts import ChatPromptTemplate, MessagePlaceholder

# Chat Template
chat_template = ChatPromptTemplate([
    ('system', "You are a helpful customer support agent."),
    MessagePlaceholder(variable_name="chat_history"),
    ('human', '{query}')
])

chat_history =[]

# Load chat history from a file
with open("chat_history.txt", "r") as f:
    chat_history.extend(f.readlines())

print(chat_history)

# Create prompt messages from chat history