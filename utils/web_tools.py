from tavily import TavilyClient
import os

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

def tavily_search(query: str) -> str:
    """Perform a web search using Tavily."""
    results = tavily_client.search(query)
    if "results" in results and results["results"]:
        return results["results"][0]["content"]
    return "No results found."
