import config
import urllib.request
import json
from prettytable import PrettyTable
from datetime import datetime
from datetime import timedelta

# Weather fetching program

# Configuration
DARKSKY_LATITUDE = "51.230753"
DARKSKY_LONGITUDE = "5.309764"

# Grab the weather data
response = urllib.request.urlopen("https://api.darksky.net/forecast/" + config.DARKSKY_API_KEY + "/" + DARKSKY_LATITUDE + "," + DARKSKY_LONGITUDE + "?units=si")

# Parse JSON from the response
data = json.load(response)

# Create a new table
table = PrettyTable()

# Setup table headers
table.field_names = ["Day", "Weather", "Temp. min", "Temp. max", "Wind speed", "Summary"]

# Define alignment of the table content
table.align["Weather"] = "r"
table.align["Temp. min"] = "r"
table.align["Temp. max"] = "r"
table.align["Wind speed"] = "r"
table.align["Summary"] = "l"

# Get the daily weather data
dailyWeather = data["daily"]["data"]

# Get the current date
now = datetime.now()

# Get 8 days of weather data
for i in range(0, 8):
    # Add an amount of days accordingly
    day = now + timedelta(days=i)

    # Add the data to the table
    table.add_row([day.strftime("%A"), dailyWeather[i]["icon"].title(), dailyWeather[i]["temperatureMin"], dailyWeather[i]["temperatureMax"], dailyWeather[i]["windSpeed"], dailyWeather[i]["summary"]])

# Print out the table
print(table)
