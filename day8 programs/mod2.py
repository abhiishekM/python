def add(x,*y):
    s=x
    for i in y:
        s+=i
    return s
def sub(x,*y):
    s=x
    for i in y:
        s-=i
    return s
def mul(x,*y):
    s=x
    for i in y:
        s*=i
    return s
def div(x,*y):
    s=x
    
    for i in y:
        s/=i
    return s
def pow(x,*y):
    s=x
    for i in y:
        s**=i
    return s
