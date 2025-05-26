                     #--------------Assignment NO 3------------------  
# Name : Taaha Akbar Cheema
# Roll NO : PIAIC 204780

# --------------------------- Chapter 2 VARIABLES ----------------------
#--------------------------------- { BASICS } ---------------------

# 1). Create a variable called greeting and store any message. Print it.
greeting = "How are you Respected Sir"

# 2). Change the value of greeting to a new message. Print the updated message.
greeting = 1
print(greeting)

# 3). Create two variables first_name and last_name. Combine them into a full name using an f-string.
first_name = "Taaha"
last_name = "Akbar"
print(f"My First Name is {first_name} and last is {last_name}")

# 4). Print a quote along with the author's name using an f-string.
poet_name = "Wasif Ali Wasif"
quote = "badhi manzilon ke musafir chota dil nahi rakhte."
print(f"{poet_name} ---> {quote} ")

# 5).Store a person's name with extra spaces. Strip the spaces before printing
first_space = "     Hello World!"
right_space = "Hello World!     "
between_space = "Hello      World!"
print(first_space.lstrip())
print(right_space.rstrip())
#--------------------------------------- {Intermediate}-------------------------------

# 6).Take a number, add 5, multiply by 2, subtract 3, and print the final result.
number = 3
print(number+5*2-3)

# 7). Create two numbers a and b and print their sum, difference, product, and quotient.
a,b =4,8
sum = a+b
product = a*b
difference = a-b
quiotent = a/b
print (f" Sum : {sum}  Product {product}  Difference {difference} Quiotent{quiotent} ")

# 8). Find the square and cube of a number using the ** operator.
cube = 3
cube = 3**3
square =2*2
print (f"Square : {square}  +  Cube : {cube}")

# 9). Print the sum of three floating-point numbers.
floating_no_1 = -4.998767
floating_no_2 = 7.78
floating_no_3 = 1.78
sum = floating_no_1+floating_no_2+floating_no_3
print(f"Sum of Floating Numbers are : {sum}")

# 10). Assign three variables x, y, z in a single line and print them.
x,y,z =1,2,3
print(x,y,z)

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------Chapter 3 LISTS--------------------------------------------------------------------
#---------------------------------------- {BASICS} ----------------------------------------------------

# 11). Create a list of 5 favorite fruits and print each fruit separately.
fruits_list = ["Orange", 
              "Mango", 
              "Banana",
              "Grapes"]
print(fruits_list)

# 12). Modify the second item in the list and print the updated list.
fruits_list[1] =" Strawberry"
print(fruits_list)

# 13). Append a new fruit and insert another at the beginning of the list.
fruits_list.append("Apple")
fruits_list.insert(0, "Cherry")
print(fruits_list)

# 14). Demonstrate deleting an item using del, pop(), and remove().
number_s=[34,56,78,90,75]
number_s.remove(56)
print(number_s)
number_s.pop()
print(number_s)
number_s.__delitem__(1)
print(number_s)

#15). Sort the list permanently with sort() and temporarily with sorted(). Print before and after each.
origional = [1,3,4,0,7]
# Temporarily Sorted the Origional List
temp_sorted= sorted(origional)  
print(temp_sorted)
print(origional)
 # Permanently Sorted the Origional List
origional.sort()                    # perm_sorted = origional.sort() **** My Question????
print(origional)                    # print(perm_sorted)....???


#------------------------------------ { Intermediate} ----------------------------------

# 16). Create a list of dream travel destinations:
      # Sort alphabetically
      # Reverse the order
      # Find the total number of destinations
travel_dest_list = ["Lahore","Oman", "Islamabad", "Quetta", "Peshawar"]
travel_dest_list.sort(reverse=True)
print(travel_dest_list)          # Sorted the List Alphabetically
travel_dest_list.reverse()
print(travel_dest_list)          # Revered the Sorted list 
print(len(travel_dest_list))     # Total List Items

# 17). Start with an empty guest list:
      # Append three guests
      # Insert a guest at the beginning
      # Remove one guest with pop()
      # Print the final invitation list
      # Access the last three elements of a list without using negative indices.
empty_guest_list = []
empty_guest_list.extend(["Hassan", " Jahanzaib","Farhan" ])
print(empty_guest_list)
empty_guest_list.insert(0,"Taaha")
print(empty_guest_list)
empty_guest_list.pop(0)
print(empty_guest_list)

# 18).Access the last three elements of a list without using negative indices.
integer_list = [1,2,3,4,5,6]
print(integer_list[3:6])

# 19). Print only the even numbers from a list.
def print_even_numbers(numbers):
   for even_number in numbers:
        if even_number % 2 == 0:
            print(even_number)
numbers_list = [3,4,5,6,7,1,2]
print_even_numbers(numbers_list)

#20). Print the squares of the first 10 natural numbers using a list.
squares = [x**2 for x in range(1, 11)]    #For each number x in the range from 1 to 10, calculate x**2, and store it in a list
print(squares)

# natuarl_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# squares = []
# for no in natuarl_list:
#     if natuarl_list[no]<=11:
#         square = natuarl_list[no]**2
#         squares.append(square)
#         print(squares)

#=============================================={B O N U S  C H A L LE N G E }===================================
# B O N U S ------ C H A L L E N G E ``
# Combine variables and lists:
# Ask the user for five favorite movies.
# Store them in a list.
# Print the sorted list alphabetically.
favourite_movies = []
for i in range (5):
      movie = input(f"Please Enter Your 5 Favourite Movies = ")  # Asking the user for five favorite movies.
      favourite_movies.append(movie)       # Storing the enterd Movies in a new list
sorted_movies = sorted(favourite_movies)
print(sorted_movies)                        # Printing the sorted list a5lphabetically.          


table_no =int (input("Enter the table no which you want"))

for i in range(1,11):
    result=table_no * i
    print(f"{table_no} * {i} = {result}")



vehicle = input("Enter you Vahicle  ")
vehicles =["car", "bike", "bus"]
if vehicle not in vehicles:
        print("Try Again")
else:
    print(f"Your {vehicle} is Good")


guests = ["Umair", "Talha", "Taha"]
name = str(input("Enter Your Name   "))
if name in guests:
 print("Thanks for coming please dont mind")
 index=guests.index(name)
 del guests[index]
 guests.append("Ali")
else:
  print("Thanks we are not inviting")

print(guests)
guests.insert(0,"Moeed")
guests.insert(int(len(guests)/2) , "Jahnzaib")
guests.append("Hassan")
print(guests)