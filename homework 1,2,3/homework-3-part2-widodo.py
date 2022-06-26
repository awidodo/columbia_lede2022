# Audrey Nika Widodo
# June 13 2022
# Homework 3

# PART TWO: Weather API
# Register for an account at weatherapi.com. 
# What is the URL to the documentation?
import requests
import json

response = requests.get('http://api.weatherapi.com/v1')
data = response.json()

# Make a request for the current weather where you are born, or somewhere you've lived.

# Print out the country this location is in.

# Print out the difference between the current temperature and how warm it feels. Use "It feels ___ degrees colder" or "It feels ___ degrees warmer," not negative numbers.

# What's the current temperature at Heathrow International Airport? Use the airport's IATA code to search.
# What URL would I use to request a 3-day forecast at Heathrow?
# Print the date of each of the 3 days you're getting a forecast for.
# Print the maximum temperature of each of the days.
# Print the day with the highest maximum temperature.
