'''
list comprehension
--> it is the shortest form of syntax to cretae a new list
syntax:
[expression loop condition]
[expression condition else loop]
Ex:
old = (1,2,3,4,5,6,7,8)
new_ = [i for i in old]
print(new_)
Ex:
old = (1,2,3,4,5,6,7,8)
new_ = [i for i in old if i % 2== 0]
print(new_)

nested comprehension
--> using list comprehension generating list inside list
Ex:
any_ = [[i*j for i in range(1,6)] for j in range(1,10)]
print(any_)
Ex:
all_ = [[1,2,3],[4,5,6],[7,8,9]]
all_ = [num for i in all_ for num in i]
print(all_)

Generator
--> A generator is a special function which generates one value at a time
Ex:
def all_():
    for i in range(1,10):
        yield i
i = all_()
print(next(i)) 
