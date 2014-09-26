#Inclass4 Part 2

"""What does the code below do? Run the code in iPython.
For each line of code, add an explanation
through a comment."""

#PART I
#This prints out the string in the quotes
print "I will now count my chickens:"
#This prints the string "Hens" and prints out the value of 25 + 30 / 6, as well as the string "Roosters"
#and the value of 100 - 25 * 3 % 4
print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4
#This prints out the string "Now I will count the eggs"
print "Now I will count the eggs:"
#This prints out the value of the function given
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
#This prints out the string given below.
print "Is it true that 3 + 2 < 5 - 7?"
#This prints out the boolean value of 3 + 2 < 5 - 7, which is false
print 3 + 2 < 5 - 7
#This prints out the string given, and the value of 3 + 2, which is 5, then it prints the second string
#and the value of 5 - 7, which is -2
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7
#This prints the string given
print "Oh, that's why it's False."
#This prints out the string provided
print "How about some more."
#This prints out the string "Is it greater?" then the boolean value of the expression, which is true
#Then it prints out the string "Is it greater or equal?" then the boolean value, which is also true
#Then it prints out the string "Is it less or equal?" then the boolean value, which is false
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

#PART II
#This creates a string with the days of the week in a variable named days
#Then it creates a string with the months in a variable named months
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
#This prints out the string "Here are the days: " then the value stored in days
#Then it prints out the string "Here are the months: " then the value stored in months
print "Here are the days: ", days
print "Here are the months: ", months

#PART III
#This creates three different lists named the_count, fruits, and change, one with integers, one with strings
#and one with integers and strings
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#This uses a for loop to iterate through the values in the_count and print out the string
#"This is the count" along with each value in the list. The %d means the values in the list are integers
for number in the_count:
    print "This is count %d" % number

#This uses a for loop to iterate through the values in fruits, then print out the string "A fruit of type"
#then the value in the list. The %s means the values in the list are stings
for fruit in fruits:
    print "A fruit of type: %s" % fruit

#This uses a for loop to iterate through the values in change, then print out the string "I got", then
#the value associated in list change
# Use %r format when you don't know
#if the elements are strings or integers
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
#Creates and empty list named elements
elements = []

# then use the range function to do 0 to 5 counts
#This uses a for loop to iterate 5 times, printing the string "Adding %d (which is the value 0-5) to the list"
#then it adds that value to the list elements
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

#This uses a for loop to iterate through the values in list elements, then prints the string "Element was: ", then
#the value associated in the list elements
for i in elements:
    print "Element was: %d" % i

#Lecture 14
#Intro to Python III


#Working with Lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"

#print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "The 'stuff' list: ", stuff

#Working with Dictionaries

d1 = {'a': 'some value', 'b': [1, 2, 3, 4]} #can contain lists

#Access an element by key
print d1['a']

#Add an element (a pair key: value) to the dict
d1[7] = 'an integer'
print d1

#Check if the dict contains a certain key
print "b" in d1

#Delete a value

del d1[7]
print d1

#Use functions defined for dictionaries
print "Keys", d1.keys()
print "Values", d1.values()

#Inclass4 Part 3

"""What does the code below do? Run the code in iPython.
For each line of code, add an explanation
through a comment."""

#PART I

#Use the code from Lecture14.py to create and change the 
#'stuff' list; Then comment on each line of the code below
#what it does, and what the result is

print stuff[1]
#This prints the item in the list at index 1
print stuff[-1] 
#This prints out the item at index 2
print stuff.pop()
#This prints the item at the current index, and removes it from the list
print ' '.join(stuff) 
#This prints the whole list, joined with more_stuff, separated by a space
print '#'.join(stuff[3:5]) 
#This prints out the values at index 3 and five, separated by a # sign

#PART II

#Create comments where marked with # to explain the code below

#This creates a dictionary named states, with five states and their abbreviations
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#This creates a dictionary named cities, with three state abbreviations and the capitol of that state
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#This adds two values to the cities dictionary
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#This prints a line with ten "-" symbols
print '-' * 10
print "NY State has: ", cities['NY']
#This prints the string "NY State has: ", then the value of cities associated with 'NY', which is "New York", the capitol
print "OR State has: ", cities['OR']
#This prints the string "OR State has: ", then the value of cities associated with 'OR', which is "Portland", the capitol

#This prints a line with ten "-" symbols
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
#This prints the string "Michigan's abbreviation is: ", then the value of states associated with 'Michigan', which is MI
print "Florida's abbreviation is: ", states['Florida']
#This prints the string "Florida's abbreviation is: ", then the value of states associated with 'Florida', which is FL

#This prints a line with ten "-" symbols
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
#This prints out the string given, then searches for the value of states associated with Michigan, which is MI, then uses that index to search through
#cities, which prints the result Detroit
print "Florida has: ", cities[states['Florida']]
#This prints out the string given, then searches for value of states with index 'Florida', which return FL, then uses that to search through cities,
#which returns Jacksonville, and prints that value

#This prints a line with ten "-" symbols
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)
#This uses a for loop to iterate through state dictionary, then prints out "%s (which is the state) is abbreviated %s (which is the abbreviation)". The %s means
#the value is a string

#This prints a line with ten "-" symbols
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)
#This uses a for loop to iterate through cities dictionary, then prints out "%s (which is the abbreviation) has the city %s (which is the city)". The %s means
#the value is a string

#This prints a line with ten "-" symbols
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])
#This uses a for loop to iterate through state dictionary, then prints out "%s (which is the state) state is abbreviated %s (which is the abbreviation) and 
#has city %s (which is the capitol of the state)". The %s means the value is a string



