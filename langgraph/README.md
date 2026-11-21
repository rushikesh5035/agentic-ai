## What is Agentic AI

**Agentic AI is a type of AI software paradigm where a system takes a goal from a user and works toward completing it independently with minimal human guidance.**

**Unlike traditional Generative AI, which is primarily reactive and responds to prompts, Agentic AI can be proactive and goal-oriented.**

**It can plan, make decisions, take actions, adapt to changes, and seek human help when necessary.**

**In simple words: Generative AI generates answers, while Agentic AI can use AI to take actions and complete tasks.**

_Example: AI Recruitment Agent_

_User: "Hire a backend engineer with 2–4 years of experience."_

The AI agent can:

- Create a job description.
- Post the job on approved platforms.
- Collect applications.
- Analyze resumes.
- Shortlist suitable candidates.
- Schedule interviews with approval.

The agent works toward the user's goal rather than simply answering questions.

## Key Characteristics of Agentic AI:

### 1. Autonomy

Autonomy refers to the AI system's ability to make decisions and take actions independently to achieve a given goal, without requiring step-by-step human instructions.

1. **It's proactive**

   The agent can decide what needs to be done next instead of waiting for instructions at every step.

   _Example: After collecting resumes, the agent automatically begins screening them._

2. **Autonomy in multiple facets**
   - **Execution:** Performs tasks independently.
   - **Decision-making:** Chooses the next action.
   - **Tool usage:** Selects and uses available tools.

3. **Autonomy can be controlled**

   Autonomy does not mean the agent can do everything without restrictions.

   **A. Permission Scope** - Limits what tools and actions an agent can perform independently.

   _Example: The agent can screen candidates but cannot reject them without approval._

   **B. Human-in-the-Loop (HITL)** - Introduces checkpoints where human approval is required before continuing.

   _Example: "Can I publish this job description?"_

   **C. Override Controls** - Allow users to stop, pause, or change the agent's behavior.

   _Example: "Pause candidate screening."_

   **D. Guardrails / Policies** - Define rules and boundaries that the agent must follow.

   _Example: Never schedule interviews on weekends._

4. **Autonomy can be dangerous**
   - The agent sends job offers with incorrect salary information.

   - The agent unfairly shortlists candidates based on age or nationality.

   - The agent spends more money on LinkedIn advertisements than the approved budget.

   Therefore, agents need appropriate permissions, monitoring, and safety controls.

---

### 2. Goal Oriented

Being goal-oriented means the AI system operates with a persistent objective and continuously directs its actions toward achieving that objective rather than responding to isolated prompts.

**A. Goals act as a compass for the agent**

The goal guides the agent's decisions and actions.

_Example: The main goal is to hire a backend engineer. The agent's actions should support that goal._

**B. Goals come with constraints**

Constraints define the boundaries within which the agent must achieve its goal.

Example:

- Experience: 2–4 years.
- Required skills: Python, FastAPI, Cloud.
- Work type: Remote.
- Budget: ₹15 LPA maximum.

**C. Goals are stored in the agent's state or memory.**
Example:

```py
agent_state = {
    "main_goal": "Hire a backend engineer",

    "constraints": {
        "experience": "2-4 years",
        "skills": ["Python", "FastAPI", "Cloud"],
        "remote_only": True
    },

    "status": "active",

    "progress": {
        "jd_created": True,
        "posted_on": ["LinkedIn"],
        "applications_received": 8,
        "interviews_scheduled": 2
    }
}
```

This is a simplified representation of the agent's current task state.

**D. Goals can be altered**

An agent should be able to update its plan when the user changes the goal.

Example:

- Original goal: Hire a full-time backend engineer.
- Updated goal: Hire a freelance backend developer instead.
- The agent updates its approach based on the new objective.

---

### 3. Planning

Planning is the agent's ability to break down a high-level goal into a structured sequence of actions or sub-goals and decide the best path to achieve the desired outcome.

**Step 1: Generating multiple candidate plans**

**Plan A:**

- Post the job on LinkedIn.
- Post the job on other approved hiring platforms.
- Collect applications.

**Plan B:**

- Use internal referrals.
- Contact hiring agencies.
- Collect suitable candidates.

**Step 2: Evaluate each plan**

The agent evaluates different factors before selecting a plan.

- **Efficiency:** Which plan is faster?
- **Tool Availability:** Which tools are available?
- **Cost:** Does the plan require paid services?
- **Risk:** What happens if the plan fails?
- **Alignment:** Does the plan match the user's requirements?

**Step 3: Select the best plan**

The agent can select a plan using:

- **Human-in-the-Loop:** Ask the user which plan they prefer.

  _Example: "Would you prefer LinkedIn or internal referrals?"_

- **Predefined Policies:** Follow rules already defined by the developer.

  _Example: "Use low-cost hiring channels before paid platforms."_

---

### 4. Reasoning

Reasoning is the process through which an AI agent interprets information, draws conclusions, and makes decisions while planning and executing actions.

**A. Reasoning During Planning:**

1.  **Goal decomposition -** Breaks a large goal into smaller tasks.

    _Example: Hiring an engineer → Create JD → Collect resumes → Screen candidates → Schedule interviews._

2.  **Tool selection -** Decides which tools are required for each task.

    _Example: Use LinkedIn API for job posting and a calendar API for interview scheduling._

3.  **Resource estimation -** Estimates the time, cost, dependencies, and risks involved.

    _Example: Posting a job on a free platform may take longer to receive applications._

**B. Reasoning During Planning:**

1.  **Decision-making -** Chooses between different available options.

    _Example: Three candidates match the requirements. The agent identifies the two most suitable candidates for further review._

2.  **HITL handling -** Recognizes when human assistance is required.

    _Example: The agent is unsure about the salary range and asks the recruiter._

3.  **Error handling -** Interprets tool or API failures and decides how to recover.

    _Example: If the calendar API fails, the agent retries or asks for assistance._

---

### 5. Adaptavility

Adaptability is the agent's ability to modify its plans, strategies, or actions in response to unexpected conditions while remaining aligned with its primary goal.

**Examples**

1. **Tool Failure**: The calendar API fails.

   The agent retries or uses an alternative approved scheduling method.

2. **External Feedback**: Very few applications are received.

   The agent suggests changing the job description or using another hiring platform.

3. **Changing Goals**: The user changes the requirement from hiring a full-time employee to hiring a freelancer.

   The agent updates its plan accordingly.

---

### 6. Context awareness

Context awareness is the agent's ability to understand and use relevant information from the ongoing task, previous interactions, user preferences, and environment to make better decisions.

**Types of Context**

- **A. Original Goal**

  The primary objective assigned to the agent.

  _Example: Hire a backend engineer._

- **B. Progress Updates**

  Information about actions already completed.

  _Example: Job description created and posted._

- **C. Environment State**

  Current information from the environment.

  _Example: Number of applications received._

- **D. Tool Responses**

  Information returned by external tools.

  _Example: Candidate resume details or calendar availability._

- **E. User Preferences and Constraints**

  Rules and preferences that guide the agent's behavior.

  _Example: Never send a job offer without approval._

**How is context awareness implemented?**

Context awareness can be supported through state management, conversation history, and memory.

**Short-Term Memory**

Stores information relevant to the current task or conversation.

_Example: The current candidate's resume and interview details._

**Long-Term Memory**

Stores information that may be useful across multiple sessions.

_Example: The recruiter's preference for remote candidates._

**Important:** Memory and state are related but different. State tracks the current workflow, while memory stores information that may be useful later.

## Key Components of Agentic AI:

1. **Brain (LLM)**

   The LLM acts as the reasoning engine or brain of the agent.

   It handles:
   - Understanding user instructions.
   - Goal interpretation.
   - Planning.
   - Reasoning.
   - Tool selection.
   - Generating responses.

   _Examples: GPT, Claude, Gemini, Llama._

2. **Orchestrator**

   The orchestrator acts like a project manager.

   It manages:
   - Task sequencing.
   - Workflow execution.
   - Conditional routing.
   - Retry logic.
   - Loops.
   - Delegation between agents or tools.

   _Example: Deciding whether the recruitment agent should continue screening resumes or move to interview scheduling._

3. **Tools**

   Tools allow the agent to interact with external systems and perform actions.

   Examples:
   - APIs.
   - Databases.
   - Web search.
   - Calendar services.
   - Python execution.
   - File systems.

   _Example: Using a calendar API to schedule interviews._

4. **Memory**

   Memory maintains relevant information from previous interactions and tasks.

   **Short-Term Memory:** Current conversation and task information.

   **Long-Term Memory:** User preferences, previous experiences, and useful information retained across sessions.

5. **Supervisor**

   The supervisor manages human oversight and control.

   It is responsible for:
   - Human approvals.
   - Monitoring agent actions.
   - Handling escalations.
   - Enforcing policies.
   - Reviewing sensitive operations.

   _Example: The agent prepares a job offer but waits for recruiter approval before sending it._

   Note: The supervisor can be a human, a software component, or a combination of both.

## What is LangChain

LangChain is an open-source framework designed to simplify the development of LLM-powered applications.

It provides reusable building blocks that allow developers to connect LLMs with prompts, tools, external data, and other application components.

In simple words, LangChain helps developers build applications using LLMs without implementing every integration from scratch.

**Key components of LangChain:**

1. **Model:**

   Provides a **unified interface** to interact with various LLMs (e.g., OpenAI, Anthropic, open-source models),

   This makes it easier to whitch between different model providers

2. **Prompts:**

   Prompts define the instructions and input provided to an LLM.

   LangChain provides tools to create and manage reusable prompts.

   _Example: "Analyze this resume and identify the candidate's technical skills."_

3. **Retrievers:**

   Retrievers fetch relevant documents or information from a knowledge base.

   They are commonly used in RAG (Retrieval-Augmented Generation) applications.

   _Example: Retrieve relevant documentation before answering a user's question._

4. **Tools**

   Tools allow an LLM-powered agent to interact with external systems.

   _Examples: Search the web, Query a database, Call an API, Execute Python code_

5. **Chains**

   Chains connect multiple components together into a workflow.

   _Example: User Input → Prompt → LLM → Output_

   LangChain also supports more complex chains involving multiple steps.

   Important: Chains are an important part of LangChain, but modern LangChain also supports agents, tools, structured outputs, and other application-building capabilities.

## The Challenge with LangChain

LangChain provides powerful abstractions for building LLM applications and agents.

However, as applications become more complex, managing workflow execution and control flow can become challenging.

**1. Linear vs. Non-linear Workflows:**

LangChain's sequential workflows are straightforward.

However, complex applications may require:

- Conditional branching.
- Loops.
- Multiple execution paths.
- Dynamic decision-making.

These workflows require more orchestration.

**2. The "Glue Code" Problem**

Developers may need to write additional Python code to manage:

- Conditional execution.
- State transitions.
- Retry logic.
- Workflow control.

This additional code is commonly referred to as **"glue code"** problem

**3. State Management**

Complex AI agents need to maintain information throughout execution.

Examples:

- Current task progress.
- Previous tool results.
- Conversation history.
- Intermediate decisions.

Managing this information becomes more important as workflows grow.

4. Maintenance Issues

As the application becomes more complex, custom workflow logic can become difficult to debug, maintain, and modify.

These challenges motivated the development of LangGraph.

**Important:** LangChain can build iterative agents and complex applications. LangGraph provides more explicit control over stateful, graph-based workflows.

## What is LangGraph

LangGraph is an open-source library developed by the LangChain team to orchestrate complex, stateful AI agent workflows.

While LangChain provides building blocks for LLM applications, LangGraph models workflows as graphs consisting of nodes, edges, and shared state.

It is designed for workflows involving:

- conditional branching.
- Loops and iterative execution.
- State management.
- Persistence and checkpointing.
- Human-in-the-loop approval.
- Multi-agent orchestration.

### Key Components of langGraph

- **1. State**

  State stores and maintains information throughout workflow execution.

  _Example: User input, task progress, and tool results._

- **2. Nodes**

  Nodes represent individual operations or tasks.

  _Example: An LLM call, database query, or document retrieval operation._

- **3. Edges**

  Edges define how execution moves between nodes.

  _Example: Move from the LLM node to the tool node._

4. **Conditional Edges**

   Conditional edges determine the next execution step based on the current state.

   _Example: If the agent needs a tool, execute the tool. Otherwise, return the final response._

5. **Checkpoints**

   Checkpoints save the workflow's state at specific points.

   They support:
   - Persistence.
   - Resuming workflows.
   - Human approval.
   - Recovery from interruptions.

---

## How LangGraph Works

LangGraph follows a graph-based workflow.

**Step 1: Define State**

Define the information that needs to be maintained throughout the workflow.

**Step 2: Create Nodes**

Each node performs a specific operation.

Example:

- Analyze resume.
- Generate SQL.
- Execute tool.
- Create report.

**Step 3: Connect Nodes**

Use edges to define the execution flow.

**Step 4: Define Conditional Routing**

Determine which node should execute next based on the current state.

**Step 5: Compile the Graph**

Compile the workflow before execution.

**Step 6: Execute the Graph**

Invoke the graph with an initial state.

**Example: LangGraph Workflow**

```
START
  |
  v
 LLM
  |
  v
Need Tool?
  |
  | Yes
  v
Execute Tool
  |
  v
Return to LLM
  |
  | No
  v
Final Response
  |
  v
 END
```

This workflow can repeat until the agent completes the task.

## Features of LangGraph

**1. State Management**

State management refers to maintaining and updating information throughout the execution of a workflow.

LangGraph allows nodes to read and update a shared state, helping the agent maintain information about its current task and progress.

Example:

In an AI recruitment agent, the state may contain:

- Candidate information.
- Resume analysis results.
- Interview scheduling status.
- Current task progress.

This information can be passed between different nodes.

**2. Event-Driven Execution**

Event-driven execution allows a workflow to pause and wait for an external event, user input, or human approval before continuing.

_Example:_

_An AI recruitment agent prepares an interview schedule._
_Instead of scheduling interviews immediately, it pauses and asks the recruiter for approval._
_Once the recruiter approves, the workflow resumes._

This is useful for long-running workflows that require external input.

**3. Fault Tolerance**

Fault tolerance refers to the ability of a system to recover from failures without losing all its previous progress.

LangGraph supports this through `checkpointing and persistence`

**Checkpointing**

Checkpointing saves the current state of a workflow at specific execution points.

If the application crashes or encounters an error, the workflow can resume from a previously saved checkpoint instead of starting from the beginning.

Example:

An AI recruitment agent has already:

- Created a job description.
- Collected 100 resumes.
- Analyzed 50 resumes.

If the server crashes, the agent can resume from the saved state rather than processing everything again.

**Important:** Recovery depends on configuring persistence and appropriate error handling. Checkpointing alone does not automatically prevent every failure.

**4. Human-in-the-Loop (HITL)**

Human-in-the-Loop allows an AI agent to pause its execution and request human approval or assistance.

LangGraph supports this through interruption and resumption mechanisms.

_Example:_

_An AI agent prepares a job offer._

_Before sending it, the workflow pauses and asks:_

_"Do you approve sending this offer to the candidate?"_

_The agent continues only after the required approval._

This is useful when:

- Actions are sensitive.
- Human judgment is required.
- The agent needs clarification.
- Important decisions require approval.

**5. Nested Workflows (Subgraphs)**

A subgraph is a graph used inside another graph.

It allows developers to break a complex workflow into smaller, reusable components.

**Example: AI Recruitment Agent**

The main workflow may contain:

- Resume Screening Subgraph.
- Candidate Evaluation Subgraph.
- Interview Scheduling Subgraph.
- Offer Generation Subgraph.

Each subgraph handles a specific responsibility.

**Benefits:**

- Modular architecture.
- Code reusability.
- Easier maintenance.
- Better organization of complex workflows.
- Useful for multi-agent systems.

**6. Observability**

Observability refers to the ability to understand, monitor, and debug what happens inside an AI application.

LangGraph integrates with LangSmith, a platform for tracing, monitoring, and debugging LLM applications.

**What can we observe?**

- Which nodes were executed.
- The order of execution.
- Inputs and outputs of operations.
- Tool calls and their results.
- Workflow execution time.
- Errors and failures.
- State changes, when captured in the trace.

**Example:**

An AI SQL agent generates an incorrect SQL query.

Using tracing, developers can inspect:

1. The original user question.
2. The generated SQL query.
3. The database error.
4. The agent's retry attempt.
5. The final response.

This makes debugging easier.

**Important:** LangSmith supports tracing for both LangChain and LangGraph applications. LangGraph's graph structure provides additional visibility into node execution and workflow state.
