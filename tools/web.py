
import requests
from bs4 import BeautifulSoup

def search_web(query: str) -> str:
    try:
        url = f"https://html.duckduckgo.com/html/?q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.select(".result__snippet")
        if results:
            return f"[WebTool] {results[0].get_text(strip=True)}"
        return "[WebTool] No good result found."
    except Exception as e:
        return f"[WebTool] Error: {e}"
