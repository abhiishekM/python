#keywords and identifiers and operators
a=10
a+=5
print(a)
a-=3
print(a)
a*=4
print(a)
a//=2
print(a)


a="abhishek mishra"
print("abhishek" in a)

lst=[1,2,3,"apple"]
print(1 in lst)
print(7 not in lst)
print("apple" in lst)


#bitwise operator
x=5
y=3
print(x&y)
print(x|y)
print(x^y)



#identity operator
# is and is not
#id() is used to print memory
x=[1,2,3]
y=[1,2,3]
z=x
print(x is z)
print(x is not y)
print("memory location of x",id(x))
print("memory location of z",id(z))
print("memory location of y",id(y))
