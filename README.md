🚀 Autonomous AI Agent System

An AI-powered autonomous agent that answers employee-related queries from structured data and seamlessly falls back to web search when information is unavailable. Built with LangChain, Google Gemini, and Tavily Search API, this system delivers context-aware, multi-turn conversations with memory.

✨ Features

Query employee dataset (salary, role counts, highest/lowest paid employees, etc.)

Fallback to Tavily API when dataset lacks answers

Maintain multi-turn conversational memory

Powered by Google Gemini for natural reasoning

📂 Project Structure
autonomous-AI-agent-system/
│── app.py                # Main entry point
│── requirements.txt      # Dependencies
│── .env                  # API keys
│── .gitignore            # Ignore sensitive files
│
├── data/
│   └── employee_data.csv # Employee dataset
│
├── utils/
│   ├── __init__.py
│   ├── employee_tools.py # Employee lookup logic
│   ├── web_tools.py      # Tavily search logic
│
├── agents/
│   ├── __init__.py
│   ├── memory.py         # ConversationBufferMemory setup
│   ├── prompts.py        # System prompts
│   ├── initializer.py    # Agent initialization
│
└── README.md             # Documentation
