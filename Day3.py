'''
Datatypes & TypeConversions

1.numeric datatype
float and integer
float
A number which contains decimal values
eg:
price = 56.89
integer(int)
A normal number without any decimal values
eg:
num1 = 89
num_2 = 6

2.String datatype
string is a sequence of characters that are enclosed in '',"",""""""
string is immutable
eg:
any_ = 'python is a language'
all_= 'Ab,.&[)-+'

3.list datatype
list is a collection of different datatypes and it is represented by [] which are seperated by ,
inside the list we call it as items
list is mutable
eg:
any_ = [1,'python',[5,6]]
print(type(any_))

4.Tuple datatype
Tuple is a collection of differnt datatypes that are enclosed in ()
and those are separeted by ,
tuple is immutable
eg:
nums = (1,89.60,'python',[3,4],(8,9))

5.Dictionary datatype
Dictionary is a collection of key:value pairs,keys and values are separeted by :
key and value pair can be call as item and items are separeted by ,
Dictionaries are represented by {}
in key place we use immutable datatypes
in values place we can use either immutable or mutable (any datatype)
eg:
data_ ={1:2,
       'name' : 'swapna'
       (2,3) : 'tuple'
print(data_)

6.set datatype
set is a collection of unique elements and sets don't accept any duplicate values
set is represented by {} and the elements are separeted by ,
eg:
an = {1,2,3,3}
print(an)

Type Conversions

float-> int, str
eg--> int()
price = 45.90
print(int(price))
eg--> str()
price = 45.90
con = str(price)
print(type(con))

integer-> float,str
eg-->float()
num = 78
print(float(num))
eg-->str()
num = 78
con_ = str(num)
print(type(num))

string-> int,float
eg-->int()
do = '10'
print(int(do))
eg--> float()
do = '10.89'
print(float(do))

list-> tuple,str
eg--> tuple()
nums = [1,2,3,4]
print(tuple(nums))
eg-> str()

tuple-> list
eg-->list()
all_ = (5,6,7)
print(list(all_))

set->tuple,list
eg-->tuple()
all_ = {5,6,7}
print(tuple(all_))

dictionary-> list
eg-->dict()
details = [('name','swapna'),('edu','B.Tech')]
print(dict(details))

'''  
