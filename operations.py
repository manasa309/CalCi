import math

def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return "Error: Division by zero!" if y == 0 else x / y
def mod(x, y): return "Error: Modulo by zero!" if y == 0 else x % y
def floordiv(x, y): return "Error: Division by zero!" if y == 0 else x // y
def power(x, y): return x ** y
def sqrt(x): return "Error: Negative number!" if x < 0 else math.sqrt(x)
def factorial(x): 
    return "Error: Negative number!" if x < 0 else math.factorial(int(x))
def absolute(x): return abs(x)
