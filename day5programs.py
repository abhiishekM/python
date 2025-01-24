num=1
while num<=5:
  print('Hi')
  num+=1

num=1
while num<=10:
  print(num)
  num+=1

num=1
while num<=5:
  print('Hi ', end=",")
  num+=1


num=100
while num>=1:
  print(num,end=",")
  num-=1


n=1
while n<=10:
  print('2 x',n,'=',n*2)
  n+=1


n=int(input('Enter the number - '))
n1=1
while n1<=10:
  print(n,'x',n1,'=',n*n1)
  n1+=1


n=1
n1=0
while n1<=10:
  n1+=n
  n+=1
print(n1)



n=int(input('Enter number'))
n1=0
while n>0:
  n1+=n
  n-=1
print(n1)




num=1
while num<=20:
  if num%2==0:
    print(num,"is even")
  else:
    print(num,"is odd")
  num+=1  




num=int(input('Enter the number - '))
count=0
while count<num:
  if num%2==0:
    print(num,"is even")
  else:
    print(num,"is odd")
  num-=1  
