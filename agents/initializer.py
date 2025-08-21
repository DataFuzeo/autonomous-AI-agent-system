import os
from langchain.agents import initialize_agent, Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.employee_tools import lookup_employee
from utils.web_tools import tavily_search
from agents.prompts import system_prompt
from agents.memory import get_memory

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", google_api_key=GEMINI_API_KEY)

employee_tool = Tool(
    name="Employee Database Lookup",
    func=lookup_employee,
    description="Use this tool to answer questions strictly about employees from the dataset."
)

web_tool = Tool(
    name="Web Search",
    func=tavily_search,
    description="Use this tool for external information not in the employee dataset."
)

def init_agent():
    return initialize_agent(
        tools=[employee_tool, web_tool],
        llm=llm,
        agent="chat-conversational-react-description",
        verbose=True,
        system_message=system_prompt,
        memory=get_memory()
    )
