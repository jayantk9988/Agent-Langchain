# 🤖 LangChain Multi-Tool AI Agent

A simple AI agent built using **LangChain, Groq, DuckDuckGo Search, and custom tools**.

This project demonstrates how an LLM can dynamically decide when to use external tools instead of answering everything directly.

The agent can:

- 🧠 Answer general questions using an LLM
- 🌐 Search the internet using DuckDuckGo
- 🧮 Perform mathematical calculations using a custom calculator tool
- 🔀 Dynamically choose the appropriate tool based on the user's query
- 🔗 Use multiple tools in a single task when required

---

## 📌 Project Overview

Traditional LLM applications generally follow a simple pattern:

```text
User
 ↓
LLM
 ↓
Answer
```

However, an AI agent can decide whether it needs additional tools to complete a task.

This project follows:

```text
                 ┌──────────────┐
                 │     User     │
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │   AI Agent   │
                 └──────┬───────┘
                        ↓
              ┌─────────┼─────────┐
              ↓         ↓         ↓
          🌐 Search  🧮 Calculator 🧠 LLM
              ↓         ↓         ↓
              └─────────┼─────────┘
                        ↓
                 Final Response
```

The main purpose of this project is to understand the **fundamentals of tool-using AI agents** using modern LangChain APIs.

---

# 🚀 Features

## 1. General Question Answering

The agent can answer questions that do not require external tools.

Example:

```text
User:
What is a Python variable?
```

The agent can answer directly using the LLM.

Flow:

```text
User
 ↓
Agent
 ↓
LLM
 ↓
Answer
```

No external tool is required.

---

## 2. Internet Search

The agent can use **DuckDuckGo Search** when the user asks for current or up-to-date information.

Example:

```text
User:
What is the latest news about AI?
```

The agent can decide that it needs internet access and call the DuckDuckGo search tool.

Flow:

```text
User
 ↓
Agent
 ↓
DuckDuckGo Search
 ↓
Search Results
 ↓
LLM
 ↓
Final Answer
```

---

## 3. Calculator Tool

The project also contains a custom calculator tool created using LangChain's `@tool` decorator.

Example:

```text
User:
Calculate 456 * 78
```

The agent can choose the calculator instead of trying to perform the calculation itself.

Flow:

```text
User
 ↓
Agent
 ↓
Calculator Tool
 ↓
Result
 ↓
LLM
 ↓
Final Answer
```

---

## 4. Multiple Tools

The agent has access to multiple tools:

```text
Tools
├── DuckDuckGo Search
└── Calculator
```

The LLM decides which tool is appropriate for the user's request.

For example:

```text
"What is the latest AI news?"
        ↓
DuckDuckGo Search
```

while:

```text
"What is 125 × 37?"
        ↓
Calculator
```

And:

```text
"What is a Python dictionary?"
        ↓
No tool
        ↓
LLM directly
```

---

## 5. Multi-Step Tool Usage

The agent can also handle tasks that require more than one tool.

Example:

```text
Search the current population of India and calculate
what 2% of that population is.
```

Possible flow:

```text
User
 ↓
Agent
 ↓
DuckDuckGo Search
 ↓
Population Result
 ↓
Agent / LLM
 ↓
Calculator
 ↓
Calculation Result
 ↓
Agent / LLM
 ↓
Final Answer
```

This demonstrates an important characteristic of agents:

> The agent can decide what action to take based on the current state of the task.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming language |
| LangChain | Agent and tool framework |
| LangGraph | Agent execution/state management |
| Groq | LLM inference |
| Llama 3.3 70B | Language model |
| DuckDuckGo | Internet search |
| python-dotenv | Environment variable management |

---

# 📂 Project Structure

```text
Agent-Langchain/
│
├── .venv/
│
├── main.py
│
├── requirements.txt
│
├── .env
│
├── .gitignore
│
└── README.md
```

### Important

The following files/folders should **not** be pushed to GitHub:

```text
.venv/
.env
__pycache__/
```

Your `.env` file contains your API key and must remain private.

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/jayantk9988/Agent-Langchain.git
```

Move into the project directory:

```bash
cd Agent-Langchain
```

---

# 🐍 2. Create a Virtual Environment

Create a virtual environment:

```bash
python -m venv .venv
```

### Windows

Activate it using PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell execution policy prevents activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate the environment again:

```powershell
.venv\Scripts\Activate.ps1
```

---

# 📦 3. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

---

# 🔑 4. Configure Environment Variables

Create a file named:

```text
.env
```

inside the project directory.

Add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

The application loads this key using:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
```

### ⚠️ Security Warning

Never commit your `.env` file to GitHub.

Add this to `.gitignore`:

```gitignore
.env
```

---

# ▶️ Running the Project

After activating the virtual environment and installing the dependencies:

```bash
python main.py
```

The agent will process the query provided in the code.

---

# 🧠 How the Agent Works

The main components of the project are:

## 1. LLM

The project uses Groq with the Llama 3.3 70B model.

```python
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
)
```

The LLM is responsible for:

- Understanding the user's request
- Deciding whether a tool is required
- Selecting the appropriate tool
- Interpreting tool results
- Generating the final response

---

# 🌐 2. DuckDuckGo Search Tool

DuckDuckGo is initialized as a LangChain tool:

```python
search_tool = DuckDuckGoSearchRun()
```

This allows the agent to retrieve information from the internet.

For example:

```text
"What is the latest news about AI?"
```

can trigger:

```text
duckduckgo_search
```

---

# 🧮 3. Custom Calculator Tool

The calculator is created using LangChain's tool decorator:

```python
@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""
    try:
        return str(eval(expression))
    except Exception:
        return "Invalid mathematical expression."
```

The tool accepts a mathematical expression and returns the result.

Example:

```python
calculator.invoke("125 * 37")
```

Result:

```text
4625
```

---

# 🤖 4. Creating the Agent

The LLM and tools are combined using LangChain's agent API:

```python
agent = create_agent(
    model=llm,
    tools=[search_tool, calculator],
    system_prompt="""You are a helpful AI research assistant.

Use DuckDuckGo when the user asks for current, recent,
or up-to-date information.

Use the calculator when the user asks for arithmetic calculations.

For general questions that do not require tools,
answer directly."""
)
```

The important part is:

```python
tools=[search_tool, calculator]
```

This gives the agent access to both tools.

---

# 🔄 Agent Decision-Making

The agent doesn't simply execute every tool for every query.

Instead, the LLM decides whether a tool is necessary.

### Example 1 — General Question

```text
What is a Python variable?
```

Flow:

```text
User
 ↓
Agent
 ↓
No tool required
 ↓
LLM
 ↓
Answer
```

---

### Example 2 — Calculation

```text
Calculate 456 * 78
```

Flow:

```text
User
 ↓
Agent
 ↓
Calculator
 ↓
456 × 78
 ↓
Result
 ↓
LLM
 ↓
Answer
```

---

### Example 3 — Internet Search

```text
What is the latest news about AI?
```

Flow:

```text
User
 ↓
Agent
 ↓
DuckDuckGo
 ↓
Search Results
 ↓
LLM
 ↓
Answer
```

---

### Example 4 — Multiple Tools

```text
Search the current population of India and calculate 2% of it.
```

Possible flow:

```text
User
 ↓
Agent
 ↓
DuckDuckGo
 ↓
Population
 ↓
Calculator
 ↓
2% calculation
 ↓
LLM
 ↓
Final Answer
```

---

# 🔍 Inspecting Tool Calls

The project can also inspect the messages returned by the agent.

Example:

```python
for message in response["messages"]:
    if hasattr(message, "tool_calls") and message.tool_calls:
        print("Tool called:")
        print(message.tool_calls)
```

This allows us to observe which tool the agent selected.

For example:

```text
Tool called:

[
    {
        'name': 'calculator',
        'args': {
            'expression': '456 * 78'
        }
    }
]
```

This is useful for understanding how tool calling works internally.

---

# 📤 Getting Only the Final Answer

The agent returns a state containing multiple messages.

To print only the final response:

```python
print(response["messages"][-1].content)
```

Instead of printing the complete agent state.

---

# 🧪 Example Queries

You can test the agent using different types of queries.

### General Question

```text
What is a Python variable?
```

Expected behavior:

```text
LLM → Direct Answer
```

---

### Calculator

```text
Calculate 125 * 37
```

Expected behavior:

```text
Calculator → Final Answer
```

---

### Internet Search

```text
What is the latest news about AI?
```

Expected behavior:

```text
DuckDuckGo → Final Answer
```

---

### Multi-Tool Query

```text
Search the current population of India and calculate what 2% of that population is.
```

Expected behavior:

```text
DuckDuckGo
     ↓
Population
     ↓
Calculator
     ↓
Final Answer
```

---

# ⚠️ Known Warning

Depending on the installed LangChain version, you may see a warning related to:

```text
langchain-community
```

For example:

```text
DeprecationWarning:
langchain-community is being sunset...
```

This is a **warning rather than a Python execution error**.

The DuckDuckGo integration used in this learning project currently comes from:

```python
from langchain_community.tools import DuckDuckGoSearchRun
```

The LangChain ecosystem is actively moving integrations toward standalone packages, so this part of the project may need to be updated as the ecosystem evolves.

---

# 🧩 Troubleshooting

## `ModuleNotFoundError`

If you see:

```text
ModuleNotFoundError
```

make sure the virtual environment is activated:

```powershell
.venv\Scripts\Activate.ps1
```

Then install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Groq API Error

If you receive an authentication error, check your `.env` file:

```env
GROQ_API_KEY=your_actual_api_key
```

Also make sure:

```python
load_dotenv()
```

is executed before:

```python
os.getenv("GROQ_API_KEY")
```

---

## Tool Calling Error

If the individual components work but the agent produces a Groq:

```text
tool_use_failed
```

error, test each component independently.

### Test LLM

```python
response = llm.invoke(
    "Explain AI agents in one sentence."
)

print(response.content)
```

### Test DuckDuckGo

```python
result = search_tool.invoke(
    "latest AI news"
)

print(result)
```

### Test Calculator

```python
result = calculator.invoke(
    "125 * 37"
)

print(result)
```

If all three work individually but the agent fails, the issue is likely related to **agent/tool-calling compatibility rather than the individual tools**.

---

# 🎯 Learning Objectives

This project was created primarily as a learning project to understand:

- What an AI agent is
- How agents differ from simple LLM calls
- How LangChain tools work
- How to create custom tools
- How an LLM chooses tools
- How external tools can extend an LLM
- How multiple tools can work together
- How agent state contains multiple messages
- How tool calls are represented
- How an agent can perform multi-step tasks
- How Groq can be used as an LLM provider

---

# 🧠 Agent vs Normal LLM

### Normal LLM

```text
User
 ↓
LLM
 ↓
Answer
```

The LLM itself generates the response.

### Tool-Using Agent

```text
User
 ↓
Agent
 ↓
LLM decides what to do
 ↓
┌───────────────┐
│ Tool required?│
└───────┬───────┘
        │
   ┌────┴────┐
   ↓         ↓
  Yes        No
   ↓         ↓
 Tool      Answer
   ↓
 Result
   ↓
 LLM
   ↓
Final Answer
```

This is the fundamental concept demonstrated by this project.

---

# 🚀 Future Improvements

This project can be extended in several ways.

### 1. Add More Tools

Possible tools:

- Weather
- Wikipedia
- Web scraping
- File reading
- Database queries
- APIs
- Email
- Calendar

---

### 2. Add Conversation Memory

Allow the agent to remember previous interactions:

```text
User:
My name is Jayant.

Agent:
Nice to meet you!

User:
What is my name?

Agent:
Your name is Jayant.
```

---

### 3. Add Structured Output

Instead of returning plain text, the agent could return structured JSON.

Example:

```json
{
  "answer": "...",
  "sources": [],
  "tools_used": []
}
```

---

### 4. Build a Web Interface

The agent could be connected to:

- Streamlit
- FastAPI
- Next.js
- React

to create a user-facing AI assistant.

---

### 5. Add More Advanced Agent Workflows

Future versions could explore:

```text
Agent
 ↓
Planner
 ↓
Multiple Tools
 ↓
Memory
 ↓
Validation
 ↓
Final Response
```

---

# 📚 Key Concepts Learned

The most important concept from this project is:

> **An AI agent is not simply an LLM. It is an LLM connected to tools and a mechanism that allows it to decide what action to take.**

In this project:

```text
LLM
 +
Tools
 +
Agent Runtime
 =
Tool-Using AI Agent
```

---

# 👨‍💻 Author

**Jayant**

BTech CSE (AI) Student

This project was created as part of my learning journey in:

- Artificial Intelligence
- Generative AI
- LangChain
- AI Agents
- LLM Applications

---
