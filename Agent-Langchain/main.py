from langchain_groq import ChatGroq
from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent
from dotenv import load_dotenv
import os
# API loading
load_dotenv()
# duckduckgo search 
search_tool = DuckDuckGoSearchRun()
# creating tool for calculator 
@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""
    try:
        return str(eval(expression))
    except Exception:
        return "Invalid mathematical expression."
# LLM  bna raha hu
llm = ChatGroq(
    model= "llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
)
# Agent bna rhe h 
agent = create_agent(
    model=llm,
    tools=[search_tool,calculator],
    system_prompt="""You are a helpful AI research assistant.

Use DuckDuckGo when the user asks for current, recent, or up-to-date information.

Use the calculator when the user asks for arithmetic calculations.

For general questions that do not require tools, answer directly."""
)
# first query || query mai duckduckgo or calculator dono use hor rhe h 
response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Search the web for the current population of India. Then calculate what 2% of that population is. Finally, explain the result in one sentence."
        }
    ]
})
print(response["messages"][-1].content)
# output with the flow of agen (flow which agent follows 
for message in response["messages"]:
    if hasattr(message, "tool_calls") and message.tool_calls:
        print("Tool called:")
        print(message.tool_calls)