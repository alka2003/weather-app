import folium

def generate_map(lat, lon, city):
    m = folium.Map(location=[lat, lon], zoom_start=10)
    folium.Marker(
        [lat, lon],
        popup=f"Weather in {city}",
        tooltip=city,
        icon=folium.Icon(color="blue")
    ).add_to(m)
    m.save("weather_map.html")
