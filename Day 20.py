'''
modules
--> A module is a python file(.py) that written using function variables,operators,etc.
Ex:
import math
print(math.pow(2,3))

Built-in modules
--> The modules are developed by programmer and those comes with installation
math,os,sys,random,date and time

Ex:OS
import os
print(os.getcwd())

Ex:Sys
import sys
print(sys.path)
print(sys.version)

Ex:random
import random
print(random.randint(1000,9999))

importing specific module
syntax:from module import function
Ex:
from swapna import add_
print(add_(56,3))

using alias name
syntax:import module as alias name
Ex:
import swapna as sw
print(sw.add_(45,24))
'''
from swapna import *
print(add_(45,7))
print(sub(67,8))

