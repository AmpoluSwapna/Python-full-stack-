'''
Dictionary
--> it is a collection of key:value pair
--> key must be unique and it should be immutable datatype(int,str,tuple)
--> dict is represented in {}
ex:
details = {1:2,
           'name':'swapna',
           (1,2):[1,2]}
print(details)

Accessing
--> dict can access by calling key,we will get value from that key
syntax:dict['key']
get()method 
--> get()method is also used to get the value from the key
synatx:dict.get(key)
data_ = {'name':'swapna',
         'balance':8000,
         'Adr':983899493572,
         'PANC':'XOBVR2890S'}
print(data_['PANC'])         
print(data_.get('Adr'))

update()
-->is used to update a key, incase if the key is not present inside the dict then it add that key:value
syntax: dict.update({key:value})
--> it can update in another way
syntax: dict[key] = value
data_ = {'name':'swapna',
         'balance':8000,
         'Adr':983899493572,
         'PANC':'XOBVR2890S',
         2:[3,4]}
print(data_)
data_['AC'] = 123456789456
data_.update({'name':'vishala'})
data_.update({'ATMPIN':1024})
print(data_)

values()
--> is used to get all the value from the dict
syntax: dict.values()
data_ = {'name':'swapna',
         'balance':8000,
         'Adr':983899493572,
         'PANC':'XOBVR2890S'}
print(data_.values())

keys()
-->is used to get all the key from the dict
syntax: dict.keys()
data_ = {'name':'swapna',
         'balance':8000,
         'Adr':983899493572,
         'PANC':'XOBVR2890S'}
print(data_.keys())

items()
it will get the key:value separated from the dict
syntax: dict.items()
data_ = {'name':'swapna',
         'balance':8000,
         'Adr':983899493572,
         'PANC':'XOBVR2890S'}
print(data_.items())         

clear()
is used to del all data from the dict
syntax: dict.clear()
data_ = {'name':'swapna',
         'balance':8000,
         'Adr':983899493572,
         'PANC':'XOBVR2890S'}
print(data_)
del data_['Adr']
print(data_)
data_.clear()
print(data_)

statements

if statement
-->if condition becomes true , then it will execute inside block of code
-->incase it becomes false it will never enter into inside the block
age = 19
if age>=18:
   print('Eligible to vote')
print(age)

a = 90
b = 78
if a>b:
   print(a)

if-else statement
-->else for if statement is a fall-back statement ,incase if conditions is false then block will execute
age = 15
if age>=18:
   print(f'your {age} Eligible to vote')
else:
   print(f'your {age} not eligible to vote')

a = 90
b = 780
if a>b:
   print(a)
else:
   print(b)





