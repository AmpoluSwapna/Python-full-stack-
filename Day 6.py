'''
String operations

1.Indexing
indexing is used to get char that you looking to access
--> positive indexing
syntax : print(variable_name[index_position])
text = 'python'
print(text[3]) # positive indexing starts from 0
--> negative indexing
syntax : print(variable_name[Negative index_position])
text = 'python'
print(text[-1]) # negative indexing starts from -1
sample ex:
txt ='python is a programming language'
print(txt[17])
 print(txt[-15])

2.len()
len() is a built-in function is used to get number of char present in the string
syntax : len(variable_name)
txt ='python is a programming language'
print(len(txt))

3.slicing
This is used to access the particular part from the string
syntax :
variable_name[start:end]
txt ='python is a programming language'
print(txt[12:23])
syntax :
variable_name[start:]
txt ='python is a programming language'
print(txt[12:])
syntax :
variable_name[:end]
txt ='python is a programming language'
print(txt[:23])
syntax :
variable_name[start:end:skip]
txt = 'python'
rev = txt[::-1]
print(rev)

4.upper()
used to convert all small char into cap
txt = 'python is a programming language'
print(txt.upper())

5.lower()
used to convert all caps into small
txt ='VISHALAKSHI'
print(txt.lower())

6.index()
used to know the index position of an char
syntax : variable_name.index('substring',start,end)
txt = 'python is a programming language'
print(txt.index('r',9,18))

7.replace()
used to replace old substring with the new substring
syntax : variable_name.replace(old,new)
txt = 'python is a programming language'
print(txt.replace('python','java'))

8.split()
this method is used to separate string based on the given substring
syntax : variable_name.split(substring)
txt = 'python is a programming language'
print(txt.split(' '))

9.count()
used to count the number of occurances of an substring
syntax : variable_name.count('substring')
txt = 'python is a programming language'
print(txt.count('a',1,12))








