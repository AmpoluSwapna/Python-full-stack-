'''
Tuple()
Tuple is a collection of different datatypes separeted by , and represented by ()
it is immutable
we can pass a tuple values and that can be assign to the variables ,but it should have same no.of variables inside the tuple 
t = (1,'python',[3,4],(7,9))
print(t[2][1])

index()
t = (1,'python',[3,4],(7,9))
print(t.index('python'))

len()
t = (1,'python',[3,4],(7,9))
print(len(t))

accessing through tuple
name,age,batch,dept = ('swapna',22,6,'python')
print(name)
print(age)
print(batch)
print(dept)

max()
so = (67,88,75,23)
print(max(so))
min()
so = (67,88,75,23)
print(min(so))
count()
so = (67,88,88,23,76)
print(so.count(88))
so = (67,5,89,45)
do =(45,89)
print(so+do)
