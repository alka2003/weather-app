import argparse
from utils.weather import get_weather, get_forecast
from utils.display import display_current, display_forecast
from utils.map import generate_map

def main():
    parser = argparse.ArgumentParser(description="Advanced Weather CLI App")
    parser.add_argument("city", help="City to fetch weather for")
    parser.add_argument("--no-map", action="store_true", help="Don't generate map")
    args = parser.parse_args()

    city = args.city
    current = get_weather(city)
    forecast = get_forecast(city)

    display_current(current)
    display_forecast(forecast)

    if not args.no_map:
        coords = current["coord"]
        generate_map(coords["lat"], coords["lon"], city)
        print("✅ Map saved as weather_map.html")

if __name__ == "__main__":
    main()
