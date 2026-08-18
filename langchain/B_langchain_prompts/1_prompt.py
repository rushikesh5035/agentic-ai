import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="openai/gpt-oss-120b")

st.header("LangChain Prompts with Groq")

# Static prompt 
# user_input = st.text_input("Enter your prompt:")

# Dynamic prompt with placeholders
paper_input = st.selectbox("Select Research Paper Name: ", ["selected...", "Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", "GPT-3: Language Models are Few-Shot Learners", "RoBERTa: A Robustly Optimized BERT Pretraining Approach", "XLNet: Generalized Autoregressive Pretraining for Language Understanding"])

explanation_style_input = st.selectbox("Select Explanation Style: ", [ "Beginner-friendly", "Technical", "Code-Oriented", "Mathematical"])

explanation_length_input = st.selectbox("Select Explanation Length: ", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])


# template
# template = PromptTemplate(
#     template="""
# Please summarize the research paper titled "{paper_input}" with the following specifications:
# Explanation Style: {explanation_style_input}
# Explanation Length: {explanation_length_input}
# 1. Mathematical Details:
#     - Include relevant mathematical equations if present in the paper.
#     - explain the mathematical concepts using simple, intuitive code snippets where applicable.
# 2. Analogies:
#     - Use relatable analogies to simplify complex concepts.
# if certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing or making assumptions.
# Ensure the summary is clear, accurate and aligned with the provided specifications.
# """,

# input_variables=["paper_input", "explanation_style_input", "explanation_length_input"],

# validate_template=True
# )


template = load_prompt("template.json")

# fill the placeholder
# formatted_prompt  = template.invoke({
#     'paper_input': paper_input,
#     'explanation_style_input': explanation_style_input,
#     'explanation_length_input': explanation_length_input
# })

# if st.button('Summarize'):
#     response = model.invoke(formatted_prompt)
#     st.write(response.content)


# using chain to combine prompt and model
if st.button('Summarize'):
    chain = template | model
    response = chain.invoke({
        'paper_input': paper_input,
        'explanation_style_input': explanation_style_input,
        'explanation_length_input': explanation_length_input
    })
    st.write(response.content) 