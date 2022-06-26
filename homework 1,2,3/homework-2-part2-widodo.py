# Audrey Nika Widodo
# June 12 2022
# Homework 2, Part 2

# PART ONE LISTS
# 1) Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order
countries = ['Pakistan', 'Japan', 'Australia', 'Indonesia',
             'United Kingdom', 'Switzerland', 'Belgium']

# 2) Using a for loop, print each element of the list
for country in countries:
    print(country)

# 3) Sort the list permanently.
countries = sorted(countries)
print(countries)

# 4) Display the first element of the list.
print(countries[0])

# 5) Display the second-to-last element of the list.
print(countries[-2])

# 6) Delete one of the countries from the list using its name.
countries.remove('Japan')

# 7) Using a for loop, print each country's name in all caps.
for country in countries:
    print(country.upper())

# PART TWO DICTIONARIES
# 1) Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'.
# Pick a tree from: https://en.wikipedia.org/wiki/List_of_trees

tree = {
    'name': 'Angel Oak',
    'species': 'southern live oak',
    'age': 450,
    'location_name': 'Johns Island, South Carolina, US',
    'latitude': 32.4302,
    'longitude': -80.0450
}

# 2) Print the sentence "{name} is a {years} year old tree that is in {location_name}"

nameTree = tree.get('name')
years = tree.get('age')
location_name = tree.get('location_name')

print(nameTree, "is a", years, "year old tree that is in", location_name)

# 3) The coordinates of New York City are 40.7128° N, 74.0059° W. Check to see if the tree is south of NYC, and print
# "The tree {name} in {location} is south of NYC" if it is.
# If it isn't, print "The tree {name} in {location} is north of NYC"

treeLatitude = tree.get('latitude')
treeLongitude = tree.get('longitude')

nycLatitude = 40.7128
nycLongitude = -80.0450

if nycLatitude > treeLatitude:
    print("The tree", nameTree, "in", location_name, ", is SOUTH of NYC")
else:
    print("The tree", nameTree, "in", location_name, ", is NORTH of NYC")

# 4) Ask the user how old they are. If they are older than the tree, display "you are {XXX} years older than {name}."
# If they are younger than the tree, display "{name} was {XXX} years old when you were born."

userAge = int(input("Please enter your age: "))

while userAge <= 0:
    userAge = int(input("Please enter a positive number for your age: "))

if userAge < years:
    treeTotalYearsOlder = years - userAge
    print(nameTree, "was", treeTotalYearsOlder, "years old when you were born.")
else:
    userTotalYearsOlder = userAge - years
    print("You are", userTotalYearsOlder, "years older than", nameTree, "tree")

# PART TWO LISTS OF DICTIONARIES
# 1) Make a list of dictionaries of five places across the world
# - (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago.
# Each dictionary should include each city's name and latitude/longitude (see note above).

worldPlaces = {
    'Moscow': 55.7558,
    'Tehran': 35.7219,
    'Falkland Islands': -51.7963,
    'Seoul': 37.5665,
    'Santiago': -33.4489
}

# 2) Loop through the list, printing each city's name and whether it is above or below the equator
# (How do you know? Think hard about the latitude.)
# When you get to the Falkland Islands, also display the message
# "The Falkland Islands are a biogeographical part of the mild Antarctic zone,"
for name, latitude in worldPlaces.items():
    if latitude > 0:
        print(name, "is above the equator")
    elif latitude < 0:
        print(name, "is below the equator")
    else:
        print("The place is on the equator")
    if name == 'Falkland Islands':
        print("The Falkland Islands are a biogeographical part of the mild Antarctic zone.")

# 3) Loop through the list, printing whether each city is
# north of south of your tree from the previous section.

for name, latitude in worldPlaces.items():
    if latitude > treeLatitude:
        print(name, "is North of the", nameTree)
    elif latitude < treeLatitude:
        print(name, "is South of the", nameTree)
    else:
        print(name, "and", nameTree, "are at the same place")