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

