# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.
marks = float(input('Enter your marks: '))

if(marks <= 25):
    grade = 'F'
    print(grade)
elif(marks > 25 and marks <= 45):
    grade = 'E'
    print(grade)
elif(marks > 45 and marks <= 50):
    grade = 'D'
    print(grade)
elif(marks > 50 and marks <= 60):
    grade = 'C'
    print(grade)
elif(marks > 60 and marks <= 80):
    grade = 'B'
    print(grade)
else:
    grade = 'A'
    print(grade)
    
    
  #Enter a number using custom input
a = int(input("Enter a nmber: "))

# if number is divisible by both 3 and 5 it returns fizzbuzz
if (a%5 == 0 and a%3 == 0):
    print("FizzBuzz")

# if number is divisible by 3 it returns fizz
elif(a%3 == 0 ):
    print("Fizz")

# if number is divisible by 5 it returns buzz
elif (a%5 == 0):
    print("Buzz")

# if none then simply return the number
else:
    print(a)
