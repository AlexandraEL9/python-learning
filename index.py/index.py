#The FizzBuzz game contains some  simple logic for kids. You are given the number.
#If the number is divisible by 3, you reply "Fizz",  if the number is divisible by 5, you reply "Buzz".
#If the number is divisible by both 3  and 5 you reply "FizzBuzz". And if the number
#doesn't meet any of these conditions - i.e., it can't be divided by 3 or 5, then you simply reply with the number given.

"""
#declare variable and give value
num =  2

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz") 
elif num % 5 == 0:
    print("Buzz")
else:
    print(num) 

                                        #build basic function 
def add_two_numbers():
    print("function running")

add_two_numbers()

        #add values to function
def add_two_numbers(num1, num2):
    print(num1, num2)

add_two_numbers(2, 3)

        #add the two numbers together 
def add_two_numbers(num1, num2):
    sum = num1 + num2
    print(sum)

add_two_numbers(2, 3)

def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum

result = add_two_numbers(10, 32)
print(result)  

       #Build a function that takes 3 numbers, multiples them together and returns the result.
def multiply_three_numbers(num1, num2, num3):
    product = num1 * num2 * num3
    return product

result = multiply_three_numbers(2, 10, 3)
print(result) 
             #result 60


       #takes one number and returns its value squared (the number times itself)
def num_squared(num1):
    product = num1 * num1
    return product

result = num_squared(2)
print(result) 
             #result 4

       #that takes 2 numbers, and returns the value of the first number divided by the second number

def num_divided(num1, num2):
    dividend = num1 / num2
    return dividend

result = num_divided(100, 2)
print(result) 
             #result 50


# Define the function named add_numbers that takes two parameters: nums_tuple, min_value
def add_numbers(nums_tuple, min_value):
    # The function returns the sum of all values in nums_tuple that are greater or equal to min_value
    return sum(num for num in nums_tuple if num >= min_value)

# Outside of the function
# Create a variable named total and assign it the return value from calling add_numbers function
total = add_numbers((21, 4, 7, 19, 1), 15)

# Print the total
print(total)
              #result  40
"""


#functions challenge
numbers = [12, 45, 60, 87, 999, 200, 84, 42, 87, 77, 2, 3, 77, 99, 20]
# 1. define/ name the function
#3.pass the function the list of numbers- tell function to expect it
def get_odd_nums(list_of_nums):
    #5. create empty list variable to add numbers into
    new_list = []
    for num in list_of_nums:#6. access each num in list to check which ones are odd (use a for loop)
        if num % 2 != 0:
            new_list.append(num)
    return new_list
#2. call the function with call statement
#4. pass the list into where t is called
result = get_odd_nums(numbers)
print(result)         #[45, 87, 999, 87, 77, 3, 77, 99]









