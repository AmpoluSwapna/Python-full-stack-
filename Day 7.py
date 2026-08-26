'''
list
Collecetion of different datatypes that are separated by , and it is represented by []

indexing
positive indexing --> 0
negative indexing --> -1

so = [1,2,3,4,'Python']
print(so[4][-1])

so = [1,2,3,4,'Python']
print(so[-1][-3])

all_=[12,[1,'python',[1,4],(78,[6,7])],['Java',78]]
print(all_[1][3])

len()
The function is used to find the number of items present inside list (gives the count of the items
Syntax:
data_ = ['Python',[1,2,(90,'Details',[67,0]),(78,'Student')]]
print(len(data_))

slicing
if 2:6 means except 2 it will gives the values 3,4,5,6
eg:
data_ = [1,2,3,4,5,6,7]
print(data_[2:6])

concatinate --> side by side
eg
a = [1,2]
b = [3,4]
print(a+b)

append() --> append method will add new items into list at last index position it also
accepts integers and it gives what is there in append(...)
Syntax --> variable_name.append(item)
eg
go = [1,2]
print(go)
go.append(3)
print(go)
go.append(4)
print(go)

eg
a = [1,2]
a.append([3,4])
print(a)

extend()
it will not accept integers, it gives the output by slitting the values at last position
accepts only iterables
eg
go = [1,2]
go.extend('python')
print(go)

pop()
it deletes the values of the particular position by indexing like from 0th count
eg
m = [5,1,2,3,4,'python']
m.pop(5)
print(m)
output --> deletes the 5th position value 'python'

remove()
it removes the particular value and one at a time, don't give multiple values
syntax --> variable_name.remove(value)
eg
m = [5,1,2,3,4,'python']
m.remove(5)
print(m)
output --> removes the value 5
