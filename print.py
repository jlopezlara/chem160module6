Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> intval=21
>>> floatval=22/7
>>> string="Hello Bye"
>>> print("Int= %5d\n"%(intval))
Int=    21

>>> print("Int= %05d"%(intval))
Int= 00021
>>> print("Int= %-5d"%(intval))
Int= 21   
>>> print("Int= %+5d"%(intval))
Int=   +21
>>> print("Flt=%7.2f"%(floatval))
Flt=   3.14
>>> print("Flt=%7.4f"%(floatval))
Flt= 3.1429
>>> print("Flt=%+7.2f"%(floatval))
Flt=  +3.14
>>> print("Str=%s"%(string))
Str=Hello Bye
>>> print("Str=%10s"%(string))
Str= Hello Bye
>>> print("Int=%5d\nFlt=%7.2f"%(intval,floatval))
Int=   21
Flt=   3.14
>>> 
