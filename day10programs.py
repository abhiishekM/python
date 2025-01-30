words=['python','is','easy']
result='$'.join(words)
print(result)
#python$is$easy

sen='my name is sujeet'
result=sen.split(' ')
print(result)
#['my', 'name', 'is', 'sujeet']


sen='  sujeet   '
result=sen.strip()
print(result)#sujeet


sen='my name is sujeet'
result=sen.replace('sujeet','sujeet R')
print(result)
#my name is sujeet R



sen='my name is sujeet'
result=sen.find('sujeet')
print(result)
#11


sen='my name is sujeetme is sujeetme is sujeetme is sujeetme is sujeetme is sujeet'
result=sen.count('sujeet')
print(result)
#6

sen='my name is sujeet'
result=sen.capitalize()
print(result)
#My name is sujeet



sen='my name is sujeet'
print(sen[::-1])
#teejus si eman ym




sen='my name is sujeet'
lst=list(sen)
print(len(lst))
#17



sen='my name is sujeet'
lst=list(sen)
vowel=0
const=0
for i in range(0,len(lst)):
  if lst[i]=='A' or lst[i]=='E' or lst[i]=='I' or lst[i]=='O' or lst[i]=='U' or lst[i]=='a' or lst[i]=='e' or lst[i]=='i' or lst[i]=='o' or lst[i]=='u':
    vowel+=1
  else:
    const+=1
print('No. of Vowels:',vowel)
print('No. of Consonant:',const)
#No. of Vowels: 6
#No. of Consonant: 11


s=input('Enter string: ')
p=s[::-1]
if s==p:
  print('Palindrome')
else:
  print('Not Palindrome')


