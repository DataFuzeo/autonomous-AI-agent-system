from agents.initializer import init_agent

if __name__ == "__main__":
    agent = init_agent()
    while True:
        user_query = input("Ask something (or type 'exit'): ")
        if user_query.lower() == "exit":
            break
        response = agent.invoke({"input": user_query})
        print("\nAgent Response:\n", response["output"])
