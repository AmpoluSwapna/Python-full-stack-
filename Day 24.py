'''
Exception handling
--> It is the process of handling errors , we can write so many exceptions for the code written in the try block 
compennets :
try : where we can write code which may contain errors
syntax:
try:
    code lines
    
except : It will handle the errors which raised at the try block
Ex:
try:
    print(5/0)
    print(num)
except ZeroDivisionError: 
    print('Division by zero')
except NameError:
    print('Name Error')

else : It only excutes when there are no errors in the try block 
syntax:
except ErrorName:
    print("ErrorName")
Ex:
try:
    print("Hello")
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('Name Error')
else:
    print('No Error')
    
finally : This block will excutes regardless with the error at the try block 
try:
    print(num)
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('Name Error')
else:
    print('No Error')
finally:
    print('End')

File Handling

read()
with open('demo.txt','r') as file:
    print(file.read())

write()
with open('demo.txt','w') as file:
    file.write('This is swapna , I am learning python course')
'''

