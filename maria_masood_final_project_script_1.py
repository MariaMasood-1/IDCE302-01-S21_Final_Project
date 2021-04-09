# -*- coding: utf-8 -*-
"""Maria_Masood_Final_Project_Script_1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wpl90kq_V8AcD6lGk5SRMqOvDdwd0yon
"""

'''
Assignment title: Final Project Script 1
Date: 04/05/2021
Description: This script scrapes the 5-day weather forecast from the National Weather Service website
and extracts information from detailed forecast listed under the forecast-tombstone class name using the BeautifulSoup library

Input: user inputs desired latitude and longitude in decimal degrees
Outputs: Detailed 5-day weather forecast from the National Weather Service website
'''

# import required libraries
import requests
from bs4 import BeautifulSoup

lat = str(input("Input the latitude in decimal degrees "))   
lon = str(input("Input the longitude in decimal degrees "))  
# Create an empty list to store response
forecast = []

## Provide the latitude and longitude for the location you would like to check the forecast for
## Lat/lon in decimal degrees provided for Worcester, MA


# Create url for the requested location through string concatenation
url = 'https://forecast.weather.gov/MapClick.php?lat='+lat+"&lon="+lon
# Check if the URL exists
# print url

# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

# Locate elements on page to be scraped
# findAll() locates all occurrences of div tag with the given class name
# stores it in the BeautifulSoup object
weather_forecast = soup.findAll("li", {"class": "forecast-tombstone"})

# Loop through the BeautifulSoup object to extract text text from every class instance using .text
# Store results in a list
for i in weather_forecast:
    i = i.text
    forecast.append(i)

# Print list to remove unicode characters
for day in forecast:
  day = day.replace('TuesdayNight', 'Tuesday Night')
  day = day.replace('WednesdayNight', 'Wednesday Night')
  day = day.replace('ThursdayNight', 'Thursday Night')
  day = day.replace('FridayNight', 'Friday Night')
  day = day.replace('CloudyLow', 'Cloudy Low')
  day = day.replace('SunnyHigh', 'Sunny High')
  day = day.replace('ClearLow', 'Clear Low')
  day= day.upper()
  print(day)