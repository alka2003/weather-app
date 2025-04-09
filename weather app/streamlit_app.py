import streamlit as st
from utils.weather import get_weather, get_forecast, kelvin_to_celsius
from datetime import datetime
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Weather App", layout="centered")
st.title("🌦️ Weather Dashboard")

city = st.text_input("Enter a city")

if city:
    try:
        data = get_weather(city)
        st.subheader(f"Current Weather in {data['name']}")
        st.write(f"**Temperature:** {kelvin_to_celsius(data['main']['temp'])} °C")
        st.write(f"**Feels Like:** {kelvin_to_celsius(data['main']['feels_like'])} °C")
        st.write(f"**Humidity:** {data['main']['humidity']}%")
        st.write(f"**Description:** {data['weather'][0]['description'].title()}")

        forecast = get_forecast(city)
        st.subheader("Upcoming Forecast")
        for entry in forecast["list"][:5]:
            dt = datetime.fromtimestamp(entry["dt"])
            temp = kelvin_to_celsius(entry["main"]["temp"])
            desc = entry["weather"][0]["description"]
            st.write(f"{dt.strftime('%Y-%m-%d %H:%M')} - {temp}°C - {desc}")

        # Show map
        coord = data["coord"]
        m = folium.Map(location=[coord["lat"], coord["lon"]], zoom_start=10)
        folium.Marker([coord["lat"], coord["lon"]], tooltip=city).add_to(m)
        st_folium(m, width=700, height=450)

    except Exception as e:
        st.error(f"Failed to fetch weather: {e}")
