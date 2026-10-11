# Local and global scope -> A variable's scope determines where it can be accessed.
# Global variable: Defined outside a function.
# Local variable: Defined inside a function and normally accessible only within that function.

def calculate_square(number):
 result = number * number
 return result
ans = calculate_square(5)
print(ans)