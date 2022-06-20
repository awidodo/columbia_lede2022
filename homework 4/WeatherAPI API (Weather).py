#!/usr/bin/env python
# coding: utf-8

# # WeatherAPI (Weather)
# 
# Answer the following questions using [WeatherAPI](http://www.weatherapi.com/). I've added three cells for most questions but you're free to use more or less! Hold `Shift` and hit `Enter` to run a cell, and use the `+` on the top left to add a new cell to a notebook.
# 
# Be sure to take advantage of both the documentation and the API Explorer!
# 
# ## 0) Import any libraries you might need
# 
# - *Tip: We're going to be downloading things from the internet, so we probably need `requests`.*
# - *Tip: Remember you only need to import requests once!*

# In[22]:


import requests
import json


# In[ ]:





# ## 1) Make a request to the Weather API for where you were born (or lived, or want to visit!).
# 
# - *Tip: The URL we used in class was for a place near San Francisco. What was the format of the endpoint that made this happen?*
# - *Tip: Save the URL as a separate variable, and be sure to not have `[` and `]` inside.*
# - *Tip: How is north vs. south and east vs. west latitude/longitude represented? Is it the normal North/South/East/West?*
# - *Tip: You know it's JSON, but Python doesn't! Make sure you aren't trying to deal with plain text.* 
# - *Tip: Once you've imported the JSON into a variable, check the timezone's name to make sure it seems like it got the right part of the world!*

# In[25]:


url = "http://api.weatherapi.com/v1/current.json?key=d724982c44574de8b3d31655222006&q=Jakarta&aqi=no"
response = requests.get(url)
data = response.json()


# In[34]:


print("Name of City:", data['location']['name'])


# In[36]:


print("Timezone:", data['location']['tz_id'])


# ## 2) What's the current wind speed? How much warmer does it feel than it actually is?
# 
# - *Tip: You can do this by browsing through the dictionaries, but it might be easier to read the documentation*
# - *Tip: For the second half: it **is** one temperature, and it **feels** a different temperature. Calculate the difference.*

# In[42]:


print(data['current'])


# In[44]:


print("Current Wind Speed:", data['current']['wind_mph'], "mph or", data['current']['wind_kph'],"kph" )


# In[49]:


feelsCelsius = data['current']['feelslike_c']
tempCelsius = data['current']['temp_c']

if feelsCelsius > tempCelsius:
    diff1 = feelsCelsius - tempCelsius
    print("It feels warmer than the actual temperature by", round(diff1,2),"degrees celsius")
else:
    diff2 = tempCelsius - feelsCelsius
    print("It feels colder than the actual temperature by", round(diff2,2), "degrees celsius")
    


# ## 3) What is the API endpoint for moon-related information? For the place you decided on above, how much of the moon will be visible tomorrow?
# 
# - *Tip: Check the documentation!*
# - *Tip: If you aren't sure what something means, ask in Slack*

# In[51]:


apiEndpointMoon = "http://api.weatherapi.com/v1/astronomy.json?key=d724982c44574de8b3d31655222006&q=Jakarta&dt=2022-06-20"
response = requests.get(apiEndpointMoon)
data = response.json()


# In[59]:


print("The moon will be visible by:", data['astronomy']['astro']['moon_illumination'], "in Jakarta.")


# In[ ]:





# ## 4) What's the difference between the high and low temperatures for today?
# 
# - *Tip: When you requested moon data, you probably overwrote your variables! If so, you'll need to make a new request.*

# In[90]:


url = "http://api.weatherapi.com/v1/forecast.json?key=d724982c44574de8b3d31655222006&q=Jakarta&days=1&aqi=no&alerts=no"
response = requests.get(url)
data = response.json()
print(data['forecast']['forecastday'][0]['day'])


# In[92]:


maxtempC = data['forecast']['forecastday'][0]['day']['maxtemp_c']
mintempC = data['forecast']['forecastday'][0]['day']['mintemp_c']

diff = round(maxtempC - mintempC,2)

print("The highest temperature is", maxtempC, "degrees celsius and the lowest temperature is", mintempC, "degrees celsius and the difference is", diff, "degrees celsius.")


# ## 4.5) How can you avoid the "oh no I don't have the data any more because I made another request" problem in the future?
# 
# What variable(s) do you have to rename, and what would you rename them?

# data and response would have to be renamed with a more specific variable
# 
# i.e.
# dataLocation would have responseLocation
# dataForecast would have responseForecast

# In[ ]:





# ## 5) Go through the daily forecasts, printing out the next three days' worth of predictions.
# 
# I'd like to know the **high temperature** for each day, and whether it's **hot, warm, or cold** (based on what temperatures you think are hot, warm or cold).
# 
# - *Tip: You'll need to use an `if` statement to say whether it is hot, warm or cold.*

# In[120]:


urlForecasts = "http://api.weatherapi.com/v1/forecast.json?key=d724982c44574de8b3d31655222006&q=Jakarta&days=3&aqi=no&alerts=no"
responseForecasts = requests.get(urlForecasts)
dataForecasts = responseForecasts.json()


# In[129]:


date1 = dataForecasts['forecast']['forecastday'][0]['date']
date2 = dataForecasts['forecast']['forecastday'][1]['date']
date3 = dataForecasts['forecast']['forecastday'][2]['date']

print(date1, date2, date3)


# In[134]:


day1 = dataForecasts['forecast']['forecastday'][0]['day']['avgtemp_c']
day2 = dataForecasts['forecast']['forecastday'][1]['day']['avgtemp_c']
day3 = dataForecasts['forecast']['forecastday'][2]['day']['avgtemp_c']

if day1 < 20:
    print("On", date1, "the temperature is", day1, "degrees celsius which will be cold")
elif day1 <30:
    print("On", date1, "the temperature is", day1, "degrees celsius which will be warm")
else:
    print("On", date1, "the temperature is", day1, "degrees celsius which will be hot")
    
if day2 < 20:
    print("On", date2, "the temperature is", day2, "degrees celsius which will be cold")
elif day2 <30:
    print("On", date2, "the temperature is", day2, "degrees celsius which will be warm")
else:
    print("On", date2, "the temperature is", day2, "degrees celsius which will be hot")
    
if day3 < 20:
    print("On", date3, "the temperature is", day3, "degrees celsius which will be cold")
elif day3 <30:
    print("On", date3, "the temperature is", day3, "degrees celsius which will be warm")
else:
    print("On", date3, "the temperature is", day3, "degrees celsius which will be hot")
    


# ## 5b) The question above used to be an entire week, but not any more. Try to re-use the code above to print out seven days.
# 
# What happens? Can you figure out why it doesn't work?
# 
# * *Tip: it has to do with the reason you're using an API key - maybe take a look at the "Air Quality Data" introduction for a hint? If you can't figure it out right now, no worries.*

# In[135]:


date1 = dataForecasts['forecast']['forecastday'][0]['date']
date2 = dataForecasts['forecast']['forecastday'][1]['date']
date3 = dataForecasts['forecast']['forecastday'][2]['date']
date4 = dataForecasts['forecast']['forecastday'][3]['date']


# 

# In[ ]:





# ## 6) What will be the hottest day in the next three days? What is the high temperature on that day?

# In[156]:


forecast3days = {date1 : day1, date2 : day2, date3 : day3}

for hottest in forecast3days:
    if max(forecast3days.values()) > forecast3days.values():
        print(hottest, max(forecast3days.values()))


# In[ ]:





# In[ ]:





# ## 7) What's the weather looking like for the next 24+ hours in Miami, Florida?
# 
# I'd like to know the temperature for every hour, and if it's going to have cloud cover of more than 50% say "{temperature} and cloudy" instead of just the temperature. 
# 
# - *Tip: You'll only need one day of forecast*

# In[184]:


urlMiami = "http://api.weatherapi.com/v1/forecast.json?key=d724982c44574de8b3d31655222006&q=Miami&days=1&aqi=no&alerts=no"
responseMiami = requests.get(urlMiami)
dataMiami = responseMiami.json()

print(dataMiami['forecast']['forecastday'][0]['hour'][0])


# In[193]:


i = 0
while i < 24:
    print(dataMiami['forecast']['forecastday'][0]['hour'][i]['time'], 
         dataMiami['forecast']['forecastday'][0]['hour'][i]['temp_c'] , "degrees celsius")
    if dataMiami['forecast']['forecastday'][0]['hour'][i]["cloud"] > 50:
        print("and cloudy")
    i += 1


# In[ ]:





# ## 8) For the next 24-ish hours in Miami, what percent of the time is the temperature above 85 degrees?
# 
# - *Tip: You might want to read up on [looping patterns](http://jonathansoma.com/lede/foundations-2017/classes/data%20structures/looping-patterns/)*

# In[199]:


i = 0
total = 0
temp = dataMiami['forecast']['forecastday'][0]['hour'][i]['temp_c']
for temp in dataMiami:
    if temp > 85:
        total += temp
        print(temp)


# In[ ]:





# In[ ]:





# ## 9) How much will it cost if you need to use 1,500,000 API calls?
# 
# You are only allowed 1,000,000 API calls each month. If you were really bad at this homework or made some awful loops, WeatherAPI might shut down your free access. 
# 
# * *Tip: this involves looking somewhere that isn't the normal documentation.*

# It would cost $4/month

# In[ ]:





# ## 10) You're too poor to spend more money! What else could you do instead of give them money?
# 
# * *Tip: I'm not endorsing being sneaky, but newsrooms and students are both generally poverty-stricken.*

# I would have advertisments and endorsements for my work.
