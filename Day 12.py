'''
loops
For loop --> is used to iterate over a sequence or iterable datatypes
Ex:
nums = [12,3,5,78]
for num in nums: # after for num is the instance variable, which means it define this variable at run time to store values from iterable datatype
    print(num)

else in for --> unlike if-else, the else block in for statement is executed after completed all iterations
Ex:
nums = [12,3,5,78]
for num in nums: 
    print(num)
else:
    print('For ended')

control statements
break--> is used to stop iteration based on the given condition
Ex:   
nums = [1,2,3,4,5,6,7]
for num in nums:
    print(num)
    if num == 3:
       break
       
val_ = [1,2,3,4,5,6,7]
for j in val_:
    if j % 2 == 0:
       print(f'{j} is even')
    else:
       print(f'{j} is odd')

continue--> is a keyword used to skip the current iteration based on the given condition
Ex:
nums = [1,2,3,4,5,6,7]
for num in nums:
    if num == 3:
       continue
    print(num)

pass--> is a space-holder,that is used after statements like (if,for,else) not to raise any error
Ex:  
for j in range(1,11):
    if j == 15:
       print(j)
    else:
       pass

assert--> is a keyword used to check the condition, incase the condition is false it will raise the error (AssertionError)
Ex:
age = 15
assert age >= 18,'Not eligible to vote'
print('your eligible to vote ')

while loop
Ex:   
num = 1
while num < 5:
      print(num)
      num += 1

questions
1.find out the number is even or odd
2.remove duplicates from the list
3.armstrong number
4.Number of vowels in the string 
5.count the no.of words in the string

---- afternoon class
iteration/instance variable
for i in [10,20,30,40,50]:
    print(i)

name = 'python'
for swapna in name:
    print(swapna)

Range -- accepts ony for numerical values 
for i in range(5):
    print(i)
#if range = n
#values = n-1

for i in range(1010):
    print(i)
   
arr =[1,2,3,4,5]
for i in range(len(arr)): # print indexes 
    print(i)

arr=[1,2,3,4,5]
for i in arr: 
    print(i)

arr=[1,2,3,4,5]
for i in range(arr):
    print(i)
    
for i in range(2,7): # for i in range(start,stop)
    print(i)

for i in range(1,10,2): # for i in range(start,stop,step)
    print(i)

for i in range(2,10,-1):
    print(i)
    
for i in range(10,2,-1): # for i in range(stop,start,step)# reverse looping 
    print(i)
    
arr = [10,20,30,40,50]
for i in range(len(arr)):
    print(arr[i])






    






















 
