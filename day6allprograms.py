#factors of a number
num=int(input('Enter the number - '))
for i in range(1,num):
  if num%i==0:
    print(i)


#perfect number program
num=int(input('Enter the number - '))
L=[]
pf=0
for i in range(1,num+1):
  if num%i==0:
    L.append(i)
for i in range(0,len(L)):
  pf+=i
if pf==num:
  print('Perfect Number')
else:
  print('Not a perfect number')
#alternative program for perfect number(in this we'll use only n/2
n=int(input('Enter the number - '))
pf=0
num=n//2
for i in range(1,num+1):
  if n%i==0:
    pf+=i
if pf==n:
  print('Perfect Number')
else:
  print('Not a perfect number')

## nested loop ##

#table
for i in range(1,6):
  for j in range(1,6):
    print(f"{i} x {j} = {i*j}")
  print()

####  patterns   ###

n=int(input('Enter no.of rows - '))
for i in range(1,n+1):
  for j in range(1,n+1):
    print('*',end="")
  print()


n=int(input('Enter no.of rows - '))
for i in range(1,n+1):
  for j in range(1,i+1):
    print('*',end="")
  print()


