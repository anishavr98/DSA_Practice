#Prob 1 : Write a program that takes an integer, then a string, then a char from the user and prints them in the screen.

a = int(input())
b = input()
c = input()[0]

print(a)
print(b)
print(c)

#Prob 2: Write a program to check whether a triangle can be formed with the given values for the angles.
#If sum of angles is equal to 180, then triangle can be formed, else it can't be formed.
a1=int(input())
a2=int(input())
a3=int(input())
if(a1+a2+a3==180):
  print("Is a triangle")
else:
  print("Not a triangle")
  
#Prob 3
"""Given mark of student, Print the Grade

Grade A if mark is greater than or equal to 90

Grade B if mark is greater than or equal to 80

Grade C if mark if greater than or equal to 60

Grade D if mark if greaer than or equal to 35

Fail if mark is lesser than 35
"""
mark = int(input())

if mark >= 90:
    print("Grade A")
elif mark >= 80:
    print("Grade B")
elif mark >= 60:
    print("Grade C")
elif mark >= 35:
    print("Grade D")
else:
    print("Fail")

"""Prob 4: Write a program using switch case which takes a value and prints the respective Size.
If size is 29 then its small

If size is 30 then its Medium

If size is 38 then its Large

If size is 42 then its XLarge

If size is not any of the above then Invalid.
"""
# Take size input from the user as an integer
size = int(input("Enter the size: "))

# Match the input value against specific cases
match size:
    case 29:
        print("Small")
    case 30:
        print("Medium")
    case 38:
        print("Large")
    case 42:
        print("XLarge")
    case _:
        # The underscore (_) acts as the default case
        print("Invalid")
