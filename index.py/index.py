#The FizzBuzz game contains some  simple logic for kids. You are given the number.
#If the number is divisible by 3, you reply "Fizz",  if the number is divisible by 5, you reply "Buzz".
#If the number is divisible by both 3  and 5 you reply "FizzBuzz". And if the number
#doesn't meet any of these conditions - i.e., it can't be divided by 3 or 5, then you simply reply with the number given.


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