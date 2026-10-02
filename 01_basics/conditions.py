# simple student grade calculator.

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
else:

  if marks >= 90:
    print("Grade A+")
  elif marks >= 80:
    print("Grade A")
  elif marks >= 70:
    print("Grade B")
  elif marks >= 60:
    print("Grade C")
  elif marks >= 40:
    print("Grade D")
  else:
    print("Grade F")


if marks >= 40:
    print("Passed")
else:
    print("Failed")

    