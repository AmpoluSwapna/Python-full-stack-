'''
scope of variables -possibility 
1.local variables --> A variable is define inside the function call it as local variable, where the variable can only access within that function
Ex:
def display():
    name = 'swapna'
    print(name)
display()

2.global variables --> A variable that is define outside the function and it can be accessed anywhere throughout the program  
Ex:
a = 90
def display():
    print(a)
display()
print(a)

global keyword --> is a keyword used to reaccess new values to a variable that was already defined outside the function call  
Ex:
a = 90
print(a)
def display():
    global a
    a = 10
display()
print(a)

passing through value
def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
even_odd(109) 

passing through reference
num =8 
def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
even_odd(num)

reccursive function --> The function calls itself until the base condition is met
Ex:
'''
def Fac(a):
    if a == 0 or a == 1:
        return a
    return a * Fac(a-1)
print(Fac(7))




















