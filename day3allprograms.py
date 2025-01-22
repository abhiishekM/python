x=5
y=6
print(x&y)
print(x|y)
print(x^y)


a="Hello guys "
print(a*3)


a="Hello"
print(a[-1])




L=[1,2,3,"HI","HELLO"]
print("The digit is found at index ",L.index(2))

#output -- The digit is found at index  1

l=[1,2,3,4,5,6,7]
print(l[0:5:1])

s="Hello Python"
print(s[-1:-13:-1])

print(s[::-1])
print(s[::2])


l=[1,42,53,74,15,6]
l.sort()
print(l)


l=[4,5,6]
l[0]=1
print(l)


l=["RAM",45,True]
l[0]="abhishek"
print(l)


l=[1,2,3,4]
l.append(5)
print(l)


l=[1,2,3,4]
l.append(5)
print(l)
l.remove(2)
print(l)


#string methods

h=" hello India "
print(h.upper())
print(h.split())
print(h.strip())
print(h)
print("-".join(h))


a=(1,2,3,"ab")
a=(90,21)
a=("ab","ba")
a=(1,5,3,2,4.5,6,98,23)
print(a)
print(a[::2])
print(type(a[4]))



A={3,5,5,5,5684,-6,2.33,2.5,"A",9.45}
print(A)
print(A)


name={1:"Alice",2:"Soooraj",3:"Sujeeeeet"}
roll={1:"23",2:"63",3:"69"}
branch={1:"IT",2:"IT",3:"IT"}
print(name[3],roll[3],branch[3])
