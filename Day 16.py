'''
Functions
--> is a block of code that can be executed only when it is called
--> Function start with def keyword and the line is declared as definition line,where we can define a function name
--> if we want to execute the program in the function,need to call with the function name define at def line 
syntax:
def fun_name(parameters):
    pass
fun_name(arguments)
ex:
def add_(a,b):
    print(a+b)
add_(6,7)

#arguments
positional/required arguments
--> the arguments(def line) and the parameters(calling fun) should be exact number,if they are not in the exact it will raise an error  
def add_(a,b):
    print(a+b)
add_(6,7)

num = 0
num_2 = 1
def add_(num,num_2):
    print(num+num_2)
add_(0,1)

num = 0
num_2 = 1
def feb_(num,num_2):
    print(num,num_2,end=' ')
    for i in range(1,10):
        num_3 = num + num_2
        num = num_2
        num_2 = num_3
        print(num_3,end=' ')
feb_(num,num_2)

#default arguments
--> where the function will only consider the data at calling function even though data present in the def line 
def feb_(num,num_2):
    print(num+num_2)
feb_([1,3],[5,6])

def data_(a=8,b=9):
    print(a+b)
data_(1,2)

def prime(num =10,count = 1):
    for j in range(1,num+1):
        if num%j==0:
            count+=1
            print(count)
    if count == 2:
        print(f'{num} is prime')
    else:
        print(f'{num} is not a prime')
prime(num=int(input("Enter a number:")),count=0)

#keyword arguments
--> are sending arguments in a pair(a=2),and the passing order is not considered 
def data_(age,name,batch,location):
    print(batch)
    print(age)
    print(name)
    print(location)
data_(name='vishali',age=22,location='vizag',batch=6)

#variable length argument
--> adding a *(call it as args) before a variable at parameter
--> we can pass tuple of arguments and can be access with indexing
def all_(*name):
    print(name)
all_('swapna','ampolu','vishali','gottapu')

#keyword length arguments
--> adding a **(call it as k args) before a variable at parameter
--> we can pass variable length arguments and can be access
def details(**data_):
    print(data_.keys())
details(name='vishali',age=22,location='vizag',batch=6)

return
--> return keyword used inside the function ,once the return is executed ,it will get back to the calling function with return values
def all_(a,b):
    return a-b
print(all_(5,9))



































    
