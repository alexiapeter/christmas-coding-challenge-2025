import os
from tavily import TavilyClient
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv('API_TAVILY')
tavily = TavilyClient(api_key)

# Christmas Market Explorer : in terminal
def find_christmas_markets(city):
    print(f"Searching for Christmas markets in {city}...")
    query = f"Christmas markets in {city} 2024 dates locations and opening hours"
    response = tavily.search(
        query=query,
        search_depth="advanced",
        max_results=3
    )

    print("\nSEARCH RESULTS")
    for result in response['results']:
        print(f"Source: {result['title']}")
        print(f"Content snippet: {result['content'][:200]}...")
        print(f"URL: {result['url']}")
        print("-" * 30)

    return response['results']

if __name__ == "__main__":
    city_input = input("Enter a city to search (e.g., Berlin): ")
    find_christmas_markets(city_input)