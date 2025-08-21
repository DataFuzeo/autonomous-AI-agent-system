🚀 Autonomous AI Agent System

An AI-powered autonomous agent that answers employee-related queries from structured data and seamlessly falls back to web search when information is unavailable. Built with LangChain, Google Gemini, and Tavily Search API, this system delivers context-aware, multi-turn conversations with memory.

📌 Features

✅ Employee Dataset Querying – Retrieve salaries, role counts, highest/lowest paid employees, etc.

✅ Web Search Fallback – Uses Tavily API when dataset lacks answers.

✅ Conversational Memory – Maintains context across multiple queries.

✅ Google Gemini Integration – Provides natural, intelligent responses.

✅ Modular Tool-Based Architecture – Easily extendable with more tools.

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
└── README.md             # Project documentation

🔑 Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/datafuzeo/employee-agent-project.git
cd employee-agent-project

2️⃣ Create a Virtual Environment
# Mac/Linux
python -m venv venv
source venv/bin/activate  

# Windows
python -m venv venv
venv\Scripts\activate  

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Up Environment Variables

Copy .env.example to .env and fill in your API keys:

GEMINI_API_KEY=your_google_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key

▶️ Running the Application
python app.py


💬 Example queries you can try:

How many Data Scientists do we have?

What is the average salary of a Software Engineer?

Who is the highest paid employee?

What is the lowest salary in the company?

Give me today’s latest AI news.

👉 Type exit to quit the program.

🛠️ Tech Stack

LangChain
 – Agent orchestration

Google Gemini
 – LLM reasoning

Tavily Search
 – Web search integration

Pandas – Dataset queries

🤝 Contributing

Contributions are welcome! Please fork the repo, create a feature branch, and submit a pull request.

📜 License

This project is licensed under the MIT License – feel free to use and adapt it.
