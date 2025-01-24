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


for i in range(5):
  print('h')


for i in range(0,5):
  print('h')

for i in range(1,5):
  print('h')


n=100
for i in range(1,101):
  print(i)


n=100
for i in range(1,101):
  print(i,end=',')


n=100
for i in range(1,101):
  if i%2==0:
    print(i,'is even')


n=int(input('Enter the number - '))
n1=1
for i in range(1,11):
  print(n,'x',n1,'=',n*n1)
  n1+=1


n=int(input('Enter number'))
n1=0
for i in range(n1,n+1):
  n1+=i
print(n1)


for i in range(1,101):
  if i%5==0:
     print(i)


num=1
while num<=10:
  print(num)
  num+=1
else:
  print('Code successfully executed')


for i in range(5):
  print('Hello')
else:
  print('loop executed')



str1=input('Enter string - ')
count=0
while count<len(str1):
  print(str1[count])
  count+=1



str1=input('Enter string - ')
count=0
while count<len(str1):
  print(str1[count],end=',')
  count+=1


str1=input('Enter string - ')
count=0
while count<len(str1):
  print(str1[count],end=',')
  count+=1
else:
  print('\nexecuted')




l1=[1,2,"RAM",True]
count=0
while count<len(l1):
  print(l1[count])
  count+=1



l1=[1,2,"RAM",True]
count=0
while count<len(l1):
  print(l1[count],end=',')
  count+=1



l1=(1,2,"RAM",True)
count=0
while count<len(l1):
  print(l1[count])
  count+=1




