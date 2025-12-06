import os

import streamlit as st
import ollama
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

TAVILY_API_KEY = os.getenv('API_TAVILY')
OLLAMA_MODEL = "qwen2.5:0.5b"

st.set_page_config(page_title="Christmas Market Explorer", page_icon="🎄")


def search_markets(city):
    tavily = TavilyClient(TAVILY_API_KEY)

    query = f"Christmas markets in {city} 2025 dates locations opening hours and food"

    try:
        response = tavily.search(query=query, search_depth="advanced", max_results=3)
        if not response.get('results'):
            return None

        return "\n\n".join([
            f"Source: {result['url']}\nContent: {result['content']}"
            for result in response['results']
        ])
    except Exception as e:
        return f"Error: {e}"


def analyze_data(city, raw_data):
    """Feeds web data to the tiny AI model."""
    prompt = f"""
    You are a travel assistant. 
    Summarize this raw data about Christmas Markets in {city} into a clean list.

    Format nicely with Markdown:
    ## [Market Name]
    * **Dates:** ...
    * **Location:** ...
    * **Food:** ...
    * **Description:** ...

    Raw Data:
    {raw_data}
    """

    response = ollama.chat(model=OLLAMA_MODEL, messages=[
        {'role': 'user', 'content': prompt},
    ])
    return response['message']['content']


# UI
st.title("🎄 Christmas Market Explorer")
st.write("Enter a city to find the best fairs, dates, and food for 2024.")

city = st.text_input("Which city do you want to visit?", placeholder="e.g. Prague, Berlin, NYC")

if st.button("Explore Markets"):
    if not city:
        st.warning("Please enter a city name first!")
    else:
        with st.spinner(f"Searching the web for {city} markets..."):
            raw_text = search_markets(city)

        if not raw_text:
            st.error("No info found. Try a major city please!")
        elif "Error" in raw_text:
            st.error(raw_text)
        else:
            with st.spinner("AI is reading and formatting the guide..."):
                final_guide = analyze_data(city, raw_text)

            st.success("Guide Generated!")
            st.markdown("---")
            st.markdown(final_guide)