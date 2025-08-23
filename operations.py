import math as m

#basic operation
def add(a,b):                                                  
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    if a == 0 or b == 0:
        return 0
    else:
        return a*b
    
def div(a,b):
    if b== 0:
        ZeroDivisionError ('division my zero, please enter valid input')
    else:
        return a/b
    
def mod(a,b):
    return a%b

def f_div(a,b):
    return a//b

def pow(a,b):
    return m.pow(a,b)


#advanced arthematic operations
def sqrt(a):
    return m.sqrt(a)

def fac(a):
    return m.factorial(a)

def a_val(a):
    return m.fabs(a)


#trignometric operations
def sin(a): return m.sin(a)
def cos(a): return m.cos(a)
def tan(a): return m.tan(a)


#inverse trignometric operations 
def asin(a): return m.asin(a)
def acos(a): return m.acos(a)
def atan(a): return m.atan(a)

#logarithms and exponential operations
def n_log(a): return m.log10(a)
def log(a): return m.log(a)
def exp(a): return m.exp(a)



