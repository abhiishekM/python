## lambda function ##

sum=lambda x,y:x+y
print(sum(1,5))

sub=lambda x,y: x-y
print(sub(1,4))


pow=lambda x,y: x**y
print(pow(2,4))


div=lambda x,y: x/y
print(div(54,9))


a=int(input('Enter first number- '))
b=int(input('Enter second number- '))
sum=lambda x,y:x+y
print('sum is',sum(a,b))


mul=lambda x,y: x*y
print(mul(2,4))


evodd=lambda x: "even" if x%2==0 else "odd"
print(evodd(5))



area=lambda rad:rad*rad*3.14
print(area(7))

l=[1,2,3]
cub=list(map(lambda x:x**3,l))
print(cub)


l=[1,2,3]
double=list(map(lambda x:x*2,l))
print(double)


def double(x):
  return x*2
l=[1,2,3]
double=list(map(double,l))
print(double)


c_rad=[12,2,3.5,8,0.5,16]
c_area=list(map(lambda rad:rad*rad*3.14,c_rad))
print(c_area)


from functools import reduce
l=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,l)
print(sum)


from functools import reduce
l=[1,2,3,4,5]
high=reduce(lambda x,y:x if x>y else y,l)
print(high)


from functools import reduce
l=[1,2,3,4,5]
sum=reduce(lambda x,y:(x**2)*(y**2),l)  
print(sum)


tup1=(10, 20, 30)
fst=lambda tp:tp[0]
femt=get_first(tup1)
print(femt)


divv=lambda x: "divisible" if x%3==0 and x%5==0 else "not divisible"
print(divv(5))
