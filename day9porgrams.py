packed_tpl=(98,4398,984)
print(packed_tpl) #output (98, 4398, 984)
a,b,c=packed_tpl
print(a,b,c) #output 98 4398 984


packed_list=[354,355,215,315]
print(packed_list) #output [354, 355, 215, 315]
a,b,c,d=packed_list
print(a,b,c,d)  #output 354 355 215 315


packed_stri='hi','heloo','python'
print(packed_stri) #output ('hi', 'heloo', 'python')
a,b,c=packed_stri
print(a,b,c) #output hi heloo python


packed_stri='hi','heloo','python'
print(packed_stri) #output ('hi', 'heloo', 'python')
a,b,c=packed_stri
print(a,b,c) #output hi heloo python



#for variable lengths
num=[384,1,53653,345,351,1,315]
print(num)
a,b,c,*d=num
print(a,b,c,*d) #output 384 1 53653 345 351 1 315
print(a,b,c,d)  #output 384 1 53653 [345, 351, 1, 315]



def sum_all(*args):
  return sum(args)
packed_args=10,65,46
result=sum_all(*packed_args)
print(result)

#output- 121



def display_info(**kargs):
  for key,value in kargs.items():
    print(key,':',value)

packed_kwargs={'name':'Alice', 'age':15}
display_info(**packed_kwargs)
#output- name : Alice
#output- age : 15

my_list = [1, 2, 3]
my_list[1] = 20 
print(my_list) # Output: [1, 20, 3]


stri=['hi','heloo','python']
stri[2]='sujeet'
print(stri)


stri=['hi','heloo','python']
stri.extend(['bihari','hai'])
print(stri)


ls1=['hi', 'heloo', 'python', 'bihari', 'hai']
ls1.pop(2)
print(ls1)


list=[3,1,4,2]
list.sort(reverse=True)
print(list)


list=[3,1,4,2]
list.clear()
print(list)


list=[3,1,4,2]
list=[x*2 for x in list]
print(list)


d={'a':'b','b':2}
d.clear()
print(d)


d={'a':1,'b':2,'c':3}
for key in d:
  d[key]*=2
print(d)


d={}
keys=['a','b','c']
values=[1,2,3]
for k,v in zip(keys,values):
  d[k]=v  
print(d)



my_set={1,684,298,32465}
print(my_set)


my_set={1,684,298,32465}
e=my_set.pop()
print(e)
print(my_set)


my_set={1,684,298,32465}
my_set.clear()
print(my_set)


s1={1,2,3}
s2={4,5}
s1=s1.union(s2)
print(s1)


s1={1,2,3}
s2={2,3,4,5}
s1.intersection_update(s2)
print(s1)


s1={1,2,3}
s2={2,3,4,5}
s1.difference_update(s2)
print(s1)



s1={1,2,3}
if 4 not in s1:
  s1.add('f6854fhfd68d468hh68sh45')
print(s1)



