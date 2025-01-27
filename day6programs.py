## user defined functions  ###

def sum(a,b):
  add=a+b
  return add
a=int(input('Enter first number- '))
b=int(input('Enter second number- '))
sum(a,b)

def pow(a,b):
  s=a**b
  return s
a=int(input('Enter number- '))
b=int(input("Enter it's power- "))
pow(a,b)


def sub(a,b):
  s=a-b
  return s
a=int(input('Enter first number- '))
b=int(input('Enter second number- '))
sub(a,b)


def sum(a,b):
  add=a+" "+b
  return add
a=input('Enter first string- ')
b=input('Enter second string- ')
sum(a,b)

def prt(a,b):
  fst=a
  snd=b
  return fst,snd
a=input('Enter first name- ')
b=input('Enter second name- ')
prt(a,b)


def fact(n):
  factorial=1
  while n>0:
    factorial*=n
    n-=1
  return factorial
n=int(input('Enter the number - '))
fact(n)


def oddeve(n):
  if n%2==0:
    print('even')
  else:
    print('odd')
n=int(input('Enter the number - '))
oddeve(n)


def c_area(rad):
  area=3.14*rad*rad
  return area
rad=int(input('Enter radius - '))
c_area(rad)


def perfect_number(n):
  pf=0
  num=n//2
  for i in range(1,num+1):
    if n%i==0:
      pf+=i
  if pf==n:
    print('Perfect Number')
  else:
    print('Not a perfect number')
n=int(input('Enter a number - '))
perfect_number(n)



def fibonacci(n):
  x,y=0,1
  for i in range(n):
    print(x, end=" ")
    x,y = y,x+y
n=int(input('Enter a number- '))
if n <= 0:
  print("Enter valid number")
else:
  print('Fibonacci Series')
  fibonacci(n)



def avg(x,y,z):
  avrg=(x+y+x)/3
  return avrg
num1=int(input('Enter first number - '))
num2=int(input('Enter second number - '))
num3=int(input('Enter third number - '))
avg(num1,num2,num3)


#plaindrome number
def palindrome_num(n):
  m=n[::-1]
  if m==n:
    print('Palindrome Number')
  else:
    print('Not')
n=input('Enter a number')
palindrome_num(n)


#armstrong number program
def armstrong_num(n):
  temp=0
  p=int(n)
  sum=0
  for i in range(1,p+1):
    temp=int(p)%10
    temp=temp**len(n)
    sum+=temp
    p=p/10
  return sum
n=input('Enter a number- ')
p=armstrong_num(n)
if p==int(n):
    print('Armstrong NUmber')
else:
    print('Not')

