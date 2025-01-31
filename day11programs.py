file=open('nf.txt','r')
c=file.readlines()
print(c)
file.close()


file=open('nf.txt','r')
c=file.readline()
print(c)
file.close()


file=open('nf.txt','r')
c=file.read()
print(c)
file.close()


file=open('nff.txt','w')
c=file.write('Hello')
file.close()



file=open('nf.txt','r')
for line in file:
  print(line)
file.close()



file=open('nf.txt','a')
file.write('\n hiiiiiiiii')
file.close()
file=open('nf.txt','r')
c=file.read()
print(c)


with open('binary.bin','rb') as file:
  content=file.read()
print(content)




with open('nf.txt','r') as file:
  file.seek(5)
  print(file.tell())
  print(file.read())



import os
if os.path.exists('nff.txt'):
  print('hao')
else:
  print('n')


try:
  file=open('nfi.txt','r')
except FileNotFoundError:
  print('not found')
