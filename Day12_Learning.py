import os
import requests
from getpass import getpass

from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


# Set OpenAI API key
if not os.getenv("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass(
        "Enter your OpenAI API key: "
    )


# Custom tool: Fetch current weather using a public API
@tool
def get_weather(city: str) -> str:
    """Get the current weather for a city using the Open-Meteo API."""

    try:
        # Convert city name into latitude and longitude
        geo_response = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={"name": city, "count": 1},
            timeout=10
        )
        geo_response.raise_for_status()
        geo_data = geo_response.json()

        if not geo_data.get("results"):
            return f"Could not find the city: {city}"

        location = geo_data["results"][0]
        latitude = location["latitude"]
        longitude = location["longitude"]
        city_name = location["name"]

        # Fetch current weather
        weather_response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
            },
            timeout=10
        )
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        current = weather_data["current"]

        return (
            f"Weather in {city_name}: "
            f"Temperature: {current['temperature_2m']}°C, "
            f"Humidity: {current['relative_humidity_2m']}%, "
            f"Wind speed: {current['wind_speed_10m']} km/h"
        )

    except requests.RequestException as error:
        return f"Weather API request failed: {error}"


# Initialize LLM
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# Create agent with the custom API tool
agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt=(
        "You are a helpful assistant. "
        "Use the get_weather tool when the user asks about weather. "
        "Summarize the returned weather information clearly."
    )
)


# Interact with the agent
while True:
    question = input(
        "\nAsk about the weather (or type 'exit'): "
    ).strip()

    if question.lower() == "exit":
        break

    try:
        result = agent.invoke({
            "messages": [
                {"role": "user", "content": question}
            ]
        })

        print("\nAgent response:")
        print(result["messages"][-1].content)

    except Exception as error:
        print(f"An error occurred: {error}")