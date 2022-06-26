# Audrey Nika Widodo
# 12 June 2022
# Homework 2, Part 1

# PART ONE LISTS
# Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
from re import S
from statistics import mean, median

list = [22, 90, 0, -10, 3, 22, 48]

# Display the number of elements in the list.
print(list)

# Display the 4th element of this list.
print(list[3])

# Display the sum of the 2nd and 4th element of the list.
sum1 = list[1] + list[3]
print(sum1)

# Display the 2nd-largest value in the list.
newList = sorted(list)
print(newList[-2])

# Display the last element of the original unsorted list
print(list[-1])

# Display the sum of all of the numbers divided by two.
totalList = sum(list) / 2
print(totalList)

# Print whether the median or the mean of the numbers is higher
# median calculation
lenList = len(list)
middleNum = lenList // 2
medianList = newList[middleNum]

# mean calculation
meanList = round(sum(list) / len(list))

if meanList > medianList:
    print("The MEAN ", str(meanList),
          " is higher than the MEDIAN", str(medianList))
else:
    print("The MEDIAN ", str(medianList),
          " is higher than the MEAN", str(meanList))

# PART 2 DICTIONARIES
# 1) Sometimes dictionaries are used to describe multiple aspects of a single object.
# Like, say, a movie. Define a dictionary called movie that works with the following code.

movie = {
    'title': 'Jurassic Park',
    'year': '1993',
    'director': 'Steven Spielberg'}

print("My favorite movie is", movie['title'], "which was released in",
      movie['year'], "and was directed by", movie['director'])

# 2) On the lines after that, add keys to the movie dictionary for budget and revenue
# (you'll use code like movie['budget'] = 1000),
# and print out the difference between the two.
# 3) If the movie cost more to make than it made in theaters, print "That was a bad investment".
# If the film's revenue was more than five times the amount it cost to make, print "That was a great investment."
# Otherwise print "That was an okay investment."

movie['budget'] = 63000000
movie['revenue'] = 104600000000

movieBudget = movie.get('budget')
movieRevenue = movie.get('revenue')

if movieRevenue > movieBudget:
    grossProfit = movieRevenue - movieBudget
    print("That was a great investment.")
elif movieBudget > movieRevenue:
    grossLoss = movieBudget - movieRevenue
    print("That was a bad investment.")
else:
    print("That was an okay investment.")

# 4) Sometimes dictionaries are used to describe the same aspects of many different objects. 
# Make ONE dictionary that describes the population of the boroughs of NYC. 
# Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m, Queens has 2.3m and Staten Island has 470,000. 
# (Tip: keeping it all in either millions or thousands is a good idea)

popNYC = {
    'Manhattan' : 1600000,
    'Brooklyn' : 2600000,
    'Bronx' : 1400000,
    'Queens' : 230000,
    'Staten Island' : 470000
}

# 5) Display the population of Brooklyn.
oneMillion = 1000000
popBrooklyn = popNYC.get('Brooklyn')
totalPopBrooklyn = popBrooklyn / oneMillion
print("Brooklyn's total population is ", totalPopBrooklyn, "million")

# 6) Display the combined population of all five boroughs.
valuesPopNYC = popNYC.values()
sumPopNYC = sum(valuesPopNYC)
totalPopNYC = sumPopNYC / oneMillion
print("Total population of the NYC's five boroughs is", totalPopNYC, "million")

# 7) Display what percent of NYC's population lives in Manhattan.
popManhattan = popNYC.get('Manhattan')
percentManhattan = round((popManhattan / sumPopNYC) * 100 , 2)
print("The percentage of NYC's population that lives in Manhattan is", percentManhattan , "%. ")
