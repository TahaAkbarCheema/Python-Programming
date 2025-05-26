# ----------------------------------- Assignment # 5 --------------------------------------------

# NAME : Taaha Akbar
# ROLL NO:  PIAIC 204780

# ------------------------------Question-1-------------------
# Palindrome Check
# Write a program that takes a string input from the user and prints whether it is a palindrome (a string that reads the same forwards and backwards). Test the code with twi cases one where the input string is a palindrome and the other where it is not a palindrome.

inputString= input("Enter your String : ")
reversedString = inputString[::-1]
print({True: "Palindrome", False: "Not a palindrome"}[reversedString == inputString])
# print(reversedString==inputString)

# ------------------------------Question-2-------------------
# Formatted Table
# Create a list of tuples where each tuple contains an item name (string) and its price (float).First print the list and then Use a for loop to print each item and its price along with serial number, aligned using the tab escape character.

items = [ ("Apple", 35), ("Mango", 50), ("Banana", 45), ("Orange", 70)]
print(items)
print("\nSr.No\tItem\tPrice")
for i,(name,price) in enumerate(items, start=1):
    print(f"{i}\t{name}\t{price}")

# ------------------------------Question-3-------------------
#  Vowel Counter
# Given a string sentence, write a program that counts and print how many vowels it contains.
# print the original string
# print the count of vowels
# Vowel Counter
# Vowel Counter

sentence = "Hello How Are YOU"
vowels = "aeiouAEIOU"
vowelsContained = []

for char in sentence:
    [vowelsContained.append(char)] * (char in vowels)

print(sentence)
print(f"Vowels found: {vowelsContained}")
print(f"Total Vowels Count Contained in string is: {len(vowelsContained)}")

# ------------------------------ Question-4 -------------------
# Discount Calculator
# You have a list of product prices (floats), e.g. [19.99, 5.50, 100.0]. Apply a 15% discount to each price and store the new prices in a separate list. Then print original list, discounted list and each original and discounted price side by side.

# Original prices
original_prices = [19.99, 5.50, 100.0]

discounted_prices = [price * 0.85 for price in original_prices]

# Print original and discounted lists
print("Original Prices:", original_prices)
print("Discounted Prices:", discounted_prices)

print("\nOriginal\tDiscounted")
for orig, disc in zip(original_prices, discounted_prices):
    print(f"{orig}\t\t{disc}")

# ------------------------------ Question-5-------------------
#  Phone Number Formatter
# You have a list of 11-digit strings like ["03123456789", "03001234567"]. Convert each into the format "+92-XXX-XXXXXXX" and print them. Print Original and Formatted number side by side.

items = ["03006776669", "03226776669"]
formattedString=[]
for item in items:
    formatted = f"+92-{item[1:4]}-{item[4:11]}"
    formattedString.append(formatted)
    print(f"+92-{item[1:4]}-{item[4:11]}")

print("\nOrigional\t\tFormattted")
for  orig, format in zip(items, formattedString):
    print(f"{orig}\t\t{format}")

#  ------------------------------ Question-6-------------------
# Score Statistics
# You have a tuple of exam scores, e.g. (72, 85, 91, 58, 76).
# print the provided tuple
# Convert it to a list and print it.
# Compute and print the minimum, maximum, and average score.

examScores = (72, 85, 91, 58, 76) 
print(examScores)
examScoresList =list(examScores)
print(examScoresList)

total = sum(examScoresList)
minimum = min(examScoresList)
maximum = max(examScoresList)
average = total / len(examScoresList)

print(f"Minimum score: {minimum}")
print(f"Maximum score: {maximum}")
print(f"Average score: {average}")

#  ------------------------------ Question-7-------------------
# Reverse Each Word in a Sentence
# Given a sentence string, reverse each word individually but keep the word order.
# print the original sentence
# print the formatted sentence

sentence = "Hello how are you"
print("Original Sentence:", sentence)
# Reverse each word but keep the order
reversed_words = [word[::-1] for word in sentence.split()]
formatted_sentence = ' '.join(reversed_words)
print("Formatted Sentence:", formatted_sentence)

#  ------------------------------ Question-8-------------------
# Running Sum List
# From a given list create a list where each element is the sum of all previous elements (inclusive). Print both the lists.

initialList = [1,2,3,4,5,6]
finalList =[]
total =0
for i in initialList:
    total+=i
    finalList.append(total)

print(initialList)
print(finalList)

 #  ------------------------------ Question-9-------------------
# Interleave Two Lists
# Combine two equal-length lists into a single one by alternating elements.
# Input: [1, 2, 3] and ['a', 'b', 'c']
# Output: [1, 'a', 2, 'b', 3, 'c']
# Print all three lists.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
interleavedList = []

for x, y in zip(list1, list2):
    interleavedList.append(x)
    interleavedList.append(y)

print("List 1:", list1)
print("List 2:", list2)
print("Interleaved List:", interleavedList)

#  ------------------------------ Question-10-------------------
# Repeat Letters
# Given a string, return a new string where each letter is repeated twice. Print both the strings

givenString ="1,2,3,4,5"
newString = ""

for x in givenString:
    newString+=x*2

print(f"Given String : {givenString}")
print(f"New String : {newString}")

########------------------------------------------ print("THANK YOU") ------------------------------------------