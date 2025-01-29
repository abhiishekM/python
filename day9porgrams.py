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
