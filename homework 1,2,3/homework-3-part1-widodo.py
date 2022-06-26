# Audrey Nika Widodo
# June 13 2022
# Homework 3

# PART ONE: Pokemon API
# Using the Pokemon API (Links to an external site.)
from itertools import count
from operator import index
import requests
import json

# What is the URL to the documentation?
response = requests.get('https://pokeapi.co/api/v2/')
data = response.json()

# What pokemon has the ID of 55?
#Golduck
pokemon55response = requests.get('https://pokeapi.co/api/v2/pokemon-species/55')
pokemon55data = pokemon55response.json()
print(pokemon55data['name'])

# How tall is that pokemon?
#17
pokemon55response2 = requests.get('https://pokeapi.co/api/v2/pokemon/55')
pokemon55data2 = pokemon55response2.json()
print(pokemon55data2['height'])

# How many versions of Pokemon games have been released?
#34
pokemonVersionResponse = requests.get("https://pokeapi.co/api/v2/version/")
pokemonVersionData = pokemonVersionResponse.json()
print(pokemonVersionData['count'])

# Print out the name of every electric-type pokemon.
dataElectricResponse = requests.get('https://pokeapi.co/api/v2/type/13')
dataElectric = dataElectricResponse.json()
count = 0
for i in dataElectric:
    i = (dataElectric['pokemon'][count]['pokemon']['name'])
    print(i)
    count += 1
    
# What are electric-type Pokemon called in the Korean version of the game?
count2 = 0
for i in dataElectric:
    i = (dataElectric['names'][count2]['language']['name']['name'])
    print(i)
    count2 += 1

# Who has a higher speed stat, Eevee or Pikachu?
pikachuResponse = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
pikachuData = pikachuResponse.json()
pikachuSpeed = pikachuData['stats'][5]['base_stat']

eeveeResponse = requests.get("https://pokeapi.co/api/v2/pokemon/eevee")
eeveeData = eeveeResponse.json()
eeveeSpeed = eeveeData['stats'][5]['base_stat']

if pikachuSpeed > eeveeSpeed:
    print("Pikachu has a higher speed stat")
else:
    print("Eevee has a higher speed stat")