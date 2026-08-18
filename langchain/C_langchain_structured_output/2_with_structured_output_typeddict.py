import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from typing import TypedDict, Annotated, Literal

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="openai/gpt-oss-120b")

# Schema for data
# class Review(TypedDict):
#     summary: str
#     sentiment: str

# using Annotated to add description to the fields -> this will attached to the schema and will be used in the prompt to generate the output

class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes mentioned in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    # sentiment: Annotated[str, "return sentiment of the review either positive, negative or neutral"]

    # Using Literal to restrict the values of sentiment to either positive, negative or neutral
    sentiment: Annotated[Literal["positive", "negative", "neutral"], "return sentiment of the review either positive, negative or neutral"]
    pros: Annotated[list[str], "Write down all the pros inside a list"]
    cons: Annotated[list[str], "Write down all the cons inside a list"]

structured_model = model.with_structured_output(Review)

response = structured_model.invoke("""
I recently purchased the new XYZ smartphone and I must say, I'm quite impressed. The camera quality is outstanding, capturing vibrant and detailed photos even in low light conditions. The battery life is also commendable, lasting me through a full day of heavy usage without needing a recharge. However, I did find the device to be a bit on the heavier side, which makes it slightly uncomfortable to hold for extended periods. Overall, I would recommend this phone to anyone looking for a high-quality camera and long-lasting battery, but be prepared for its weight.
""")

print(response)
print(type(response)) # dict

