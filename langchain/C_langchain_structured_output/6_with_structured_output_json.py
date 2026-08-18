
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from typing import Optional


load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="openai/gpt-oss-120b")

# JSON Schema for the student model
# JSON schema used when you application is build using multiple languages. This is used to generate the JSON schema for the structured output of the model.
review_schema = {
    "title": "Review",
    "type": "object",
    "properties": {
        "key_themes":{
            "type": "array",
            "items": {
                "type": "string"
            },
        },
        "description": "A brief summary of the review",
    },
    "summary": {
        "type": "string",
        "description": "A brief summary of the review"
    },
    "sentiment": {
        "type": "string",
        "enum": ["positive", "negative", "neutral"],
        "description": "return sentiment of the review either positive, negative or neutral"
    },
    "pros": {
        "type": ["array", "null"],
        "items": {
            "type": "string"
        },
        "description": "Write down all the pros inside a list"
    },
    "cons": {
        "type": ["array", "null"],
        "items": {
            "type": "string"
        },
        "description": "Write down all the cons inside a list"
    },
    "name": {
        "type": ["string", "null"],
        "description": "Name of the reviewer if mentioned in the review"
    },
    "required": ["key_themes", "summary", "sentiment"]
}

structured_model = model.with_structured_output(review_schema)

response = structured_model.invoke("""
I recently purchased the new XYZ smartphone and I must say, I'm quite impressed. The camera quality is outstanding, capturing vibrant and detailed photos even in low light conditions. The battery life is also commendable, lasting me through a full day of heavy usage without needing a recharge. However, I did find the device to be a bit on the heavier side, which makes it slightly uncomfortable to hold for extended periods. Overall, I would recommend this phone to anyone looking for a high-quality camera and long-lasting battery, but be prepared for its weight.
""")

print(response)
print(type(response))