import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def tavily_search(query: str, max_results: int = 5) -> str:
    response = client.search(query=query, max_results=max_results)
    results = response.get("results", [])

    if not results:
        return "No results found."

    formatted = []
    for i, r in enumerate(results, 1):
        title = r.get("title", "Unknown")
        url = r.get("url", "")
        snippet = r.get("content", "").strip()

        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."

        formatted.append(f"{i}. **{title}**\n   {url}\n   {snippet}")

    return "\n\n".join(formatted)