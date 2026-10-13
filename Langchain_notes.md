# LangChain Notes

## 1. What Is LangChain?

LangChain is an open-source framework for building applications powered by large language models (LLMs).

An LLM can generate text, answer questions, summarize documents, and reason about instructions. However, a useful application usually needs more than a single model call. It may need prompts, external data, tools, structured results, memory, retrieval, and multiple processing steps.

LangChain provides reusable abstractions and integrations for connecting these parts into an application.

### Simple Definition

> LangChain is a framework that helps developers connect language models with prompts, data, tools, workflows, and application logic.

### What Can Be Built with LangChain?

- Chatbots and conversational assistants
- Retrieval-Augmented Generation (RAG) applications
- Document question-answering systems
- Research assistants
- Summarization and classification pipelines
- Agents that use tools and APIs
- Structured data extraction systems
- Multi-step LLM workflows

### Basic LangChain Application

```text
User Input
    ↓
Prompt Template
    ↓
Language Model
    ↓
Output Parser
    ↓
Application Response
```

LangChain does not replace the language model. It provides the application layer around the model.

---

## 2. Problems Before LangChain

Before using a framework, \*developers could call an LLM directly through a provider's SDK. That is sufficient for a small experiment:

```python
response = client.chat.completions.create(
    model="some-model",
    messages=[{"role": "user", "content": "Explain RAG"}],
)
```

The difficulty starts when the application grows.

### 2.1 Repetitive Provider-Specific Code

Different providers may have different SDKs, authentication methods, request formats, message formats, and response objects. Changing from OpenAI to Gemini, Groq, or Ollama can require changes throughout the codebase.

### 2.2 Difficult Prompt Management

Without reusable templates, prompts are often written as long strings inside application code. This makes reuse, testing, versioning, and system/user message management difficult.

### 2.3 Manual Multi-Step Workflows

If an application needed multiple model calls, we had to manually pass the output of one step into the next step. This created complicated and difficult-to-maintain code.

### 2.4 Difficult Structured Output Handling

An LLM naturally returns text, while software often needs predictable data:

```json
{
  "sentiment": "positive",
  "score": 0.92,
  "reason": "The customer praised the product."
}
```

Without parsing and validation, developers must write their own JSON conversion, schema checking, retries, and error handling.

### 2.5 No Direct Access to Private or Current Information

The model may not know internal documents, today's product information, recently updated policies, or data in our database. A separate pipeline is required to load, split, embed, store, retrieve, and pass relevant context to the model.

### 2.6 Tool Integration Was Manual

Connecting an LLM to search, databases, APIs, calculators, or application functions required custom schemas, tool-selection logic, execution code, and result handling.

### 2.7 Limited Observability

It was difficult to inspect a complete LLM workflow, including the prompt sent to the model, intermediate results, latency, token usage, and errors.

### Before LangChain

```text
Application Code
    ├── Provider-specific model SDK
    ├── Manually formatted prompts
    ├── Custom output parsing
    ├── Custom document ingestion
    ├── Custom vector search
    ├── Custom tool execution
    └── Custom logging and tracing
```

> A direct SDK is not wrong. It is often enough for one simple model call. The problems appear when the application becomes multi-step, data-aware, or tool-using.

---

## 3. What Does LangChain Solve?

LangChain solves the integration and orchestration problems involved in building LLM applications.

### 3.1 Common Interfaces for Models

LangChain provides common interfaces for chat models, embeddings, retrievers, tools, and other components. This makes application code more consistent and makes it easier to change providers.

For example, the same general pattern can be used with different chat-model integrations:

```python
response = model.invoke("What is generative AI?")
```

The provider-specific implementation remains inside the integration package.

### 3.2 Reusable Prompt Templates

Prompt templates separate instructions from changing input values.

```python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    template="Explain {topic} in simple language.",
    input_variables=["topic"],
)
```

### 3.3 Composable Workflows

LangChain components can be connected using LCEL's pipe operator:

```python
chain = prompt | model | parser
```

The output of one component becomes the input of the next component.

### 3.4 Output Parsing and Validation

LangChain provides parsers for strings, JSON, structured schemas, and Pydantic models. This helps convert model output into a format that application code can use.

### 3.5 Data Ingestion and Retrieval

LangChain provides integrations and abstractions for the RAG pipeline:

```text
Documents → Document Loader → Text Splitter → Embeddings → Vector Store → Retriever → Relevant Context + User Question → Language Model → Answer
```

### 3.6 Tools and Tool Calling

A Python function can be exposed as a tool with a name, description, and input schema:

```python
from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b
```

The model suggests a tool call. The application or agent executes the tool and sends the result back to the model.

### 3.7 Observability and Deployment Integrations

LangChain applications can be connected to LangSmith for tracing and evaluation, and LangServe can expose chains through APIs.

### Overall Problem-to-Solution Mapping

| Problem                        | LangChain capability                       |
| ------------------------------ | ------------------------------------------ |
| Provider-specific model code   | Standard model interfaces and integrations |
| Repeated prompt strings        | Prompt templates                           |
| Complex multi-step logic       | Chains, runnables, and LCEL                |
| Unreliable text output         | Output parsers and structured output       |
| Private or current information | Document loaders and retrievers            |
| Semantic search                | Embeddings and vector stores               |
| External actions               | Tools and tool calling                     |
| Difficult debugging            | LangSmith tracing and observability        |
| Exposing workflows as APIs     | LangServe and web frameworks               |

---

## 4. Why Do We Need LangChain?

We need LangChain when an application must do more than send one prompt to one model. The more an application needs data, tools, validation, memory, multiple steps, and monitoring, the more valuable an orchestration framework becomes.

### Use LangChain When You Need To:

- Build a reusable LLM application instead of a one-off experiment
- Connect an LLM to private documents or live data
- Use multiple model calls in a workflow
- Enforce a predictable output format
- Give a model access to tools or APIs
- Switch between model providers more easily
- Add retrieval, memory, or conversation history
- Trace, test, and debug LLM behavior
- Create a complete RAG or agent system

### When LangChain May Not Be Necessary

For a very small application that only makes one simple model call, the provider's SDK may be enough. LangChain becomes more valuable as the application's workflow, integrations, and reliability requirements grow.

### Key Idea

> LangChain is an orchestration layer between the application and the language model.

It helps organize the complete workflow:

```text
Application
    ↓
LangChain Components
    ├── Models
    ├── Prompts
    ├── Parsers
    ├── Runnables and Chains
    ├── Loaders and Splitters
    ├── Embeddings and Vector Stores
    ├── Retrievers
    ├── Tools
    └── Agents
    ↓
Language Models + External Data + External Actions
```

---

---

## 5. LangChain v1 Overview

LangChain v1 is the modern LangChain release focused on building dependable LLM applications and agents with clear, composable building blocks.

### What Changed in the v1 Way of Thinking?

Older LangChain examples often focused on class-based chains such as `LLMChain` and large framework abstractions. In the v1 style, we generally build workflows from smaller components:

```text
Prompt + Model + Parser + Runnable Logic
```

The pipe operator makes the data flow explicit:

```python
chain = prompt | model | parser
```

### Important v1 Ideas

- Use modern model integrations such as `ChatOpenAI`, `ChatGoogleGenerativeAI`, and `ChatGroq` from their provider packages.
- Use `langchain_core` for prompts, messages, runnables, tools, and parsers.
- Use `invoke()` for one input, `batch()` for multiple inputs, and `stream()` when partial output is useful.
- Prefer `with_structured_output()` when the selected model supports it and the application needs structured data.
- Use LangChain agents for straightforward tool-using agent applications.
- Use LangGraph when the workflow needs deeper state management, durable execution, human approval, or custom graph control.

### A Modern v1 Application Flow

```text
User Input
    ↓
Prompt / Messages
    ↓
Chat Model
    ├── Direct Answer
    ├── Structured Output
    └── Tool Call → Tool Result → Model
    ↓
Final Application Result
```

---

---

## 6. LangChain Components

![alt text](image.png)

> Note: These are learning categories, not seven completely separate packages. Some capabilities overlap. For example, embeddings, vector stores, document loaders, and retrievers together form the RAG stack, while callbacks and observability support every other component.

---

---

## 7. Models

### What Is a Model in LangChain?

A model is the component that interacts with an AI model provider. In LangChain, model objects expose common methods and can be composed with prompts, parsers, retrievers, and tools.

1. Language Models: LLMs and Chat Models
2. Embedding Models

### 7.1 Language Models: LLMs and Chat Models

#### LLMs

Traditional LLMs take a raw string prompt and return a raw string response. They are designed primarily for text completion.

```python
from langchain_openai import OpenAI

llm = OpenAI(model="gpt-3.5-turbo-instruct")
response = llm.invoke("Explain embeddings in one paragraph.")
```

#### Chat Models

Chat models take a sequence of messages rather than only a raw string. Each message has a role, such as `system`, `human`, `assistant`, or `tool`.

They are designed for conversational interactions and can support additional capabilities such as tool calling, streaming, multimodal input, and structured output, depending on the provider and model.

```python
from langchain_groq import ChatGroq

model = ChatGroq(model="openai/gpt-oss-20b")
response = model.invoke("Explain embeddings in one paragraph.")
print(response.content)
```

The response is usually an `AIMessage`, not just a plain string. It may contain content, metadata, token usage, and tool calls.

#### LLMs Versus Chat Models

| Feature      | LLM                                    | Chat Model                             |
| ------------ | -------------------------------------- | -------------------------------------- |
| Input        | Raw string                             | Sequence of messages                   |
| Output       | Usually raw string                     | Usually an `AIMessage`                 |
| Main use     | Text completion                        | Conversation and instruction following |
| Roles        | Not central                            | System, human, AI, and tool roles      |
| Modern usage | Useful for legacy or completion models | Common choice for current applications |

### 7.2 Embedding Models

Embedding models do not generate conversational answers. They convert text into numerical vectors that capture semantic meaning.

These vectors allow applications to compare text by meaning rather than only by exact words. Texts with similar meanings are represented by vectors that are close together in vector space.

```text
Text → Embedding Model → Numerical Vector
```

Embedding models are mainly used for:

- Semantic search
- RAG applications
- Similarity comparison

```python
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

query_vector = embeddings.embed_query(
    "How can I reset my password?"
)

document_vectors = embeddings.embed_documents([
    "Password reset instructions",
    "Company holiday policy",
])
```

Embedding models are used during two stages of a RAG workflow:

```text
Indexing time:
Documents → Embeddings → Vector Store

Query time:
User Question → Query Embedding → Similarity Search
```

### Common Model Methods

| Method                           | Use                               |
| -------------------------------- | --------------------------------- |
| `invoke(input)`                  | Run the model once                |
| `ainvoke(input)`                 | Run asynchronously                |
| `batch(inputs)`                  | Process multiple inputs           |
| `stream(input)`                  | Receive output progressively      |
| `bind_tools(tools)`              | Make tools available to the model |
| `with_structured_output(schema)` | Request a structured result       |
| `with_retry(...)`                | Retry failed calls                |

### Model Configuration

Common configuration options include:

- Model name
- API key or provider credentials
- Temperature
- Maximum output tokens
- Request timeout
- Retry count
- Streaming

The exact options depend on the provider and model.

### Model Selection Is a Trade-Off

There is no universally best model. Choose based on:

- Quality and reasoning capability
- Speed and latency
- Cost
- Context-window size
- Tool-calling support
- Structured-output support
- Privacy and deployment requirements
- Availability of streaming and asynchronous calls

---

---

## 8. Prompts and Messages

### What Is a Prompt?

A prompt is the instruction and context given to a model. A good prompt explains the task, supplies required information, and defines the desired response.

### Static Prompt

```python
response = model.invoke("Explain retrieval in simple language.")
```

This is useful for a one-off request, but it is not reusable.

### Prompt Template

A prompt template contains fixed instructions and placeholders for changing values:

```python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Explain {topic} for a beginner using one example."
)

formatted_prompt = prompt.invoke({"topic": "vector stores"})
```

### Chat Prompt Template

Chat prompts represent a conversation using message roles:

```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a clear and patient teacher."),
    ("human", "Explain {topic} with a practical example."),
])

chain = prompt | model
response = chain.invoke({"topic": "retrievers"})
```

### Message Roles

| Role               | Responsibility                                       |
| ------------------ | ---------------------------------------------------- |
| `system`           | Defines behavior, rules, and high-level instructions |
| `human` / `user`   | Contains the user's request or input                 |
| `assistant` / `ai` | Represents an earlier model response                 |
| `tool`             | Contains the result returned by a tool               |

### Message History

Conversation history is a list of messages. Passing previous messages gives the model context about earlier turns.

```python
messages = [
    ("system", "You are a helpful assistant."),
    ("human", "What is RAG?"),
    ("ai", "RAG means Retrieval-Augmented Generation."),
    ("human", "Why is it useful?"),
]

response = model.invoke(messages)
```

### Message Placeholder

When the history is dynamic, use a placeholder:

```python
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder("history"),
    ("human", "{question}"),
])
```

### Prompt Design Checklist

Before sending a prompt, clarify:

1. What role should the model play?
2. What task should it perform?
3. What context is trustworthy?
4. What format should it return?
5. What should it do when information is missing?
6. Which input values are dynamic?

### Prompt and Model Composition

```text
Template Input
     ↓
Formatted Messages
     ↓
Chat Model
     ↓
AIMessage
```

Use a parser after the model when the application needs a specific output type.

---

## 9. Output Parsers and Structured Output

### Why Do We Need Output Parsing?

Models generate responses probabilistically. A human can understand a natural-language answer, but software needs predictable data.

For example, an application may need:

```python
{
    "name": "Alice",
    "age": 30,
    "city": "Delhi",
}
```

Output parsers convert model responses into a format the application can use.

### 9.1 String Output Parser

`StrOutputParser` extracts a string from the model response.

```python
from langchain_core.output_parsers import StrOutputParser

chain = prompt | model | StrOutputParser()
answer = chain.invoke({"topic": "RAG"})
```

### 9.2 JSON Output Parser

`JsonOutputParser` converts a JSON response into a Python dictionary. It can also provide format instructions for the prompt.

```python
from langchain_core.output_parsers import JsonOutputParser

parser = JsonOutputParser()

prompt = PromptTemplate(
    template="Return the name and age.\n{format_instructions}",
    input_variables=[],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    },
)

chain = prompt | model | parser
result = chain.invoke({})
```

JSON parsing checks whether the response is valid JSON, but a basic JSON parser does not necessarily guarantee that every required field has the correct type or value.

### 9.3 Structured Output Parser

`StructuredOutputParser` lets us describe expected fields with `ResponseSchema` objects and generate format instructions.

It is useful when we need a predefined set of fields, but it does not provide the same level of Python-side validation as a Pydantic model.

### 9.4 Pydantic Output Parser

A Pydantic model defines the expected fields and validates the result:

```python
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

class Person(BaseModel):
    name: str
    age: int = Field(gt=0)
    city: str

parser = PydanticOutputParser(pydantic_object=Person)
chain = prompt | model | parser
person = chain.invoke({})
```

The result is a validated `Person` object rather than an unverified string.

### 9.5 Modern Structured Output

When the model integration supports it, the modern approach is often:

```python
structured_model = model.with_structured_output(Person)
result = structured_model.invoke("Alice is 30 and lives in Delhi.")
```

This is different from manually asking the model to print JSON and then parsing text. The provider integration may use native structured output or tool-calling capabilities behind the scenes.

### Parser Comparison

| Parser or method           | Result                       | Validation level                                                    |
| -------------------------- | ---------------------------- | ------------------------------------------------------------------- |
| `StrOutputParser`          | String                       | No schema validation                                                |
| `JsonOutputParser`         | Python dictionary            | JSON syntax validation                                              |
| `StructuredOutputParser`   | Dictionary with named fields | Field instructions, limited validation                              |
| `PydanticOutputParser`     | Pydantic object              | Python type and constraint validation                               |
| `with_structured_output()` | Schema-defined result        | Depends on model/provider support; usually preferred when available |

### Structured Output Best Practices

- Define clear field names and descriptions.
- Use enums or `Literal` for limited choices.
- Add Pydantic constraints where possible.
- Handle parsing failures and model refusals.
- Do not assume a schema makes the model's answer factually correct.
- Validate business rules after parsing.
- Prefer native structured output when supported by the selected model.

---

---

## 10. Chains and LCEL

### What Is a Chain?

A chain is a sequence of LangChain components connected to complete a task. The output of one component becomes the input of the next component.

```text
Input → Prompt → Model → Parser → Output
```

For example, a simple question-answering chain may contain a prompt template, a chat model, and a string output parser.

```python
from langchain_core.output_parsers import StrOutputParser

chain = prompt | model | StrOutputParser()
result = chain.invoke({"topic": "RAG"})
```

### What Is LCEL?

LCEL means LangChain Expression Language. It provides a declarative way to compose LangChain components using the pipe operator (`|`).

```python
chain = prompt | model | parser
```

This is similar to a Unix pipeline: one step passes its output to the next step.

### Why Use LCEL?

LCEL makes workflows:

- Easier to read
- Easier to compose
- Reusable
- Streamable
- Batchable
- Compatible with synchronous and asynchronous execution
- Easier to trace and inspect

### Common Chain Patterns

### 1. Simple Chain

A simple chain connects components in a straight line. Use it when one model call is enough.

```py
model = ChatGroq(model="llama-3.1-8b-instant")

prompt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}.",
    input_variables=["topic"]
)

parser = StrOutputParser()

# Simple Chain
chain = prompt | model | parser

# Invoke chain
response = chain.invoke({"topic": "space exploration"})

print(response)
```

**Graph of the chain in ASCII format**

```py
chain.get_graph().print_ascii()
```

```
     +-------------+
     | PromptInput |
     +-------------+
            *
            *
    +----------------+
    | PromptTemplate |
    +----------------+
            *
            *
      +----------+
      | ChatGroq |
      +----------+
            *
            *
   +-----------------+
   | StrOutputParser |
   +-----------------+
            *
            *
+-----------------------+
| StrOutputParserOutput |
+-----------------------+
```

### 2. Sequential Chain

A sequential chain runs multiple steps one after another. The output of one step becomes the input of the next step.

One step runs after another:

```text
Input → Chain 1 → Chain 2 → Chain 3 → Output
```

Example:

```py
model = ChatGroq(model="llama-3.1-8b-instant")

prompt1 = PromptTemplate(
    template="Generate a report on {topic}.",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a 5 short summary of the following text: {text}.",
    input_variables=["text"]
)

parser = StrOutputParser()

# Create Sequential chain
chain = prompt1 | model | parser | prompt2 | model | parser

# invoke it
response = chain.invoke({"topic": "Unemployment in India"})

print(response)

# graph in ASSIC
chain.get_graph().print_ascii()
```

```
     +-------------+
     | PromptInput |
     +-------------+
            *
            *
    +----------------+
    | PromptTemplate |
    +----------------+
            *
            *
      +----------+
      | ChatGroq |
      +----------+
            *
            *
   +-----------------+
   | StrOutputParser |
   +-----------------+
            *
            *
+-----------------------+
| StrOutputParserOutput |
+-----------------------+
            *
            *
    +----------------+
    | PromptTemplate |
    +----------------+
            *
            *
      +----------+
      | ChatGroq |
      +----------+
            *
            *
   +-----------------+
   | StrOutputParser |
   +-----------------+
            *
            *
+-----------------------+
| StrOutputParserOutput |
+-----------------------+
```

### 3. Parallel Chain

A parallel chain runs independent tasks at the same time and returns their results together. Use it when the tasks do not depend on one another.

Independent tasks run from the same input:

```text
             ┌─→ Notes ─┐
Input ───────┤          ├→ Combined Result
             └─→ Quiz ──┘
```

Example:

```py
model1 = ChatGroq(model="llama-3.1-8b-instant")

model2 = ChatGroq(model="openai/gpt-oss-20b")

prompt1 = PromptTemplate(
    template="Generate short and simple notes from following text: {text}.",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template="Generate 5 short questions and answers from the following text: {text}.",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quize into a single document \n Notes: {notes} \n Quiz: {quiz}",
    input_variables=["notes", "quiz"]
)

parser = StrOutputParser()

# Create a parallel chain to run multiple chains concurrently
Parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

marge_chain = prompt3 | model1 | parser

chain = Parallel_chain | marge_chain

# invoke it
response = chain.invoke({"text": text})

print(response)

chain.get_graph().print_ascii()
```

```
          +---------------------------+
          | Parallel<notes,quiz>Input |
          +---------------------------+
                **               **
              **                   **
            **                       **
+----------------+              +----------------+
| PromptTemplate |              | PromptTemplate |
+----------------+              +----------------+
          *                             *
          *                             *
    +----------+                  +----------+
    | ChatGroq |                  | ChatGroq |
    +----------+                  +----------+
          *                             *
          *                             *
+-----------------+            +-----------------+
| StrOutputParser |            | StrOutputParser |
+-----------------+            +-----------------+
                 **             **
                   **         **
                     **     **
          +----------------------------+
          | Parallel<notes,quiz>Output |
          +----------------------------+
                         *
                         *
                +----------------+
                | PromptTemplate |
                +----------------+
                         *
                         *
                   +----------+
                   | ChatGroq |
                   +----------+
                         *
                         *
                +-----------------+
                | StrOutputParser |
                +-----------------+
                         *
                         *
            +-----------------------+
            | StrOutputParserOutput |
            +-----------------------+
```

### 4. Conditional Chain

A conditional chain chooses one branch based on a condition or a previous result. Use it when different inputs need different workflows.

A branch is selected based on the input or a previous result:

```text
Input → Classifier → Positive Branch
                 └→ Negative Branch
```

In Conditional Chain, we can run different chains based on the output of a previous chain.

### Conditional Chain: Short Example

```python
from langchain_core.runnables import RunnableBranch

positive = PromptTemplate.from_template("Thank the customer: {feedback}") | model | parser
negative = PromptTemplate.from_template("Apologize to the customer: {feedback}") | model | parser

chain = RunnableBranch(
    (lambda x: x["sentiment"] == "positive", positive),
    negative,  # default branch
)

result = chain.invoke({
    "sentiment": "positive",
    "feedback": "I loved the product!",
})
```

The complete sentiment-classification example is available in `E_langchain_chains/4_conditional_chain.py`.

### Chain Patterns: Quick Revision

| Pattern     | Simple meaning                 | Typical use                       |
| ----------- | ------------------------------ | --------------------------------- |
| Simple      | One straight workflow          | Prompt → Model → Parser           |
| Sequential  | Steps run one after another    | Report → Summary                  |
| Parallel    | Independent steps run together | Notes and quiz from the same text |
| Conditional | Select one branch              | Positive versus negative feedback |

```text
Simple:      Input → A → B → Output
Sequential:  Input → A → B → C → Output
Parallel:    Input → A ─┐
                     B ─┴→ Output
Conditional: Input → Condition → Branch A or Branch B
```

### Chain Execution Methods

```python
chain.invoke(input)       # One input
chain.batch([input1, input2])  # Multiple inputs
chain.stream(input)       # Stream output
await chain.ainvoke(input)     # Asynchronous execution
```

---

---

## 11. Runnables

### What Is a Runnable?

A Runnable is a component that follows a common execution interface. Prompts, models, parsers, retrievers, functions, and many other LangChain objects can be used as runnables.

The common interface allows different components to be composed consistently.

```text
Runnable Input → Runnable Processing → Runnable Output
```

### Runnable Categories

#### 1. Task-Specific Runnables

These are LangChain components that perform a particular task and can participate in a pipeline.

Examples:

- Chat model: runs an LLM call
- Prompt template: formats dynamic input
- Output parser: converts model output
- Retriever: fetches relevant documents
- Tool: performs an external action

#### 2. Runnable Primitives

These are building blocks for controlling how components interact. They define whether steps run sequentially, in parallel, conditionally, or through a custom Python function.

The main primitives studied in this workspace are:

1. `RunnableSequence` — runs steps in order.
2. `RunnableParallel` — runs independent steps at the same time.
3. `RunnablePassthrough` — forwards the input unchanged.
4. `RunnableLambda` — wraps a Python function as a runnable.
5. `RunnableBranch` — implements conditional `if/else` execution.

`RunnableMap` is commonly used as another name or pattern for mapping one input into multiple runnable outputs. In modern LCEL code, this behavior is commonly expressed with `RunnableParallel`.

### Common Runnable Types

| Runnable              | Purpose                                    |
| --------------------- | ------------------------------------------ |
| `RunnableSequence`    | Execute components one after another       |
| `RunnableParallel`    | Execute independent components in parallel |
| `RunnablePassthrough` | Pass the input forward unchanged           |
| `RunnableLambda`      | Convert a Python function into a runnable  |
| `RunnableBranch`      | Select a runnable based on a condition     |

### 1. Runnable Sequence

Runs each component in order. The output of one step becomes the input of the next step.

```python
from langchain_core.runnables import RunnableSequence

chain = RunnableSequence(prompt, model, parser)
print(chain.invoke({"topic": "embeddings"}))
```

The pipe operator is commonly used as a shorter LCEL representation of a sequence.

```python
chain = prompt | model | parser
```

### 2. Runnable Parallel

Runs independent runnables together and returns their results in a dictionary.

```python
from langchain_core.runnables import RunnableParallel

parallel = RunnableParallel(
    summary=summary_chain,
    questions=question_chain,
)

result = parallel.invoke({"text": document_text})
```

The result is a dictionary containing the output of each branch.

### 3. Runnable Passthrough

`RunnablePassthrough` forwards the original input without changing it. It is useful when one input must be sent to multiple parts of a workflow.

```text
Original Input → Retriever
               └→ Prompt Input
```

```python
from langchain_core.runnables import RunnablePassthrough

chain = RunnablePassthrough()
print(chain.invoke("same input"))
```

### 4. Runnable Lambda

`RunnableLambda` wraps a normal Python function so it can participate in a chain.

```python
from langchain_core.runnables import RunnableLambda

uppercase = RunnableLambda(lambda text: text.upper())
result = uppercase.invoke("langchain")
```

It is useful for preprocessing, word counting, filtering, formatting, and post-processing.

### 5. Runnable Branch

`RunnableBranch` selects one runnable when a condition is true and another runnable otherwise.

```text
Input → Condition
          ├── True  → Runnable A
          └── False → Runnable B
```

```python
from langchain_core.runnables import RunnableBranch

branch = RunnableBranch(
    (lambda x: x > 10, RunnableLambda(lambda x: "large")),
    RunnableLambda(lambda x: "small"),  # default branch
)

print(branch.invoke(5))   # small
print(branch.invoke(20))  # large
```

### LCEL: The Shorter Runnable Syntax

`RunnableSequence` can become lengthy when many components are connected. LCEL provides the shorter pipe syntax:

```python
chain = prompt | model | parser
```

This is the most common way to create a sequential runnable workflow.

### Why Runnables Matter

Runnables create a common language for composing LangChain applications. Instead of writing custom orchestration code for every component, we connect components with a shared interface.

---

---

## 12. Document Loaders

### What Is a Document Loader?

A document loader reads data from a source and converts it into LangChain `Document` objects.

A `Document` generally contains:

```python
Document(
    page_content="The actual text",
    metadata={"source": "sample.txt"},
)
```

The `page_content` contains the text. The `metadata` contains useful information such as the source, page number, title, or URL.

### Why Do We Need Document Loaders?

Different data sources have different formats. A PDF is not read in the same way as a web page or a directory of text files.

Document loaders provide a consistent output format so that the rest of the RAG pipeline can work with the data in the same way.

```text
PDF / Text / Website / ArXiv / Wikipedia
                    ↓
             Document Loader
                    ↓
          List[Document]
```

### Common Loaders in This Workspace

| Loader            | Source                        |
| ----------------- | ----------------------------- |
| `TextLoader`      | Text files                    |
| `PyPDFLoader`     | PDF files and pages           |
| `DirectoryLoader` | Multiple files in a directory |
| `WebBaseLoader`   | Web pages                     |
| `ArxivLoader`     | ArXiv papers                  |
| `WikipediaLoader` | Wikipedia content             |

### Text Loader

```python
from langchain_community.document_loaders import TextLoader

loader = TextLoader("sample.txt", encoding="utf-8")
documents = loader.load()
```

### PDF Loader

```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("attention.pdf")
documents = loader.load()
```

`PyPDFLoader` is designed mainly for text-based PDFs. It extracts text and returns a list of LangChain `Document` objects. In the common page mode, each page may become a separate `Document` with page-related metadata.

> Important: `PyPDFLoader` is not an OCR solution. It may extract little or no useful text from scanned PDFs or pages where the content is stored as images.

#### Choosing a PDF Loader

| PDF type or requirement            | Recommended loader                                   |
| ---------------------------------- | ---------------------------------------------------- |
| Simple, clean, text-based PDF      | `PyPDFLoader`                                        |
| PDF with tables or columns         | `PDFPlumberLoader`                                   |
| Scanned or image-based PDF         | `UnstructuredPDFLoader` or `AmazonTextractPDFLoader` |
| Need layout and image-related data | `PyMuPDFLoader`                                      |
| Need richer structure extraction   | `UnstructuredPDFLoader`                              |

The correct choice depends on the document layout, OCR needs, table quality, metadata requirements, and deployment environment. Always inspect the extracted text before sending it to a splitter or embedding model.

#### PyPDFLoader Example

```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("attention.pdf")
documents = loader.load()

print(f"Pages loaded: {len(documents)}")
print(documents[0].page_content[:500])
print(documents[0].metadata)
```

#### PDF Ingestion Checklist

1. Identify whether the PDF contains real text or scanned images.
2. Select a loader that matches the layout and extraction requirement.
3. Inspect a few pages and their metadata.
4. Check tables, columns, headers, footers, and page numbers.
5. Use OCR when the PDF contains images of text.
6. Split the extracted documents only after verifying the content.

### Web Loader

```python
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://example.com/article")
documents = loader.load()
```

Web loaders may require HTML parsing and filtering so that navigation menus and unrelated page content are not included.

#### Filtered WebBaseLoader Example

```python
from langchain_community.document_loaders import WebBaseLoader
import bs4

loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent",),
    bs_kwargs={
        "parse_only": bs4.SoupStrainer(
            class_=("post-title", "post-content", "post-header")
        )
    },
)

documents = loader.load()
print(documents[0].page_content[:500])
```

`SoupStrainer` limits extraction to the important article sections. This can reduce navigation text, advertisements, and unrelated HTML from entering the RAG pipeline.

### ArXiv Loader

`ArxivLoader` loads research papers from ArXiv using a paper identifier or search query.

```python
from langchain_community.document_loaders import ArxivLoader

documents = ArxivLoader(
    query="1706.03762",  # Attention Is All You Need
    load_max_docs=1,
).load()

print(documents[0].page_content[:500])
print(documents[0].metadata)
```

Use the paper identifier when you need a specific paper. For larger ingestion jobs, handle rate limits, retries, duplicate papers, and metadata carefully.

### Wikipedia Loader

`WikipediaLoader` retrieves Wikipedia pages for a search query.

```python
from langchain_community.document_loaders import WikipediaLoader

documents = WikipediaLoader(
    query="Artificial Intelligence",
    load_max_docs=2,
).load()

for document in documents:
    print(document.metadata.get("title"))
    print(document.page_content[:300])
```

Wikipedia is useful for demonstrations, exploratory research, and general reference information. For production knowledge bases, prefer authoritative sources that you control and can update reliably.

### CSV and Structured-Data Loaders

For tabular data, use a loader that preserves row and column information, such as `CSVLoader`.

```python
from langchain_community.document_loaders import CSVLoader

documents = CSVLoader("employees.csv").load()
print(documents[0].page_content)
print(documents[0].metadata)
```

For production systems, decide whether rows should become individual documents and which columns should be searchable text versus metadata.

### Commonly Used Production Loader Categories

There is no universal ranking of “most used” loaders. Production teams choose based on their data sources and extraction requirements. The following categories are common:

| Data source              | Common loader choices                                                    | Typical use                            |
| ------------------------ | ------------------------------------------------------------------------ | -------------------------------------- |
| Plain text and Markdown  | `TextLoader`, Markdown loaders                                           | Notes, documentation, source files     |
| PDF documents            | `PyPDFLoader`, `PyMuPDFLoader`, `PDFPlumberLoader`, Unstructured loaders | Manuals, policies, research papers     |
| Word documents           | `Docx2txtLoader`, Unstructured loaders                                   | Reports, contracts, internal documents |
| CSV and spreadsheets     | `CSVLoader`, dataframe loaders                                           | Records, catalogues, tabular knowledge |
| Websites                 | `WebBaseLoader`, sitemap/web-crawling loaders                            | Documentation and public knowledge     |
| Cloud storage            | S3, Azure Blob, Google Cloud Storage loaders                             | Enterprise document repositories       |
| Databases                | SQL and database loaders                                                 | Structured business data               |
| SaaS and knowledge bases | Confluence, Notion, SharePoint, GitHub loaders                           | Internal company knowledge             |
| Research sources         | `ArxivLoader`, `WikipediaLoader`                                         | Research and educational applications  |
| Scanned documents        | Unstructured, Textract, OCR-based loaders                                | Invoices, scans, image PDFs            |

### Production Loader Selection Checklist

- Does the loader preserve useful metadata?
- Can it handle the document size and ingestion volume?
- Does it support incremental updates?
- Can it retry temporary failures?
- Does it preserve page, section, row, or source identity?
- Can it handle tables, images, and scanned text?
- Are credentials and private data handled securely?
- Can the extracted content be inspected and evaluated?

### Loader Workflow

```python
documents = loader.load()

print(len(documents))
print(documents[0].page_content)
print(documents[0].metadata)
```

---

## 13. Text Splitters

### Why Split Documents?

Large documents are usually too long to send to a model or embed as one unit. Text splitters divide documents into smaller chunks.

```text
Large Document → Smaller Chunks → Embeddings → Vector Store
```

Good chunks should contain meaningful information and enough surrounding context to be useful during retrieval.

### Important Splitting Terms

- `chunk_size`: Maximum size of a chunk.
- `chunk_overlap`: Number of characters or tokens repeated between neighboring chunks.
- `separator`: The boundary used to divide text.
- `Metadata:` Source information carried along with the chunk.

### 1. Recursive Character Text Splitter

`RecursiveCharacterTextSplitter` is the recommended general-purpose splitter for ordinary text. It tries separators in order and keeps larger meaningful units together whenever possible.

The default separator order is approximately:

```python
["\n\n", "\n", " ", ""]
```

This means it first tries to keep paragraphs together, then lines, then words. The final empty separator allows it to split individual characters when necessary.

```text
Paragraph → Line → Word → Character
```

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
)

chunks = splitter.split_documents(documents)
```

Here, `chunk_size=500` aims for chunks of up to about 500 characters, and `chunk_overlap=50` repeats some content between neighboring chunks.

#### How It Splits

- **Split method:** Tries a list of separators recursively.
- **Chunk-size measurement:** Characters by default.
- **Best for:** Generic prose, articles, notes, and ordinary documents.

#### Limitations

- Character count is not the same as token count, so a chunk may still be too large for a model's token limit.
- It does not truly understand the meaning of the text; it uses separators and size rules.
- Important tables, headings, lists, and code blocks may be split poorly.
- The same fixed chunk size may not work for every document type.
- Too-small chunks can lose context, while too-large chunks can reduce retrieval precision.
- A very large string without useful separators may still be split awkwardly.
- It can create duplicate context and extra storage when overlap is too large.

For production systems, inspect sample chunks and evaluate retrieval quality instead of choosing `chunk_size` and `chunk_overlap` blindly.

### 2. Character Text Splitter

`CharacterTextSplitter` is the simplest splitter. It uses one separator and measures chunk size by characters.

```python
from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(
    separator="\n\n",  # split at paragraph boundaries
    chunk_size=500,
    chunk_overlap=50,
)

chunks = splitter.split_documents(documents)
```

#### How It Splits

- **Split method:** One fixed separator, such as `"\n\n"`.
- **Chunk-size measurement:** Characters by default.
- **Best for:** Simple text with a predictable structure.

#### Limitations

- It does not recursively try other separators when the chosen separator is unsuitable.
- Chunks may exceed the desired size if one separated section is very large.
- It may break useful context when the separator does not match the document structure.
- It is less flexible than `RecursiveCharacterTextSplitter` for mixed or irregular text.

Use it when you know the document has a reliable separator. Otherwise, start with the recursive splitter.

### 3. HTML Header Text Splitter

`HTMLHeaderTextSplitter` is a structure-aware splitter. It splits content at HTML headers and adds header information to the metadata of each chunk.

It can keep content grouped by sections and preserve context such as the page's `h1`, `h2`, and `h3` hierarchy.

#### Short Example: HTML String

```python
from langchain_text_splitters import HTMLHeaderTextSplitter

html = """
<h1>LangChain</h1>
<p>LangChain helps build LLM applications.</p>
<h2>RAG</h2>
<p>RAG retrieves relevant context before generation.</p>
"""

headers = [("h1", "Header 1"), ("h2", "Header 2")]
splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers)

chunks = splitter.split_text(html)
```

#### Short Example: Web Page

```python
url = "https://plato.stanford.edu/entries/goedel/"
headers = [("h1", "Header 1"), ("h2", "Header 2"), ("h3", "Header 3")]

splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers)
chunks = splitter.split_text_from_url(url)
```

#### Important Points

- It preserves useful heading context through metadata.
- It can be combined with another splitter when sections are still too large.
- It depends on meaningful HTML heading structure.
- Poorly structured HTML may produce poor chunks.
- Web pages may contain navigation, advertisements, and unrelated elements unless cleaned before splitting.

### 4. Recursive JSON Splitter

`RecursiveJsonSplitter` is designed for nested JSON data. It traverses the JSON structure and tries to keep nested objects together while creating chunks below the configured maximum size.

```python
import requests
from langchain_text_splitters import RecursiveJsonSplitter

data = requests.get("https://api.smith.langchain.com/openapi.json").json()
splitter = RecursiveJsonSplitter(max_chunk_size=300)

chunks = splitter.split_json(data)
documents = splitter.create_documents([data])
```

#### How It Splits

- **Split method:** JSON keys and values while traversing the structure.
- **Chunk-size measurement:** Characters by default.
- **Best for:** OpenAPI schemas, API responses, configuration, and nested JSON.

#### Important Points and Limitations

- It tries to keep nested JSON objects whole whenever the size allows it.
- It may split nested objects when needed to meet `max_chunk_size`.
- A very large non-nested string value is not necessarily split internally.
- It is not a semantic text splitter; it follows JSON structure.
- It may produce less useful chunks when the JSON keys have little meaning without additional context.
- For a hard size limit on large string values, compose it with a recursive text splitter afterward.
- Lists can optionally be preprocessed into JSON objects before splitting.

Example of applying a text splitter after JSON splitting:

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

json_text_chunks = splitter.split_text(data)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
final_chunks = text_splitter.create_documents(json_text_chunks)
```

### Other Structure-Aware Splitters

- `HTMLHeaderTextSplitter` preserves HTML heading context.
- `RecursiveJsonSplitter` divides nested JSON while trying to preserve meaningful structure.
- Other specialized splitters can work with programming languages, Markdown, and token limits.

### Why Use Chunk Overlap?

Important information may appear at the boundary between two chunks. Overlap repeats a small portion so that context is not lost.

```text
Chunk 1: [A B C D E]
Chunk 2:         [D E F G H]
                  ↑ overlap
```

Too much overlap increases storage and retrieval cost, so it should be chosen based on the document and task.

### Choosing Chunk Size

There is no universal best chunk size. Consider:

- Document structure
- Model context window
- Embedding model behavior
- Question complexity
- Desired retrieval precision
- Cost and latency

Small chunks may improve precision but lose context. Large chunks preserve context but may include irrelevant information.

### Text-Splitting Workflow

```text
Loaded Documents
      ↓
Choose Splitter
      ↓
Set Chunk Size and Overlap
      ↓
Create Document Chunks
      ↓
Inspect Content and Metadata
      ↓
Embed and Index
```

---

---

## 14. Embeddings

### What Are Embeddings?

An embedding model converts text into a fixed-length list of numbers called a vector. The vector represents the semantic meaning of the text.

```text
Text → Embedding Model → Vector of Numbers
```

Texts with similar meaning should have vectors that are close to each other. This allows applications to search by meaning instead of only matching exact words.

### Example

```python
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

query_vector = embeddings.embed_query("What is RAG?")

document_vectors = embeddings.embed_documents([
    "RAG retrieves context before generating an answer.",
    "A vector store indexes numerical representations of text.",
])
```

### Main Methods

| Method                   | Purpose                         |
| ------------------------ | ------------------------------- |
| `embed_query(text)`      | Embed one user query            |
| `embed_documents(texts)` | Embed a list of document chunks |

### Embeddings in RAG

```text
Indexing time:
Document Chunks → Document Embeddings → Vector Store

Query time:
User Query → Query Embedding → Similarity Search
```

The document and query embeddings should normally come from compatible embedding models. The embedding model is not the same as a chat model: it represents text numerically but does not generate an answer.

### Similarity Metrics

Common ways to compare vectors include `cosine similarity`, `Euclidean distance`, and `dot product`. The vector store usually handles this comparison.

### Important Considerations

- Higher dimensionality does not automatically mean better retrieval.
- Embedding quality depends on the model, language, domain, and chunk quality.
- Changing the embedding model usually requires re-embedding the documents.
- Store the embedding-model name with an index so the index can be reproduced correctly.
- Remove or protect sensitive data before sending it to an external embedding provider.

---

---

## 15. Vector Stores

### What Is a Vector Store?

A vector store stores **document chunks**, their **embeddings**, and **metadata**. It provides efficient similarity search for a user query.

```text
Document Chunk + Embedding + Metadata → Vector Store

User Query → Similarity Search → Relevant Documents
```

### Creating a Vector Store

```python
from langchain_community.vectorstores import FAISS

vector_store = FAISS.from_documents(
    documents=chunks,
    embedding=embeddings,
)
```

### Similarity Search

```python
results = vector_store.similarity_search(
    "What is retrieval augmented generation?",
    k=4,
)

for document in results:
    print(document.page_content)
```

`k` controls how many documents are returned. A larger `k` gives more context but may also add irrelevant information and increase model cost.

### FAISS and Chroma

| Vector store             | Useful for                                                   |
| ------------------------ | ------------------------------------------------------------ |
| FAISS                    | Fast local similarity search and experiments                 |
| Chroma                   | Local persistence, metadata, and development workflows       |
| Managed vector databases | Production scale, availability, filtering, and shared access |

### Vector Store vs Vector Database

These terms are sometimes used interchangeably, but there is a useful practical distinction.

#### Vector Store

A vector store is usually a library or service focused mainly on storing embeddings and performing similarity search.

Typical characteristics:

- Lightweight and easy to use
- Useful for experiments and smaller applications
- May provide basic metadata filtering
- May require the application to manage persistence, backups, scaling, and security
- May not provide rich transactions, distributed clustering, or a full database query system

**FAISS** is a good example. It provides fast local vector indexing and similarity search, while persistence and production infrastructure are handled separately by the application.

#### Vector Database

A vector database is a full database system designed to store and query vectors together with metadata.

It may provide:

- Distributed architecture and horizontal scaling
- Durable persistence and replication
- Backup and restore
- Metadata schemas and filters
- Authentication and authorization
- Monitoring and operational tooling
- High availability and access controls
- Transactional or near-transactional guarantees, depending on the product

Examples include **Milvus, Qdrant, and Weaviate**

#### Which One Should We Choose?

```text
Learning / prototype / local experiment → FAISS or Chroma

Production / large dataset / multiple users → Vector Database
```

The exact choice depends on dataset size, query volume, latency requirements, update frequency, filtering needs, security, availability, and operational budget.

> A vector database can be viewed as a vector store with additional database capabilities such as durability, clustering, scaling, security, and advanced metadata management.

### Metadata Filtering

Metadata can store source, page number, document type, tenant, date, or permissions. Filtering prevents retrieval from returning documents outside the allowed scope.

### Important Considerations

- The index is only as good as the chunks and embeddings inserted into it.
- Keep the original source and metadata with every chunk.
- Plan how documents will be updated or deleted.
- Use access-control filters for private or multi-tenant data.
- Evaluate retrieval quality separately from answer quality.

---

---

## 16. Retrievers

### What Is a Retriever?

A retriever accepts a query and returns the most relevant `Document` objects. It is the search component of a RAG application.

`or`

A retriever is a component in LangChain that fetches relevant documents from a
data source in response to a user’s query.

- There are multiple types of retrievers
- All retrievers in LangChain are runnables

```
Data Source <------- Retriever ----------> Documents
                        |
                        |
                        |
                      Query
```

```python
retriever = vector_store.as_retriever(
    search_kwargs={"k": 4}
)

documents = retriever.invoke("What is RAG?")
```

### Retriever Types

### 1. Basic Retriever

Returns documents that are most similar to the query.

```python
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3},
)
documents = retriever.invoke("What is RAG?")
```

Use this when a simple top-`k` similarity search is sufficient.

### 2. Wikipedia Retriever

Searches Wikipedia and returns relevant documents for general-knowledge questions.

```python
from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(load_max_docs=2)
documents = retriever.invoke("Artificial Intelligence")
```

### 3. Vector-Store Retriever

Uses an existing FAISS, Chroma, or other vector store as the retrieval backend.

```python
retriever = vector_store.as_retriever(search_kwargs={"k": 4})
documents = retriever.invoke("Explain embeddings")
```

This is the most common retriever pattern in a basic RAG pipeline.

### 4. Maximal Marginal Relevance (MMR)

MMR is an information-retrieval algorithm designed to reduce redundancy while maintaining high relevance to the query.

- Regular similarity search may return documents that are all very similar, repeat the same information, or lack diverse perspectives.

- MMR selects the most relevant document first, then selects documents that are relevant but less similar to the documents already selected.

```text
Most relevant document → Relevant but different document → Another diverse result
```

MMR is especially useful in RAG when the context window should contain diverse but still relevant information.

```python
retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 4, "fetch_k": 10},
)
```

`fetch_k` creates a larger candidate set. MMR then chooses a diverse subset of `k` documents.

### 5. Multi-Query Retriever

Uses a model to generate multiple versions of the user's question, retrieves results for each version, and combines them. This helps when one wording does not match the wording in the documents.

#### Why Use Multi-Query Retrieval?

A single query may not capture all the ways an idea is expressed in the documents.

```text
Original query → Different query versions → Retrieve each → Combine and deduplicate
```

The steps are:

1. Take the original query.
2. Ask an LLM to generate semantically different versions.
3. Retrieve documents for each version.
4. Combine and deduplicate the results.

This can improve recall, but it adds model calls, latency, and cost.

```python
from langchain.retrievers.multi_query import MultiQueryRetriever

retriever = MultiQueryRetriever.from_llm(
    retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
    llm=model,
)
documents = retriever.invoke("How does RAG improve answers?")
```

It can improve recall, but it adds model calls and latency.

### 6. Contextual Compression Retriever

First retrieves documents and then compresses them to keep only the parts relevant to the query. This can reduce unnecessary context sent to the model.

#### Why Use Contextual Compression?

A normal retriever may return an entire paragraph even when only one sentence answers the question.

```text
Base Retriever → Complete documents → Compressor → Relevant passages only
```

How it works:

1. A base retriever fetches documents.
2. A compressor examines each document.
3. Only query-relevant content is kept.
4. Irrelevant content is discarded.

Use it for long documents or mixed-content chunks. The trade-off is an additional processing step, cost, and latency.

```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

base = vector_store.as_retriever(search_kwargs={"k": 4})
compressor = LLMChainExtractor.from_llm(model)

retriever = ContextualCompressionRetriever(
    base_retriever=base,
    base_compressor=compressor,
)
documents = retriever.invoke("What is photosynthesis?")
```

Compression can reduce irrelevant context, but adds another model step, cost, and latency.

### Other Important Retriever Types

| Retriever                     | Simple explanation                                                         | Useful when                                                   |
| ----------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------- |
| `BM25Retriever`               | Keyword-based lexical search                                               | Exact words, IDs, and acronyms matter                         |
| `ParentDocumentRetriever`     | Searches small child chunks but returns larger parent documents            | Search precision and full context are both needed             |
| `TimeWeightedVectorRetriever` | Combines semantic similarity with recency                                  | Recent information should be preferred                        |
| `SelfQueryRetriever`          | Converts a natural-language query into a search query and metadata filters | Users ask about dates, categories, or authors                 |
| `MultiVectorRetriever`        | Uses multiple vectors or representations for one document                  | Documents have summaries, chunks, or multiple representations |
| `EnsembleRetriever`           | Combines multiple retrievers                                               | Both keyword and semantic search are important                |
| `ArxivRetriever`              | Retrieves research papers from ArXiv                                       | Research-paper search is required                             |

#### Keyword Search Versus Semantic Search

```text
BM25 / keyword search → matches exact words and terms
Vector search         → matches meaning and semantics
Ensemble retrieval    → combines both strengths
```

For example, vector search may understand that “vehicle” and “car” are related, while BM25 may be better at finding an exact identifier such as `SKU-123`.

### Retriever Selection Guide

| Retriever              | Use when                                             |
| ---------------------- | ---------------------------------------------------- |
| Basic similarity       | You need a simple top-`k` search                     |
| Wikipedia              | You need general Wikipedia knowledge                 |
| Vector-store           | You are searching your own embedded documents        |
| MMR                    | Results contain too many near-duplicates             |
| Multi-query            | Different phrasings may retrieve different documents |
| Contextual compression | Retrieved chunks contain too much irrelevant text    |

### Retriever Quality Factors

- Chunk size and overlap
- Embedding model
- Search type
- Number of results (`k`)
- Metadata filters
- Query wording
- Reranking or compression
- Quality and freshness of the source data

### Retriever Versus Vector Store

```text
Vector Store = stores and searches vectors

Retriever    = application-facing interface that returns relevant documents
```

A vector store can become a retriever through `as_retriever()`, but retrievers can also use other search systems such as Wikipedia or databases.

---

---

## 17. Retrieval-Augmented Generation (RAG)

### What Is RAG?

Retrieval-Augmented Generation is a pattern in which an application retrieves relevant external information and provides it to the language model before generating an answer.

```text
User Question
      ↓
Retriever
      ↓
Relevant Documents
      ↓
Prompt with Context
      ↓
Language Model
      ↓
Answer
```

### Why Use RAG?

RAG helps an application answer questions using:

- Private company documents
- Current information
- Large document collections
- Domain-specific knowledge
- Sources that can be cited or inspected

RAG does not retrain the model. It supplies useful context at query time.

### Complete RAG Flow

RAG has two connected phases:

1. **Indexing:** Prepare the external knowledge base before users ask questions.
2. **Query-time RAG:** Retrieve useful information and generate an answer when a user asks a question.

```text
                INDEXING PHASE
Documents → Load → Split → Embed → Store in Vector Database
                                           │
                                           ▼
                QUERY-TIME PHASE
User Query → Query Embedding → Retrieve Relevant Chunks
                                      │
                                      ▼
                       Context + User Query
                                      │
                                      ▼
                                  Prompt
                                      │
                                      ▼
                                     LLM
                                      │
                                      ▼
                                  Response
```

### Phase 1: Indexing

Indexing is the process of preparing a knowledge base so it can be searched efficiently at query time.

#### Step 1: Document Ingestion

Load source knowledge into LangChain `Document` objects.

Examples include PDFs, Word documents, YouTube transcripts, web pages, GitHub repositories, internal wikis, SQL records, and scraped webpages.

```text
Source Data → Document Loader → Documents with content and metadata
```

#### Step 2: Text Chunking

Break large documents into small, meaningful chunks. Large documents may exceed the model context window, and smaller focused chunks usually improve semantic retrieval.

```text
Documents → Text Splitter → Document Chunks
```

Common tools include `RecursiveCharacterTextSplitter`, `MarkdownHeaderTextSplitter`, and structure-aware splitters.

#### Step 3: Embedding Generation

Convert every chunk into a dense numerical vector that captures its meaning.

```text
Document Chunk → Embedding Model → Vector
```

The same or compatible embedding model should be used for both document chunks and user queries.

#### Step 4: Store Vectors and Metadata

Store each vector together with its original chunk text and metadata in a vector store or vector database.

```text
Vector + Original Text + Metadata → Vector Store / Vector Database
```

Local options include FAISS and Chroma. Production options may include managed or distributed vector databases.

### Phase 2: Query-Time RAG

#### Step 1: Receive the Query

The user asks a question in natural language.

#### Step 2: Embed the Query

The query is converted into a vector using the embedding model.

```text
User Query → Query Embedding Vector
```

#### Step 3: Retrieve Relevant Chunks

The retriever searches the vector store and returns the most relevant chunks. It may use similarity search, MMR, multi-query retrieval, metadata filters, or compression.

#### Step 4: Augment the Prompt

The retrieved chunks are combined with the user's question to create an enriched prompt.

```text
Retrieved Context + User Question → Augmented Prompt
```

Example prompt:

```text
You are a helpful assistant.
Answer the question only from the provided context.
If the context is insufficient, say you do not know.

Context:
{context}

Question:
{question}
```

#### Step 5: Generate the Answer

The LLM receives the augmented prompt and generates the final response using the user's question and retrieved context.

```text
Augmented Prompt → LLM → Grounded Response
```

### Why RAG Is Useful

RAG allows an application to work with:

- Private data
- Recent developments and updated documents
- Large external knowledge bases
- Domain-specific information

It can also reduce unsupported answers when the prompt instructs the model to rely only on retrieved context. However, retrieval quality must be evaluated because poor chunks or irrelevant results can still lead to hallucinations.

### RAG Indexing Pipeline

Indexing usually happens before the user asks a question:

```text
Load Documents
      ↓
Split Documents
      ↓
Create Embeddings
      ↓
Store Vectors and Metadata
```

### RAG Query Pipeline

```text
User Question
      ↓
Create Query Embedding
      ↓
Retrieve Relevant Chunks
      ↓
Build Prompt with Context
      ↓
Generate Answer
```

### Simple Retrieval Chain

```python
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    "Answer using only this context:\n{context}\n\nQuestion: {input}"
)

document_chain = create_stuff_documents_chain(model, prompt)
retrieval_chain = create_retrieval_chain(retriever, document_chain)

response = retrieval_chain.invoke({"input": "What is RAG?"})
print(response["answer"])
```

### Common RAG Problems

- Poor chunking produces incomplete context.
- Poor embeddings return irrelevant documents.
- A small `k` may miss important information.
- A large `k` may overwhelm the model with noise.
- Similar documents may be repeated without diversity methods such as MMR.
- Stale indexes may return outdated information.
- The model may still hallucinate when the retrieved context is insufficient.

### RAG Best Practices

1. Preserve source and page metadata.
2. Test chunk sizes and overlap with real questions.
3. Inspect retrieved documents before debugging the model prompt.
4. Use metadata filtering for permissions and domains.
5. Tell the model to say when the context does not contain an answer.
6. Evaluate retrieval and generation as separate stages.
7. Return citations or source information when trust is important.

---

## 18. Memory and Conversation History

An LLM is stateless by default. Memory means that the application stores useful previous information and sends it again when needed.

```text
Previous Messages → Application Memory → New Prompt → Model
```

```python
messages = [
    ("system", "You are helpful."),
    ("human", "My name is Ravi."),
    ("ai", "Nice to meet you, Ravi."),
    ("human", "What is my name?"),
]
response = model.invoke(messages)
```

### Short Memory Example

```python
from langchain_core.messages import HumanMessage, AIMessage

history = [
    HumanMessage(content="My favorite language is Python."),
    AIMessage(content="I will remember that for this conversation."),
]

response = model.invoke(history + [
    HumanMessage(content="What is my favorite language?")
])

print(response.content)
```

The application sends the previous messages again; the model does not remember them independently.

For dynamic history, use `MessagesPlaceholder` in a `ChatPromptTemplate`. Memory can be short-term history, summarized history, long-term user data, or retrieved memories. Limit its size, isolate sessions, protect sensitive information, and allow deletion where appropriate.

---

## 19. Tools

A tool is a Python function or external capability packaged so a model or agent can understand and call it.

LLMs are good at reasoning and language generation, but they cannot automatically access live data, perform reliable calculations, call APIs, run code, or interact with databases. Tools connect these capabilities to the model.

```text
Model decides → Tool executes → Result returns to model
```

### 1. Built-In Tools

Provided by LangChain or an integration package.

```python
from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()
result = search.invoke("What is the capital of France?")
```

Other examples include Wikipedia, shell, Python, HTTP, and database tools. Review permissions before exposing powerful tools.

### 2. Custom Tools

Custom tools wrap application logic, APIs, calculations, or database operations.

```python
from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b
```

The name, docstring, type hints, and parameters describe the tool to the model.

### 3. Structured Tools

Structured tools use an explicit schema for complex inputs, often with Pydantic.

```python
from pydantic import BaseModel
from langchain_core.tools import StructuredTool

class MultiplyInput(BaseModel):
    a: int
    b: int

tool = StructuredTool.from_function(
    func=lambda a, b: a * b,
    name="multiply",
    description="Multiply two numbers",
    args_schema=MultiplyInput,
)
```

### 4. Toolkits

A toolkit is a group of related tools packaged for a common purpose, such as database, search, GitHub, or file-management tools.

```python
class MathToolkit:
    def get_tools(self):
        return [add, multiply]
```

Good tools have clear descriptions, typed inputs, validation, safe error handling, limited permissions, and concise results.

### Ways to Create a Tool

1. `@tool` decorator — the simplest approach for a typed Python function.
2. `StructuredTool` — useful when an explicit Pydantic input schema is required.
3. `BaseTool` — lower-level custom implementation for advanced behavior.

`BaseTool` is the abstract base class behind common tool abstractions. It defines the structure and interface that a custom tool follows.

### Tools in the Agent Ecosystem

An agent is an LLM-powered system that can decide, use external tools, observe results, and continue toward a goal.

```text
User Goal → Agent Model → Tool → Observation → Agent Model → Final Answer
```

### Common Built-In Tool Examples

| Tool                     | Purpose                                  |
| ------------------------ | ---------------------------------------- |
| `DuckDuckGoSearchRun`    | Web search                               |
| `WikipediaQueryRun`      | Wikipedia lookup                         |
| `PythonREPLTool`         | Run Python code                          |
| `ShellTool`              | Run shell commands                       |
| HTTP request tools       | Call web APIs                            |
| Database query tools     | Query structured data                    |
| Email or messaging tools | Send messages through connected services |

### Custom Tools: When to Use Them

Create a custom tool when the model needs to interact with your own API, business logic, database, product, or application.

Workspace examples: `K_ Tools_in_LangChain/1_tools-in-langchain.ipynb` and `tool.md`.

---

## 20. Tool Calling

Tool calling is when a model returns a structured request containing a tool name and arguments. The application or agent runtime executes the actual function.

```text
User Request → Model Tool Call → Application Executes Tool
             → Tool Result → Model → Final Answer
```

### Define, Bind, and Execute

```python
@tool
def multiply(a: int, b: int) -> int:
    """Return the product of two numbers."""
    return a * b

model_with_tools = model.bind_tools([multiply])
message = model_with_tools.invoke("What is 3 multiplied by 4?")

tool_call = message.tool_calls[0]
result = multiply.invoke(tool_call["args"])
```

Binding registers the tool's name, description, and input schema. The model suggests the call; the application executes it. In a complete loop, the result is sent back to the model for the final response.

### What Does Tool Binding Provide?

Tool binding tells the model:

1. Which tools are available.
2. What each tool does through its description.
3. Which input format and arguments the tool expects through its schema.

```text
Tool Binding = Tool Name + Description + Input Schema
```

### Tool Calling Versus Tool Execution

| Concept        | Responsibility                      |
| -------------- | ----------------------------------- |
| Tool binding   | Register tools with the model       |
| Tool calling   | Model suggests a tool and arguments |
| Tool execution | Application runs the function       |
| Final response | Model explains the result           |

### Tool Execution

Tool execution is the step where the actual Python function or external API runs using the arguments suggested by the model.

```text
Model says: "Call multiply with a=8 and b=7."
Application runs: multiply(a=8, b=7)
Result: 56
```

The model suggests the action; LangChain or the application performs the action.

The currency-conversion notebook demonstrates a multi-step call where one tool obtains an exchange rate and another performs the calculation.

### Safety

- Validate model-provided arguments.
- Restrict shell, filesystem, database, and network permissions.
- Add timeouts and error handling.
- Require approval for sensitive actions.
- Log tool calls and results.
- Never expose secrets in tool descriptions or results.

---

## 21. Agents

An agent is an LLM-powered application that decides which actions to take, uses tools, observes results, and continues until it can complete a task.

```text
User Goal → Model Decides → Tool Call → Tool Result → Model Decides Again → Answer
```

An ordinary chain follows a predefined sequence. An agent chooses its next step dynamically.

| Chain                    | Agent                             |
| ------------------------ | --------------------------------- |
| Predetermined steps      | Dynamic steps                     |
| More predictable         | More flexible                     |
| Easier to test           | Requires stronger safety controls |
| Good for fixed workflows | Good for tool-using tasks         |

Agent components include a model, instructions, tools, memory/state, an execution loop, and a stop condition. Use an agent when the next action depends on the model's interpretation; use a chain when the steps are known in advance.

---

## 22. Callbacks and Observability

Callbacks are hooks that run when events occur inside a LangChain workflow, such as model calls, chain steps, retrieval, tool calls, errors, and streaming.

```text
Workflow Event → Callback → Log / Trace / Metric / Action
```

Observability helps inspect prompts, model responses, retrieved documents, tool calls, token usage, latency, retries, and errors. Add session and request metadata, but avoid logging secrets or unnecessary personal data.

---

## 23. LangSmith

LangSmith is used to trace, debug, evaluate, and monitor LangChain and other LLM applications.

### Main Capabilities

- **Tracing:** View the complete execution tree.
- **Debugging:** Inspect prompts, retrieval, tools, outputs, and errors.
- **Datasets:** Store representative inputs and expected results.
- **Evaluation:** Compare application versions.
- **Monitoring:** Track production quality, latency, failures, and usage.

```python
import os

os.environ["LANGSMITH_API_KEY"] = "your-api-key"
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_PROJECT"] = "my-project"
```

### Evaluation Types

- Unit tests for individual components
- Offline evaluation on curated datasets
- Regression tests after model or prompt changes
- Backtesting against historical examples
- Online monitoring and anomaly detection
- LLM-as-a-judge evaluation
- Deterministic code-based evaluation

---

## 24. LangServe and Deployment

Deployment makes a LangChain workflow available through an API, application, background job, or hosted service.

```text
LangChain Workflow → API / App Server → Client
```

LangServe can expose LCEL chains and runnables as API endpoints:

```python
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(title="LangChain API")
add_routes(app, chain, path="/chain")
```

Common options include Streamlit for learning UIs, FastAPI for custom APIs, LangServe for serving chains, containers for reproducibility, and LangGraph/LangSmith deployment for stateful agent workflows.

### Deployment Checklist

- Store keys in environment variables or a secrets manager.
- Add authentication, validation, timeouts, retries, and rate limits.
- Restrict dangerous tools.
- Monitor latency, cost, errors, and quality.
- Pin dependencies and test upgrades.

The `1.1_openai`, `1.2 Ollama`, and `1.3_groq` examples contain application and serving patterns.

---

## 25. Testing, Evaluation, and Production Best Practices

LLM output can vary even when code does not change. Test both software correctness and response quality.

### Testing Layers

1. **Unit tests:** Test schemas, formatting, routing, metadata filters, and tools.
2. **Integration tests:** Test loaders, splitters, embeddings, vector stores, retrievers, models, and tools together.
3. **Evaluation tests:** Test correctness, relevance, groundedness, format, safety, latency, and cost.
4. **Regression tests:** Compare a new model, prompt, retriever, or chain with a known baseline.

```python
result = chain.invoke({"topic": "RAG"})
assert isinstance(result, str)
assert len(result) > 0
```

### Production Best Practices

- Version prompts and schemas.
- Validate tool arguments and model outputs.
- Preserve source metadata for citations.
- Use permission filters for private data.
- Add timeouts, retries, fallbacks, and rate limits.
- Track token usage, cost, latency, and errors.
- Protect personal data, API keys, and system prompts.
- Require human approval for high-impact actions.
- Use traces and user feedback to improve evaluation datasets.

### RAG Debugging Order

```text
Source quality → Chunk quality → Embedding quality
      → Retrieval quality → Prompt grounding → Answer quality
```

Debug retrieval before assuming the model itself is the problem.

---

---

## 26. Interview Questions and Final Cheat Sheet

### Quick Interview Answers

**What is LangChain?** An orchestration framework for building LLM applications with models, prompts, parsers, workflows, retrieval, tools, and agents.

**What is LCEL?** LangChain Expression Language, commonly used to compose components with the pipe operator.

**What is a Runnable?** A component with a common execution interface that can be composed with other components.

**What is RAG?** Retrieval-Augmented Generation retrieves external context and provides it to a model before generation.

**What is an embedding?** A numerical vector representation of text meaning used for similarity search.

**What is a retriever?** A component that accepts a query and returns relevant `Document` objects.

**What is MMR?** An algorithm that balances relevance and diversity to reduce duplicate retrieval results.

**What is tool calling?** The model returns a structured request for a tool; the application executes it and returns the result.

**What is an agent?** An LLM-powered system that dynamically chooses actions and tools to complete a task.

**Why use LangSmith?** To trace, debug, evaluate, and monitor LLM applications.

### Final Architecture Cheat Sheet

```text
User → Prompt / Messages → Chain, Runnable, or Agent
                              ├── Model → Parser → Response
                              ├── Retriever → Context → Model
                              ├── Tool Call → Execution → Model
                              └── Memory / State → Prompt Context

Callbacks and LangSmith observe the workflow.
```

### Final RAG Cheat Sheet

```text
Load → Split → Embed → Store
                         ↓
Query → Embed → Retrieve → Augment Prompt → Generate
```

### Final Tool Cheat Sheet

```text
Create Tool → Bind Tool → Model Suggests Call
            → Execute Tool → Return Result → Final Answer
```

### Revision Strategy

For every LangChain topic, revise in this order:

1. What problem does it solve?
2. What is the main concept?
3. What is the data flow?
4. What is a small code example?
5. What are the limitations and trade-offs?
6. How is it used in a complete project?

---

---
