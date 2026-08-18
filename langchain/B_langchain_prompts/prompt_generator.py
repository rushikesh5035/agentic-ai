from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {explanation_style_input}
Explanation Length: {explanation_length_input}
1. Mathematical Details:
    - Include relevant mathematical equations if present in the paper.
    - explain the mathematical concepts using simple, intuitive code snippets where applicable.
2. Analogies:
    - Use relatable analogies to simplify complex concepts.
if certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing or making assumptions.
Ensure the summary is clear, accurate and aligned with the provided specifications.
""",

input_variables=["paper_input", "explanation_style_input", "explanation_length_input"],

validate_template=True
)

template.save("template.json")