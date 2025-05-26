# # # ----------------------------------- Assignment # 4 --------------------------------------------

# # # NAME : Umair Arshad
# # # ROLL NO:  PIAIC 255935

# # # ---------------------------------------------------------{ P A R T # 1 }---------------------------
# # # ------------------------------Question-1-------------------
# # # Q1. Favorite Movie Intro
# # # Ask the user for:
# # # Their name
# # # Their favorite movie

# name = input("Whats your Name  : ")
# movie = input("Which is Your Favourite Movie  : ")
# print(f"{name}'s favourite movie is {movie}")

# # # ------------------------------Question-2-------------------
# # # Ask the user to enter a word.
# # # Print:
# # # The word in uppercase
# # # The word in lowercase
# # # The word in title case

# text = input("Please Enter a Word : ")
# uppercase_text = text.upper()
# print(f"Uppercase : {uppercase_text}")
# lowercase_text =text.lower()
# print(f"Lowercase : {lowercase_text}")
# titlecase_text = text.title()
# print(f"Titlecase : {titlecase_text}")

# # # ---------------------------------Question-3----------------
# # # Convert them to int or float
# # # Print:
# # # Sum
# # # Difference
# # # Product
# # # Quotient

first_No = int (input("Enter 1st No"))
sec_No = int( input("Emter 2nd No"))

sum = first_No + sec_No
difference = first_No - sec_No
product = first_No * sec_No
quotient = first_No % sec_No

print(f"Sum : {sum}")
print(f"Product : {difference}")
print(f"Difference : {product}")
print(f"Quotient : {quotient}")


# # # -------------------------------------------{ P A R T # 1 }---------------------------
# # # -----------------------Question - 4--------------------
# # # Q4. My Friends List
# # # Create a list of 4 friends’ names.
# # # Print each name using a for loop.

# myFriends = ["Ali", "Ahamd", "Umair", "Muhees"]
# for friend in myFriends:
#    print(friend)

# # #   -----------------------Question - 5--------------------
# # Q5. Update Your List
# # Create a list of 3 favorite fruits.
# # Replace the second fruit with another.
# # Add one fruit to the end using .append().
# # Add one to the beginning using .insert(0, ...).
# # Print the list after each change.

# fruits = ["Mango", "Apple", "Banana"]
# print("Initial list:", fruits)

# fruits[1] = "Strawberry"
# print("After replacing second fruit:", fruits)

# fruits.append("Grapes")
# print("After appending a fruit:", fruits)

# fruits.insert(0, "Pineapple")
# print("After inserting at the beginning:", fruits)

# # #   -----------------------Question - 6--------------------
# #  Q6. List Length Reporter
# # Ask the user to enter 5 favorite animals (use input()).
# # Store each animal in a list.
# # After collecting:
#     # Print the total number of animals using len()
#     # Print the first and last animal using indexing

# favorite_animals = []

# for i in range(5):
#     animal = input(f"Enter favorite animal #{i+1}: ")
#     favorite_animals.append(animal)

# print("Total number of animals:", len(favorite_animals))

# print("First animal:", favorite_animals[0])
# print("Last animal:", favorite_animals[-1])

# # #   -----------------------Question - 7--------------------
# # Q7. Print Numbers
# # Use range() and for loop to:

# # Print numbers from 1 to 10
# # Print even numbers from 2 to 20
# # Print multiples of 5 from 5 to 50

# # Print numbers from 1 to 10
# print("Numbers from 1 to 10:")
# for i in range(1, 11):
#     print(i)

# # Print even numbers from 2 to 20
# print("\nEven numbers from 2 to 20:")
# for i in range(2, 21, 2):
#     print(i)

# # Print multiples of 5 from 5 to 50
# print("\nMultiples of 5 from 5 to 50:")
# for i in range(5, 51, 5):
#     print(i)


# # #   -----------------------Question - 8--------------------
# # Q8. Squares Table
# # Use a for loop to print square numbers from 1 to 10:
# # 1 squared is 1  
# # 2 squared is 4  
# # 3 squared is 9  
# # ...  
# # 10 squared is 100 

# # # Print square numbers from 1 to 10
# for i in range(1, 11):
#     print(f"{i} squared is {i ** 2}")

# # #   -----------------------Question - 9--------------------
# # Q9. Make a List of Cubes
# # Use list comprehension to generate cubes of numbers 1–5.
# # Print the list.
# # # Output:
# # [1, 8, 27, 64, 125]

# # Generate cubes using list comprehension
# cubes = [x**3 for x in range(1, 6)]
# print(cubes)

# # #   -----------------------Question - 10--------------------
# # Q10. Top 3 Movies
# # Ask the user to enter 5 movie names using input().

# # Store them in a list.

# # Print:

# # The first 3 movies using slicing
# # The last 2 movies using slicing

# # Create an empty list to store movie names
# movies = []

# # # Ask the user to enter 5 movie names
# for i in range(5):
#     movie = input(f"Enter movie # {i+1}: ")
#     movies.append(movie)

# # # Print the first 3 movies using slicing
# print("First 3 movies:", movies[:3])

# # # Print the last 2 movies using slicing
# print("Last 2 movies:", movies[-2:])

# # #   -----------------------Question - 11--------------------
# # Q11. 🧑‍🏫 Top Students
# # Ask the user to enter names of 5 students using input() (one by one).

# # Store the names in a list.

# # Then:

# # Print a greeting for each student using a for loop.

# # Print only the top 3 students using slicing.

# # Copy the list using [:], then:

# # Add 2 new names to the copied list using .append()
# # Print both the original and the new list to show that the original is unchanged.

# # Step 1: Collect 5 student names from the user
# students = []
# for i in range(5):
#     name = input(f"Enter the name of student #{i+1}: ")
#     students.append(name)

# # # Step 2: Print a greeting for each student
# print("\nGreetings:")
# for student in students:
#     print(f"Hello, {student}!")

# # # Step 3: Print only the top 3 students using slicing
# print("\nTop 3 students:", students[:3])

# # # Step 4: Copy the list using slicing
# new_students = students[:]

# # # Step 5: Add 2 new names to the copied list
# new_students.append("Alice")
# new_students.append("Bob")

# # # Step 6: Print both the original and the new list
# print("\nOriginal list of students:", students)
# print("New list with additional students:", new_students)

# # #   -----------------------Question - 12--------------------
# # Q12. ✈️ Travel Wishlist
# # Create a list of 5 places you want to visit.

# # Print the original list.

# # Print a temporarily sorted list using sorted().

# # Sort the list in reverse alphabetical order using .sort(reverse=True).

# # Use .reverse() twice:

# # First to flip and print the list
# # Then to flip it back and print again

# # Create a list of 5 places to visit
# places = ["Japan", "Iceland", "New Zealand", "Canada", "Norway"]

# # Print the original list
# print("Original list:", places)

# # Print a temporarily sorted list using sorted()
# print("Temporarily sorted list:", sorted(places))

# # Print the original list again to show it’s unchanged
# print("Original list after sorted():", places)

# # Sort the list in reverse alphabetical order
# places.sort(reverse=True)
# print("List sorted in reverse alphabetical order:", places)

# # Use .reverse() to flip the list
# places.reverse()
# print("List after first reverse():", places)

# # Use .reverse() again to flip it back
# places.reverse()
# print("List after second reverse():", places)

# # #   -----------------------Mini Challenge: Name Art Generator--------------------
# # Ask the user to enter their name
# name = input("Enter your name: ")

# # Convert the name to a list of characters
# char_list = list(name)

# # Print each character on a new line using a for loop
# print("\nCharacters in your name:")
# for char in char_list:
#     print(char)

# # Print the first 3 letters
# print("\nFirst 3 letters:", char_list[:3])

# # Print the last 2 letters
# print("Last 2 letters:", char_list[-2:])

# # Print the total number of letters
# print("Total number of letters:", len(char_list))



