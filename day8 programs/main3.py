from myf import eveno,factorial,sum,sub
a=int(input('Enter number- '))
b=int(input('Enter number- '))

print('Sum is:',sum.add(a,b))
print('Difference is:',sub.sub(a,b))
print('Factorial of',a,'is',factorial.facto(a))
print('Factorial of',b,'is',factorial.facto(b))
print(a,'is',end=' ')
eveno.eveno(a)
print(b,'is',end=' ')
eveno.eveno(b)