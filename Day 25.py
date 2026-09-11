'''
print("Good Morning")

#perform operation
a = 15
b = 25
print(a+b)
'''
#list--> append(),extend(),insert()
batch = ['PFS-6','DA-6']
print(batch)
#print(type(batch))# everything is a object
#print(len(batch))
batch.append('swapna')
print(batch)
print(len(batch))
batch.extend(['vishala','ampolu']) 
print(batch)
batch.insert(0,'sravanthi')#inserts value at specific index
print(batch)
batch.insert(-1,'python')#inserts value before index 
print(batch)
#print(len(batch))

#indexing-->[]--> index starts at 0 and ends at len(obj)-1
#also in reverse manner -1 to len(obj)
#print(batch[0])
#print(batch[4])
#print(batch[34])#indexerror --> length is only 7 we are accessing extra

#slicing--> group of values [start:end] , start is included where as end is excluded
#print(batch[0:3])
#print(batch[4:6])
#print(batch[2:4])
#last 3 elements --> we prefer negative index values
#print(batch[-3:])
#first 3 elements
#print(batch[:3])

#striding -->[start:end:step]
print(batch[::2])#skips 1 elements 
print(batch[::3])#skips 2 elements 
print(batch[1:5:2])#first performs batch[1:5]--> then skips 1 element 

#tryoout
print(batch[:7:4])
print(batch[7::4])
print(batch[1::5])
print(batch[1:7:-2])
print(batch[-1:-4:-1])
