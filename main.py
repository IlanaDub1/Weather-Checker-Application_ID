import streamlit as st
import requests


# Function to get weather data
def get_weather(city):
    api_key = "18913edae72bac8bfca2f89df65a99a5"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(complete_url)
    return response.json()


# Streamlit UI
st.title("Weather App")
name = st.text_input('Enter your name', '')
if name:
    st.write(f'Hello {name}, welcome to the weather app!')

city = st.text_input("Enter city name:")

if st.button("Get Weather"):
    data = get_weather(city)

    if data.get("cod") != "404":
        main = data.get("main", {})
        temperature = main.get("temp", "N/A")
        humidity = main.get("humidity", "N/A")
        weather_description = data.get("weather", [{}])[0].get("description", "N/A")

        st.write(f"Temperature: {temperature}°C")
        st.write(f"Humidity: {humidity}%")
        st.write(f"Weather Description: {weather_description}")
    else:
        st.write("City Not Found!")
