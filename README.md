# 🚀 Autonomous AI Agent System

An AI-powered conversational agent that:

- 🧑‍💼 Answers employee-related queries from a structured dataset  
- 🌐 Falls back to web search when the dataset lacks information  
- 🧠 Maintains chat memory for contextual and natural conversations  
- ⚡ Built with **LangChain**, **Google Gemini**, and **Tavily Search API**  

---

## 📂 Project Structure
autonomous-AI-agent-system/
│── app.py # Main entry point
│── requirements.txt # Dependencies
│── .env # API keys
│── .gitignore # Ignore sensitive files
│
├── data/
│ └── employee_data.csv # Employee dataset
│
├── utils/
│ ├── init.py
│ ├── employee_tools.py # Employee lookup logic
│ ├── web_tools.py # Tavily search logic
│
├── agents/
│ ├── init.py
│ ├── memory.py # ConversationBufferMemory setup
│ ├── prompts.py # System prompts
│ ├── initializer.py # Agent initialization
│
└── README.md # Project documentation

---

## ⚡ Features

- ✅ Query structured employee dataset (salary, count, role lookups, etc.)  
- ✅ Fallback to **Tavily web search** when data is not available  
- ✅ Uses **Google Gemini (Gemini-2.5-pro)** for reasoning and responses  
- ✅ Keeps conversation **memory** for multi-turn interactions  
- ✅ Extensible **tool-based architecture** (easily add more tools)  

---

## 🔑 Setup & Installation

### 1. Clone the repo
```bash
git clone https://github.com/datafuzeo/employee-agent-project.git
cd employee-agent-project
### 2. Create a virtual environment
python -m venv venv
source venv/bin/activate      # On Mac/Linux
venv\Scripts\activate         # On Windows
### 3. Install dependencies
pip install -r requirements.txt
### 4. Set up API keys

Copy .env.example to .env and fill in your credentials:

GEMINI_API_KEY=your_google_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key

### run Application:
python app.py
Example queries:

How many Data Scientists do we have?

What is the average salary of a Software Engineer?

Who is the highest paid employee?

What is the lowest salary in the company?

Give me today’s latest AI news.

Type exit to quit the program.

🛠️ Tech Stack

LangChain – Agent orchestration

Google Gemini – LLM reasoning

Tavily Search – Web search integration

Pandas – Dataset queries
