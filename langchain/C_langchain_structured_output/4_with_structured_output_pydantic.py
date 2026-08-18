import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from typing import Optional, TypedDict, Annotated, Literal
from pydantic import BaseModel, Field

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="openai/gpt-oss-120b")

class Review(BaseModel):

    key_themes: list[str] = Field(description="Write down all the key themes mentioned in the review in a list")

    summary: str = Field(description="A brief summary of the review")
    
    sentiment: Literal["positive", "negative", "neutral"] = Field(description="return sentiment of the review either positive, negative or neutral")

    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")

    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")

    name: Optional[str] = Field(default=None, description="Name of the reviewer if mentioned in the review")

structured_model = model.with_structured_output(Review)

response = structured_model.invoke("""
I recently purchased the new XYZ smartphone and I must say, I'm quite impressed. The camera quality is outstanding, capturing vibrant and detailed photos even in low light conditions. The battery life is also commendable, lasting me through a full day of heavy usage without needing a recharge. However, I did find the device to be a bit on the heavier side, which makes it slightly uncomfortable to hold for extended periods. Overall, I would recommend this phone to anyone looking for a high-quality camera and long-lasting battery, but be prepared for its weight.
""")

print(response)
print(type(response)) # dict
