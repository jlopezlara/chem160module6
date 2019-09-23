Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from ising_class import *
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from ising_class import *
ModuleNotFoundError: No module named 'ising_class'
>>> Temp=2.3
>>> n=20
>>> ntrials=500000
>>> nequil=100000
>>> ising1=ising(Temp,n)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ising1=ising(Temp,n)
NameError: name 'ising' is not defined
>>> ising1.randomize()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ising1.randomize()
NameError: name 'ising1' is not defined
>>> ising1.trials(nequil)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    ising1.trials(nequil)
NameError: name 'ising1' is not defined
>>> ising1.resetprops()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    ising1.resetprops()
NameError: name 'ising1' is not defined
>>> for i in range(ntrials):
	ising1.trials()
	ising1.addprops()
	ising1.calcprops()
	ising1.printsys()
	
