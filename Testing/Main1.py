def add(a,b):
    return a+b

def sub(a,b):
    return a - b

def divide(a,b):
    if b == 0:
        raise ValueError("it is not possible to divide")
    else:
        return a/b
    
def multiply(a,b):
    return a * b
    
    