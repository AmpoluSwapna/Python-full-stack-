
'''
1.Arithmetic operators
--> +
any = 56
any_1 = 45
print(any + any_1)
--> -
all = 76
all_2 = 54
print(all - all_2)
--> *
mul = 49
mul_n = 56
print(mul *mul_n)
--> /
a = 78
b = 48
print(a / b)
--> //
an = 56
an_4 = 77
print( an // an_4)
--> %
num = 45
num_3 = 98
print( num % num_3)

2.Assignment operator
--> += 
d = 0
d += 1
print(d)
--> -=  
m = 67
m -= 5
print(m)
--> *=
c = 7
c *= 2
print(c)
--> /=
s = 8
s /= 4
print(s)
--> %=
v = 9
v %= 3
print(v)

3.Comparison operator
==,<=,>=,<,>,!=
--> ==
val = 9
val_2 = 9
print(val == val_2)
--> !=
r = 7
r_1 = 5
print(r!= r_1)
--> >
p = 5
p_3 = 3
print(p > p_3)
--> <
n = 6
n_4 = 9
print(n < n_4)
--> >=
u = 10
u_2 = 9
print(u >= u_2)
--> <=
z= 6
z_3 = 2
print(z <= z_3)

4.logical operator
--> and
var = 9
var_2 = 13
print(var >= var_2 and var <=10)
--> or
one=9
one_2=13
print(one >= one_2 or one<10)
--> not
van=9
van_2=13
print(not(van >= van_2 or van <10))

5.Identity operator
--> is
x =[1,2]
y =[1,2]
print( x is y)
--> is not
t=[1,2]
q=[1,2]
print(id(t))
print(id(q))
print( t is not q )

6.Membership operator
--> in
shell= 'python is language '
print('y' in shell )
--> not in 
name = 'python is language' 
print('i' not in name)

PYTHON PRACTICE

# print hello world
print("Hello World!")

# sum of two numbers
num_1 = int(input("Enter 1st number:"))
num_2 = int(input("Enter 2nd number:"))
print(num_1 + num_2)

practice questions
#area of rectangle
length = int(input("Enter a number:"))
width = int(input("Enter a number:"))
area = length*width
print(area)

# even or odd
num = [1,2,3,4,5,6,7]
for i in num:
    if i % 2 == 0:
       print(f'{i} is even')
    else:
       print(f'{i} is odd')
       
num = int(input("Enter a number:"))
if num % 2 == 0:
    print(f'{num} is even ')
else:
     print(f'{num} is odd')

#name and age
name = input("Enter a name:")
age = int(input("Enter your age:"))
print(f'my name is {name} and I am {age} years old')

#counts number of words
a = input()
new_ = a.split()
print(len(new_))

#find maximun and minimum values in list
num = [10,20,30,40,50]
highest = max(num)
lowest = min(num)
print("maximum:",highest)
print("minimum:",lowest)

#str is palindrome
any_= input("enter a word:")
empty_str = ''
for i in any_:
    empty_str = i + empty_str
if empty_str == any_:
    print(f'{any_} is a palindrome')
else:
    print(f'{any_} is not a palindrome')

#find positive numbers
num = [2,4,6,8]
for i in num:
    if num > 0:
        print(f'{num} is positive number')
    else:
        print(f'{num} is negative number')

def add_(a,b):
    return a+b

def sub (a,b):
    return a-b

def pw(a,b):
    return a**b
'''
swapna_details_ICIC = {
    'Name': 'swapna',
    'Adr': '123456789',
    'pan': 'GPCBU2073T',
    'ATMPIN': '2244',
    'Balance': 10000
}

All_attempts = 3

while All_attempts > 0:
    user_pin = input("Enter your 4 digit ATM PIN: ")

    if len(user_pin) == 4 and user_pin.isdigit():

        if user_pin in swapna_details_ICIC['ATMPIN']:
            print('Welcome to ICIC ATM')

            choice_ = int(input('Enter\n1. Withdraw\n2. Deposit: '))

            if choice_ == 1:
                with_m = int(input('Enter amount to withdraw: '))

                if with_m <= swapna_details_ICIC['Balance'] and with_m % 100 == 0:
                    swapna_details_ICIC['Balance'] -= with_m

                    print(
                        f'Take your cash and the balance is '
                        f'{swapna_details_ICIC["Balance"]}'
                    )
                else:
                    print('Insufficient balance or This ATM cannot provide change')

            elif choice_ == 2:
                depo_m = int(input('Enter amount to deposit: '))

                if depo_m % 100 == 0:
                    swapna_details_ICIC['Balance'] += depo_m

                    print(
                        f'Amount deposited and total balance is '
                        f'{swapna_details_ICIC["Balance"]}'
                    )
                else:
                    print('This ATM does not accept change')

            else:
                print('Invalid choice')

            break

        else:
            All_attempts -= 1

            if All_attempts > 0:
                print(f'Incorrect PIN entered and you have {All_attempts} attempts left')
            else:
                print('Your card is blocked')

    else:
        print("PIN must contain exactly 4 digits")












