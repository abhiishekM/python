def facto(num):
  if num==0 or num==1:
    return 1
  else:
    return num*facto(num-1)
