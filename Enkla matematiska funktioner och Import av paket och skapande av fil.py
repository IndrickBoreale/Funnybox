#!/usr/bin/env python
def sum(a,b):
	return a+b
print sum(3,2)



def sum(a,b,c):
	return a-b-c
print sum(10,5,2)



def sum(a,b,c,d):
	return a*b*c*d
print sum(2,3,4,5)



def sum(a,b,c,d,e):
	return a/b/c/d/e
print sum(100,2,2,5,5)



def minus(a,b):
	return a-b
def division(a,b):
	return a/b
print minus(3,2)
print division(5.0,2.0)



def mymult(a,b):
	svar=0
	while b>0:
		b=b-1		
		svar=svar+a
	return svar
print mymult(4,3)



def mymult2(a,b):
	svar=0
	while b>1:
		b=b-3
		svar=svar+a
	return svar
print mymult2(2,21)



def bytvarde(a):
	global lokalvar
	lokalvar=a
lokalvar=10
print lokalvar
bytvarde(12)
print lokalvar



import math as lollery
print lollery.sin(50)



from math import cos
print cos(70)



from math import *
print tan(30)



minfil = open('test.txt','w')
minfil.write ('Hello World!')
minfil.close()
print minfil



minfil = open('test.txt','r')
print minfil.read()
minfil.close()



minfil = open('test.txt','r')
print minfil.read(5)
print minfil.read()
minfil.close()



f = open('data.dat','w')
for k in range(0,11):
	s = '%3d' %(k*8)
	print(s)
f.close()




