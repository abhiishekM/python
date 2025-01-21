print("Hey")

print('Hello World')

print("""Hi""")

print('''Hey''')


a=5.2
b=9.6
print(a+b)
print(type(a+b))


a= "hebcig"
b="fad"
print(a+b)
print(type(a+b))

a=input("Enter first number - ")
b=input("Enter second number - ")
print(int(a)+int(b))



a=int(input("Enter first number - "))
b=int(input("Enter second number - "))
print(a+b)


#division of two num taking inputfrom user
#multiplication of two num taking inputfrom user
a=int(input("Enter first number - "))
b=int(input("Enter second number - "))
d=a//b
print(d)
print(type(d))


#average of three numbers inputfrom user

a=int(input("Enter first number - "))
b=int(input("Enter second number - "))
c=int(input("Enter third number - "))
avg=(a+b+c)/3
print(avg)
print(type(avg))


#program to calculate area of a square of any given size

a=int(input("Enter the side of square - "))
area=a*a
p=4*a
print("Area=",area)
print("perimeter=",p)


#area of right angle triangle
base=float(input("Enter base of the triangel -"))
height=float(input("Enter height of the triangel"))
area= .5*base*height
print("Area = ",area)


#area and perimeter of triangle
a=float(input("Enter first side of triangle - "))
b=float(input("Enter second side of triangle -"))
c=float(input("Enter third side of triangle -"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
peri=a+b+c
print("Area = ",area)
print("Perimeter = ",peri)


#to calculate area of a circle
radius=float(input("Enter radius of the circel"))
area=3.1*radius*radius
print("Area =" ,area)


#to calculate simple intrest
principal=float(input("Enter principal amount"))
rat=float(input("Enter rate - "))
time=float(input("Enter time in years"))
si=(principal*rat*time)//100
print("Simple intrest = ",si)


#to calculate compund intrest
principal=float(input("Enter principal amount - "))
rat=float(input("Enter rate - "))
time=float(input("Enter time in years"))
ci=principal*(1+(rat/100))**time-principal
print("Compound intrest = ",ci)



#TO FIND SUM OF 5 SUBJECTS AND FIND PERCENTAGE
s1=float(input("Enter marks of first sub. -"))
s2=float(input("Enter marks of second sub. -"))
s3=float(input("Enter marks of third sub. -"))
s4=float(input("Enter marks of fourth sub. -"))
s5=float(input("Enter marks of fifth sub. -"))
sum = s1+s2+s3+s4+s5
per=(sum/500)*100
print("Total marks = ",sum)
print("Percentage = ",per)


a=input("Enter first number - ")
b=input("Enter second number - ")
print("Before swapping",a,b)
t=a
a=b
b=t
print("After swapping",a,b)

a=float(input("Enter first number - "))
b=float(input("Enter second number - "))
print("Before swapping",a,b)
print("After swapping",((a*b)/a),((a*b)/b))


a=float(input("Enter first number - "))
b=float(input("Enter second number - "))
print("Before swapping",a,b)
a,b=b,a
print("After swapping",a,b)



#fstring uses

name="RAM"
AGE=5
print(f"name {name} age {AGE}")


#fstring uses
name="Abhishek"
AGE=18
clg="NIET"
print(f"my name is {name}, my age is {AGE}. I'm studying in {clg}")



#.format usage

name="RAM"
AGE=5
print("name is {} and my age {}".format(name,AGE))
#OUTPUT ---  name is RAM and my age 5



#fstring uses
name="Abhishek"
AGE=18
clg="NIET"
roll= 3
print("my name is {}, my age is {}. I'm studying in {}".format(name,AGE,clg,roll))



num=91.08794
print(f"the given number upto 2 decimal points {num:.2f}")

#output -- the given number upto 2 decimal points 91.08794000

