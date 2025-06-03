import requests
from bs4 import BeautifulSoup

def basic_web_search(query: str) -> str:
    print(f"[WebTool] Searching for: {query}")
    try:
        response = requests.get(
            f"https://www.google.com/search?q={query}",
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=5  # 5-second timeout to prevent hanging
        )

        if response.status_code != 200:
            return "Hmm... I couldn't reach the search engine. Try again later."

        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.select("div.BNeawe.vvjwJb.AP7Wnd")
        snippets = soup.select("div.BNeawe.s3v9rd.AP7Wnd")

        output = []
        for title, snippet in zip(results[:3], snippets[:3]):
            output.append(f"{title.text.strip()}: {snippet.text.strip()}")

        return "\n\n".join(output) if output else "I searched everywhere but found nothing relevant."
    
    except requests.exceptions.Timeout:
        return "It seems the request is taking too long... maybe the network is down."
    except requests.exceptions.RequestException as e:
        return f"I'm sorry, but I don’t think we're connected to the internet right now… ({e})"
