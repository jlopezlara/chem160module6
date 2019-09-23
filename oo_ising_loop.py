Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from ising_class import *
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from ising_class import *
ModuleNotFoundError: No module named 'ising_class'
>>> Temp=0.5
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
>>> while Temp<4.:
	ising1.changeTemp(Temp)
	ising1.trials(nequil)
	ising1.resetprops()
	for i in range(ntrials):
		ising1.trial()
		ising1.addprops()

		
Traceback (most recent call last):
  File "<pyshell#15>", line 2, in <module>
    ising1.changeTemp(Temp)
NameError: name 'ising1' is not defined
>>> 	ising1.calcprops()
	
SyntaxError: unexpected indent
>>> 
