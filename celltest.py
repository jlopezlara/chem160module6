Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from ising_class import *
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from ising_class import *
ModuleNotFoundError: No module named 'ising_class'
>>> acell=cell(3,3,10) #Args: i, j, n
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    acell=cell(3,3,10) #Args: i, j, n
NameError: name 'cell' is not defined
>>> print(acell.cellspin())
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(acell.cellspin())
NameError: name 'acell' is not defined
>>> acell.spin.flip() #Reaching through cell to inner spin object
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    acell.spin.flip() #Reaching through cell to inner spin object
NameError: name 'acell' is not defined
>>> print(acell.left) #Directly accessing the neighbor indices
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(acell.left) #Directly accessing the neighbor indices
NameError: name 'acell' is not defined
>>> print(acell.right)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(acell.right)
NameError: name 'acell' is not defined
>>> print(acell.up)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(acell.up)
NameError: name 'acell' is not defined
>>> print(acell.down)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(acell.down)
NameError: name 'acell' is not defined
>>> 
