# name is a parameter 
def greet(name): 
    print(f'Hello, {name}! Welcome to python learning.')
greet("Chanchal") #Chanchal is an arguments

print() 

# displays something on the screen.
# return gives a value back so you can store it, reuse it, or calculate with it.

def calculate_total(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = calculate_total(num1, num2)
print(f"Total:{result}")

# Default Arguments
def calculate_price(price, tax=5):
    tax_amount = price * tax / 100
    return price + tax_amount

print(calculate_price(20))
print(calculate_price(20, 10))

# Keyword arguments
def student_details(name, age, course):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")

student_details(course="CS", age=23, name="Chanchal")

# *args -> Multiple positional arguments, args collects the values into a tuple.
# **kwargs — multiple keyword arguments, it collects the named values into a dictionary.


def calculate_sum(*args):
    return sum(args)
result = calculate_sum(10, 20, 30, 40)
print(result)

def display_profile(**kwargs):
    print(kwargs)
display_profile(name="chanchal", age=23, course= "Python")

