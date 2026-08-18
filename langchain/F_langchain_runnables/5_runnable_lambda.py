# Runnablelambda 
# it is a runnable primitive that allow you to apply custom Python function within an AI pipeline.
# It acts as a middleware between AI components, enabling preprocessing, transformation, API calls, filtering, and post-processing of data.


import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="openai/gpt-oss-20b")

parser = StrOutputParser()

def word_count(text):
    return len(text.split())


# Now 'word_count' function converted into a RunnableLambda, which can be used in a RunnableSequence or RunnableParallel.
# runnable_word_count = RunnableLambda(word_count)

# result = runnable_word_count.invoke("This is a test sentence to count words.")  # This will return 8

# print(result)


prompt = PromptTemplate(
    template="Generate a Joke on {topic}.",
    input_variables=["topic"],
)

# Sequence chain that first generates a joke
joke_generator_chain = RunnableSequence(prompt, model, parser)

# Then, in parallel, we can run the joke generator and the word count function on the generated joke.
parallel_chain = RunnableParallel({
    'joke_generator': RunnablePassthrough(),
    # 'word_count': RunnableLambda(word_count),
    'word_count': RunnableLambda(lambda x: len(x.split())),
})

# Finally, we can create a final chain that first generates the joke and then runs the parallel chain on the generated joke.
final_chain = RunnableSequence(joke_generator_chain, parallel_chain)

response = final_chain.invoke({"topic": "AI Agents"})

final_response = """{} \n word count: {}""".format(response['joke_generator'], response['word_count'])

print(final_response)