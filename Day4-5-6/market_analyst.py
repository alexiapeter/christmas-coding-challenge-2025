import os

import ollama
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()
api_key = os.getenv('API_TAVILY')
tavily = TavilyClient(api_key)

OLLAMA_MODEL = "qwen2.5:0.5b"


def search_markets(city):
    """
    1: The Researcher (Tavily)
    Searches the web and returns raw text.
    """
    print(f"\nScanning the web for Christmas markets in {city}...")


    query = f"Christmas markets in {city} 2025 dates locations opening hours and famous food"

    try:
        response = tavily.search(
            query=query,
            search_depth="advanced",
            max_results=3
        )
    except Exception as e:
        return f"Error connecting to Tavily: {e}"

    if not response.get('results'):
        return "No results found."

    context_data = "\n\n".join([
        f"Source: {result['url']}\nContent: {result['content']}"
        for result in response['results']
    ])

    return context_data


def analyze_data(city, raw_data):
    """
    2: The Analyst (Ollama)
    Feeds the raw text into qwen2.5:0.5b to clean it up.
    """
    print(f"Reading data and extracting details for {city}...")

    prompt = f"""
    You are a helpful travel assistant. 
    I will give you raw search results about Christmas Markets in {city}.

    Your goal is to extract the details and format them into a clean guide.
    Ignore unrelated text, ads, or cookies.

    Please format the output exactly like this for each market found:

    ## [Market Name]
    * **Dates:** [Start Date] - [End Date]
    * **Location:** [Address or Area]
    * **Opening Hours:** [Times if available, else "Not specified"]
    * **Must-Try Food:** [Mention specific foods found in text]
    * **Description:** [A 1-sentence summary of the vibe]

    Here is the raw data found on the web:
    {raw_data}
    """

    try:
        response = ollama.chat(model=OLLAMA_MODEL, messages=[
            {'role': 'user', 'content': prompt},
        ])
        return response['message']['content']
    except Exception as e:
        return f"Error connecting to Ollama: {e}. Is 'ollama serve' running?"


if __name__ == "__main__":
    while True:
        city_input = input("\n Enter a city (or 'quit'): ")
        if city_input.lower() == 'quit':
            break

        raw_text = search_markets(city_input)

        if "Error" in raw_text:
            print(raw_text)
        else:
            final_guide = analyze_data(city_input, raw_text)


            print("\n" + "=" * 40)
            print(f"AI GUIDE: {city_input.upper()}")
            print("=" * 40)
            print(final_guide)