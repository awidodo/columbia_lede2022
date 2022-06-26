# Audrey Widodo
# 8 June 2022
# Homework 1

#Prompt the user for their year of birth
birthYear = int(input("Please enter your year of birth: "))
while birthYear >= 2022:
    birthYear = int(input("Please enter your year of birth: "))

#How old the user is
age = 2022 - birthYear
print("How old the user is: " + str(age))

# How many times the user's heart has beaten
userHeartbeat = (35000000 * birthYear) // 1000000
print("How many times the user's heart has beaten: " + str(userHeartbeat) + " million")

# How many times a blue whale's heart has beaten
ageMinutes = age * 525600
whaleHeartbeat = (ageMinutes * 11) // 1000000
print("How many times a blue whale's heart has beaten: " + str(whaleHeartbeat) + " million")

# How many times a rabbit's heart has beaten
# If the answer to rabbit heartbeats is more than a million, say "XXX million" instead of the very long raw number
rabbitHeartbeat = (ageMinutes * 130) // 1000000
print("How many times a rabbit's heart has beaten: " + str(rabbitHeartbeat) + " million")

# How old they are in Venus years
venusAge = age // 0.615
print("How old they are in Venus years: " + str(venusAge))

# How old they are in Neptune years
neptuneAge = age / 165
print("How old they are in Neptune years: " + str(neptuneAge))

# Whether they are the same age as you, older or younger
# If older or younger, how many years difference
myAge = 23
if age < myAge:
    print("User is YOUNGER than me by " + str(myAge - age) + " years")
elif age == myAge:
    print("User is the SAME age as me")
else:
    print("User is OLDER than me by " + str(age - myAge) + " years")

#  If they were born in an even or odd year
if (birthYear % 2) == 0:
    print("User was born on " + str(birthYear) + " which is an EVEN year")
else:
    print("User was born on " + str(birthYear) + " which is an ODD year")

# How many times there has been a president from the Democratic Party in office since they were born (1960 onward, and each president only counts once)
count = 0
if birthYear >= 1961 and birthYear <= 1969:
    count += 2
elif birthYear >= 1977 and birthYear < 1993:
    count += 3
elif birthYear >= 1993 and birthYear < 2009:
    count += 4
elif birthYear >= 2009 and birthYear < 2017:
    count += 5
elif birthYear >= 2021:
    count += 6
print("How many times there has been a president from the Democratic Party in office since they were born: " + str(count))

# Which US President was in office when they were born (1960 onward)
if birthYear >= 1953 and birthYear < 1961:
    print("When you were born the U.S. President was Dwight D. Eisenhower")
elif birthYear >= 1961 and birthYear < 1963:
    print("When you were born the U.S. President was John F. Kennedy")
elif birthYear >= 1963 and birthYear < 1969:
    print("When you were born the U.S. President was Lyndon B. Johnson")
elif birthYear >= 1969 and birthYear < 1974:
    print("When you were born the U.S. President was Richard Nixon")
elif birthYear >= 1974 and birthYear < 1977:
    print("When you were born the U.S. President was Gerald Ford")
elif birthYear >= 1977 and birthYear < 1981:
    print("When you were born the U.S. President was Jimmy Carter")
elif birthYear >= 1981 and birthYear < 1989:
    print("When you were born the U.S. President was Ronald Reagan")
elif birthYear >= 1989 and birthYear < 1993:
    print("When you were born the U.S. President was George H.W. Bush")
elif birthYear >= 1993 and birthYear < 2001:
    print("When you were born the U.S. President was Bill Clinton")
elif birthYear >= 2001 and birthYear < 2009:
    print("When you were born the U.S. President was George W. Bush")
elif birthYear >= 2009 and birthYear < 2017:
    print("When you were born the U.S. President was Barack Obama")
elif birthYear >= 2017 and birthYear < 2021:
    print("When you were born the U.S. President was Donald Trump")
elif birthYear >= 2021:
    print("When you were born the U.S. President is Joe Biden")