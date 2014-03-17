# coding=utf-8

f = open('Förändring av existerande fil (DATA).txt','r')  #the file "f" is opened and read
r = open('Förändring av existerande fil (DATA).txt','w')  #the file "r" is opened and prepared to be written in
while 1:  #an infinite loop
	s=f.readline()  #as long as the loop is running, the program will read the current line and then move to the next
	if s =='':  #when the program reaches a line where there is just a space, IE the end....
		break  #...it will stop the loop.
	m=int(s)  #the program must convert what it reads to a number, since that is what the read file contains.
	p=m*10  #modifies the numbers it found in the file by multiplying each number by 10
	q='%3d\n' %(p)	#each number is written on its own line
	r.write(q)  #the numbers are written inside "r"
r.close()  #the file "r" is closed
f.close()  #the file "f" is closed




