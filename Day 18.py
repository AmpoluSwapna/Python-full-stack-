'''
lambda function
--> lambda function is a small anonymous function
--> lambda can take n number of arguments but only with one expression
--> The function is defined by using lambda keyword
syntax:
Ex:
lambda arguments : expression 
add = lambda a,b,c : a+b+c
print(add(10,20,30))

# even or odd using lambda function 
even = lambda num : num % 2 == 0
print(even(9))

#find greater number using lambda function  
num = lambda a,b : a if a > b else b
print(num(10,20))

#To find out cube value using lambda function
num = lambda a : a**3
print(num(5))

filter()
--> filter() function will perform only on selected elements of iterables
syntax:
filter(lambda arguments : expression , iterable)
Ex:
nums = [1,2,3,4,5,6,7,8]
data_ = filter(lambda a : a % 2 == 0 , nums)
print(tuple(data_))

map()
-->map()function will perform on all elements of a iterables
syntax:
map(lambda arguments : expression , iterable)
Ex:
nums = [1,2,3,4,5,6,7,8]
get_ = map(lambda a : a +6,nums)
print(list(get_))
Ex:
nums = [1,2,3,4,5,6,7,8]
get_ = filter(lambda a : a%2==0,nums)
print(list(get_))

reduce()
--> The reduce() function repeatedly applies a function to the elements and reduces them to one final value
--> It is avaiable in the functools module 
syntax:
reduce(lambda arguments : expression , iterable)
Ex:
from functools import reduce
nums = [1,2,3,4,5]
data_ = reduce(lambda a,b: a+b,nums)
print(data_)
Ex:
from functools import reduce
data_ = reduce(lambda a,b: a+b,range(1,10))
print(data_)

