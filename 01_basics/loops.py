# print even num b/w 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
     print(i)

# table 
num = int(input("Enter a number: "))
for i in range(1, 11):
   print(f"{num} * {i} = {num * i}")

# Countdown
count = 5
while(count >= 1):
   print(count)
   count = count - 1
   
print ("Go!")


# print * 
for i in range(5):
   for j in range(0, i+1):
      print("*", end="")
   print()

# break statement
num1 = 1
while(num1 <= 10):
   print(num1)
   num1 = num1 + 1

   if num1 == 6:
      break
# continue statement
num2 = 1
while(num2 <= 10): 
   
   if num2 == 5:
      num2 += 1
      continue
   print(num2)
   num2 += 1

   