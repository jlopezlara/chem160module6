Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> self.left=((i-1+n)%n,(j-1+n)%n)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    self.left=((i-1+n)%n,(j-1+n)%n)
NameError: name 'i' is not defined
>>> self.right=((i+1)%n,(j+1)%n)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    self.right=((i+1)%n,(j+1)%n)
NameError: name 'i' is not defined
>>> self.up=((i-1+n)%n,(j+1)%n)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    self.up=((i-1+n)%n,(j+1)%n)
NameError: name 'i' is not defined
>>> self.down=((i+1)%n,(j-1+n)%n)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    self.down=((i+1)%n,(j-1+n)%n)
NameError: name 'i' is not defined
>>> 
