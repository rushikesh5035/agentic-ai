## Runnables

# 1. Task Specific Runnables
# These are core langChain components that have been converted into Runnables so they can be used in pipelines.
# it performs a task specific operations like LLM calls, prompting, retrieval, etc.
# Examples: 1. ChatOpenAI (Runs an LLM model), 2. PromptTemplate (formats prompts dynamically), 3. LLMChain, 4. RetrievalQA, etc.

# 2. Runnable Primitives
# These are the fundamental building blocks for structuring execution logic in AI workflows. 
# They help orchestrate execution by defining how different components interact (sequentially, in parallel, conditionally, etc.) and manage the flow of data between them.

# Examples: 
# 1. RunnaleSequence -> RUn steps in order (| operator) 
# 2. RunnableParallel -> Runs multiple steps in parallel/simultaneosly. 
# 3. RunnableMap -> Maps the same input across multiple function.
# 4. RunnanleBranch -> Implement conditional execution (if-else logic)
# 5. RunnableLambda -> Wraps custom Python Functions into Runnables.
# 6. RunnablePassThrough -> just forwards input as output (acts as a plcaeholder)


