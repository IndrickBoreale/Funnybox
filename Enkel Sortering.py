# coding=utf-8
def findbiggest(a,b):		#funktionen definieras
	if(a>b):				#ifall a är större än b så ska a returneras
		return a		
	else:					#annars kommer b att returneras
		return b
print findbiggest(3,7)		#a och b definieras och skrivs ut
print findbiggest(6,2)		#a och b definieras och skrivs en andra gång, med andra tal



def findlargest(a,b,c):		#funktionen definieras
	if(a>b>c):				#alla möjliga kombinationer av tre olika tal
		return a,b,c
	if(b>c>a):
		return b,c,a
	if(c>a>b):
		return c,a,b
	if(a>c>b):
		return a,c,b
	if(b>a>c):
		return b,a,c
	if(c>b>a):
		return c,b,a
print findlargest(15,30,45)			#de tre talen definieras och skrivs ut 3 gånger med olika värden
print findlargest(392,7304,157)
print findlargest(7090,99425,194)
