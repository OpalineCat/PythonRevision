import math

def square(num):
    return num ** 2

def square_root(num):
    return num ** 0.5

def factorial(num):
    fac = 1
    for i in range(1 , num + 1):
        fac = fac * i
    return fac

print("Welcom to the calculator!! Choose a method - ")
print("1. square of a number , 2. square root of a number , 3. factorial of a number , 4. Quit")
while True:

  choice = int(input("Enter you choice number: "))

  num = int(input("Enter the number of which you want to do the calculation of. "))

  if choice == 1:
    print(f"The square of the number is {square(num)}")
  elif choice == 2:
    print(f"The sqare root of the number is {square_root(num)}")
  elif choice == 3:
    print(f"The factorial of the number is {factorial(num)}")
  elif choice == 4:
     print("Thanks for using Calculator!!")
     break
  else:
    print("Invalid option")

#Counts words in a sentence and finds the most frequent word.
