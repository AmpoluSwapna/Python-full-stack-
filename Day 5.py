'''
Bitwise operator
--> & bitwise and
5 --> 0101
3 --> 0011
1 --> 0001
print(5&3)

--> | bitwise or
5 --> 0101
3 --> 0011
print(5|3)
7 --> 0111

--> ^ bitwise xor
5 --> 0101
3 --> 0011
6--> 0110
print(5^3)

--> >> right shift
5 --> 0101
1 --> 0001
print(5>>2)

--> << left shift
5 --> 0101
10 --> 1010
print(5 <<1)

input formatting
--> integer --> int(input())
num = int(input('Enter your four digit number '))
print(num)
--> float --> float(input())
a = float(input('Enter decimal number'))
print(a+5)
--> string -->input()
b = input("enter your name")
print(b)
--> list
num = list(map(int,input('Enter numbers:').split()))
print(num)
--> tuple
num = tuple(map(int,input('Enter numbers:').split()))
print(num)
--> sets 
num = set(map(int,input('Enter numbers:').split()))
print(num)
--> eval
data_ = eval(input('enter:'))
print(type(data_))

output formatting
 --> separeted by commas
name = 'swapna'
age = 21
print(' My name is ',name ,'age is ', age )
print('Hello!',name )
--> fstring or doc string
name = 'swapna'
age = 21
print(f'My name is {name} and I am {age} years old')
-->modulo
name = 'swapna'
age = 21
print('my name is %s and i am %d years old '%(name,age))
 
