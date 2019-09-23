Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from cards import *
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from cards import *
ModuleNotFoundError: No module named 'cards'
>>> ntrials=10000
>>> awins=0
>>> for i in range(ntrials):
	adeck=deck()
	adeck.shuffle()
	ascore=0
	bscore=0
	while adeck.cardsleft()>2:
		acard1=adeck.dealcard()
		acard2=adeck.dealcard()
		bcard=adeck.dealcard()
		if acard1.value()>bcard.value() or acard2.value()>bcard.value():
			ascore+=1
		else:
			bscore+=1
		if ascore > bscore:
			awins+=1
	print("Player A win percentage=",awins/ntrials)
	
