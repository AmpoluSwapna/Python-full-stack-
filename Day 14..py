'''
in string 
ran_ = int(input('Enter a number:'))
for j in range(1,ran_+1):
    if j % 2 == 0:
         print(f'{j} is even')
    else:
         print(f'{j} is odd')

 
ran_ = int(input('Enter a number:'))
for j in range(1,ran_+1):
    if j % 2!=0:
        print(f'{j} is odd')
        
in list       
nums = [23,78,97,5]
for j in nums:
    if j % 2 == 0:
        print(f'{j} is even')
    else:
        print(f'{j} is odd')

words_ = input('Enter a word:')
vowels = 'aeiouAEIOU'
count = 0
for i in words_: 
    if i not in vowels:
       count += 1
       print(f'{i} is consonant')
print(count)

removing duplicates list 
digits_ = [1,2,3,1,5,3]
empty_ =[]
for i in digits_:         
    if i not in empty_:
        empty_.append(i)
print(empty_)        

digits_ = (1,2,3,4,5,2,3,4,5)
empty_ = ()
for j in digits_:
    if j not in empty_:
       empty_+= (j)
print(f'{j} is duplicate')

'''
  









        
