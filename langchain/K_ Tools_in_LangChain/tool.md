### What is a Tool?

A Tool is just a Python function (or API) that is packaged in a way the LLM can understand and call when needed.

_LLM (Like GPT( are great at:_

1. Reasoning
2. language generation

_But they **can't do things like**:_

1. Access live data (weather, news)
2. Do reliable math
3. Call APIs
4. Run Code 5. Interact with a databse

---

#### Langchain Tools

1. Built-in Tools
2. Custome Tools

---

#### How Tools fits into the Agent Ecosystem

An AI agent is an LLM-powered system that can autonomously think, decide and take actions using external tools or APIs to achieve a goal

---

### Built-in tools

A built-in tools is a tool that LangChain already provides you -- It's pre-build, production ready, and requores minimal or no setup.

You don't have to write the function logic yourself -- you just import and use it.

**Most Common Built-in Tool:**

1. _DuckDuckGoSearchRun_ - Web search via DuckDuckGO
2. _WikipediaQueryRun_ - Wikipedia summary
3. _PythonREPLTool_ - Run raw python code
4. _ShellTool_ - Run shell commands
5. _RequestGetTool_ - Make HTTP GET requests
6. _GmailSendMessaeTool_ - Send emails via Gmail
7. _SlackSendMessageTool_ - Post message to Slack
8. _SQLDatabaseQueryTool_ - Run SQL queries

---

**Custom Tool**

A custom tool is a tool that you define yourself.

Use them when:

- you want to call **your own APIs**
- you want to **encapsulate business logic**
- you want the LLM to interact with **your database, product, or app**

---

### Structured Tool

A **Structured Tool** in langchain is a special type of tool where the input to the tool follows a structured schema, typically defined using a Pydantic model

---

### BaseTool Class

**BaseTool Class** is the abstract base class for all tools in langChain.
It defines the core structure and interface that any tool must follow, whether it's a simple one-liner or a fully customized function.

All other tool types liek **@tool, StructuredTool** are build on top of BaseTool

---

### Toolkits

A toolkit is just a collection (bundle) of related tools that serve a common purpose -- packaged together for convenience and reusability.

In langchain:

- A toolkit might be: GooglDriveToolKit
- and it can contain the following tools

1. GoogleDriveCreateFileTool: Upload a file
2. GoogleDriveSearchTool: Search for a file by name/content
3. GoogleDriveReadFileTool: read contents of a file
