'''
Built-in functions
# math
import math
print(math.pi)
print(math.ceil(4.3))
print(math.floor(5.6))
print(math.sqrt(25))
print(math.sin(2))
print(math.pow(2,3))
print(math.cos(5))

# random
import random
print(random.randint(100000,999999))
print(random.randrange(1,100))
colour = ['red','blue','green','pink','lavander']
print(random.choice(colour))
random.shuffle(colour)
print(colour)

# platform
import platform
print(platform.python_version)
print(platform.system())
print(platform.platform())
print(platform.processor())

# collections
import collections
data_ = ['banana','apple','banana','orange','orange']
print(collections.Counter(data_))
all_ = collections.Counter(data_)
print(all_.most_common())

from collections import defaultdict
data_ = defaultdict(list)
data_['python'].append('swapna')
data_['python'].append('vishala')
data_['java'].append('madhu')
print(data_)

# datetime 
from datetime import datetime
today = datetime.today()
print(today.month)
print(today.day)
print(today.year)
print(today.hour)
print(today.minute)

from datetime import datetime
now = datetime.now()
print(now.strftime('%d-%m-$Y'))
print(now.strftime('%H-%M-$S'))
print(now.strftime('%A'))
print(now.strftime('%a'))

EX:
import random
attempt = 3
num = random.randrange(1,100)
print(num)
while attempt > 0:
    game = int(input('Enter a number between 1 and 100:'))
    if game == num:
        print("your guess is correct")
        break
    else:
        attempt -= 1
if attempt == 3:
    print('price money is 500')
elif attempt == 2:
    print('price money is 200')
elif attempt == 1:
    print('price money is 100')
else:
    print('better luck next time')

#itertools
import itertools
a = itertools.count(24)
print(next(a))
print(next(a))
b = itertools.repeat('vishala',6)
for j in b:
    print(j)
c = itertools.cycle(['swapna','ampolu','vishala'])
for j in c:
    print(j)
n = itertools.chain([1,2,3],[4,5,6])
print(list(n))

import math
print(math.pow(5,6))


