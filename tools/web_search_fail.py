import requests


def duckduckgo_search(query: str, k: int = 5):
    """
    Perform a web search using the DuckDuckGo Instant Answer API.

    Parameters:
        query (str): The search query string from the user.
        k (int): The number of search results to return.

    Returns:
        list[dict]: A list of up to `k` search results containing title and URL.
    """
    # DuckDuckGo Instant Answer API endpoint
    url = "https://api.duckduckgo.com/"

    # Send request
    params = {
        "q": query,
        "format": "json",
        "no_redirect": 1,
        "no_html": 1
    }

    response = requests.get(url, params=params)
    data = response.json()

    results = []

    # Extract related topics (these often contain useful links)
    for topic in data.get("RelatedTopics", []):
        if "Text" in topic and "FirstURL" in topic:
            results.append({
                "title": topic["Text"],
                "url": topic["FirstURL"]
            })
        # Some topics are nested under 'Topics'
        elif "Topics" in topic:
            for subtopic in topic["Topics"]:
                if "Text" in subtopic and "FirstURL" in subtopic:
                    results.append({
                        "title": subtopic["Text"],
                        "url": subtopic["FirstURL"]
                    })

        if len(results) >= k:
            break

    return results[:k]


def search_api_tool(query: str):
    """Requires api key of google

    Args:
        query (str): any topic you wanna search
    """
    url = "https://www.searchapi.io/api/v1/search"
    params = {
        "engine": "google",
        "q": query
    }

    response = requests.get(url, params=params)
    return response


def brave_search_tool(query: str):
    """Requires Brave Api key

    Args:
        query (str): any topic you wanna search
    """
    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": ""
    }
    params = {
        "q": query
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f"Error {response.status_code}: {response.text}"
