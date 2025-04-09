from rich.table import Table
from rich.console import Console
from datetime import datetime
from .weather import kelvin_to_celsius

console = Console()


def display_current(data):
    table = Table(title=f"Current Weather - {data['name']}")
    table.add_column("Parameter")
    table.add_column("Value")

    table.add_row("Weather", data["weather"][0]["description"].title())
    table.add_row("Temperature", f"{kelvin_to_celsius(data['main']['temp'])} °C")
    table.add_row("Feels Like", f"{kelvin_to_celsius(data['main']['feels_like'])} °C")
    table.add_row("Humidity", f"{data['main']['humidity']}%")
    table.add_row("Wind", f"{data['wind']['speed']} m/s")
    table.add_row("Sunrise", datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M"))
    table.add_row("Sunset", datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M"))

    console.print(table)


def display_forecast(data):
    table = Table(title="5-Day Forecast")
    table.add_column("Date")
    table.add_column("Time")
    table.add_column("Temp (°C)")
    table.add_column("Description")

    for entry in data["list"][:10]:  # Show only 10 entries
        dt = datetime.fromtimestamp(entry["dt"])
        temp = kelvin_to_celsius(entry["main"]["temp"])
        desc = entry["weather"][0]["description"].title()
        table.add_row(dt.strftime("%Y-%m-%d"), dt.strftime("%H:%M"), str(temp), desc)

    console.print(table)
