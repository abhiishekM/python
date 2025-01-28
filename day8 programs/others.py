import os
print(os.getcwd())
print(os.listdir())
os.mkdir("new_folder2")
print(os.listdir())



from datetime import datetime
now = datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))


#age calculator
from datetime import datetime
now = datetime.now()
by=int(input('Enter year of birth- '))
age=datetime.now().year-by
print(age)
