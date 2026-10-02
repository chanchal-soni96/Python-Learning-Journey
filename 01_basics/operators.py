# Arithmetic
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


# Logical operators:
age = 22
has_id = True

print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)

# Student Marks Calculator(Practice).
python_marks = int(input("Enter Python marks: "))
java_marks = int(input("Enter Java marks: "))
javascript_marks = int(input("Enter Javascript marks: "))

total_subjects = 3

total_marks = python_marks + java_marks + javascript_marks
average = total_marks / total_subjects
percentage = (total_marks / 300) *100
is_passed = percentage >= 40

print("Total_marks: ", total_marks)
print("Average: ", round(average, 2))
print("Pecentage: ", round(percentage, 2))
print("Is_passed: ", is_passed)

