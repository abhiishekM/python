#custom module
def facto(num):
  if num==0 or num==1:
    return 1
  else:
    return num*facto(num-1)

#used it as
import module
n=int(input('Enter number- '))
module.facto(n)
