print("Enter your choice:\n 1.Addition\n2.Subtraction\n3.Division\n4.Multiplication")
n=int(input())
if n==1:
  print("Enter number 1 and number 2")
  a=int(input("First number "))
  b=int(input("Second number "))
  print("Sum is:",a+b)
elif n==2:
  print("Enter number 1 and number 2")
  a=int(input("First number "))
  b=int(input("Second number "))
  print("Subtraction is:",a-b)
elif n==3:
  print("Enter number 1 and number 2")
  a=int(input("First number "))
  b=int(input("Second number "))
  print("Division is:",a/b)
elif n==4:
  print("Enter number 1 and number 2")
  a=int(input("First number "))
  b=int(input("Second number "))
  print("Product is:",a*b)
else:
  print("Not a valid choice")



print("Enter two numbers")
a=int(input("First number "))
b=int(input("Second number "))
print("Enter your choice:\n1.Addition\n2.Subtraction\n3.Division\n4.Multiplication")
n=int(input())
if n==1:
  print("Sum is:",a+b)
elif n==2:
  print("Subtraction is:",a-b)
elif n==3:
  print("Division is:",a/b)
elif n==4:
  print("Product is:",a*b)
else:
  print("Not a valid choice") 



day=int(input("Enter the week day - "))
if day==1:
  print("MONDAY")
elif day==2:
  print("TUESDAY")
elif day==3:
  print("WEDNESDAY")
elif day==4:
  print("THURSDAY")
elif day==5:
  print("FRIDAY")
elif day==6:
  print("SATURDAY")
elif day==7:
  print("SUNDAY")
else:
  print("INVALID DAY")








#greatest of two integers

a=int(input("Enter first integer -"))
b=int(input("Enter second integer -"))
if a>b:
  print("A is greater")
else:
  print("B is greater")


#check two integers are equal or not

a=int(input("Enter first integer -"))
b=int(input("Enter second integer -"))
if a==b:
  print("Both are equal")
else:
  print("both are not equal")


#greatest of three integer

a=int(input("Enter first integer -"))
b=int(input("Enter second integer -"))
c=int(input("Enter third integer - "))
if a>b and a>c:
  print("A is greatest")
elif b>c:
    print("b is greatest")
else:
  print("c is greatest")


#program to check vowel or consonant
str1=input('Enter one character')
if str1 in 'aeiou':
  print('Vowel')
else:
  print('Consonant')
