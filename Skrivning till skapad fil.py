f = open('Skrivning till skapad fil (DATA).txt','w')  #the file is created and named
for k in range(1,11):  #it is declared that "k" should be counted 10 times
	s='%3d\n' %(k*8)  #For each time "k" is counted, "s" equals "k" times 9. Also, each "s" has 3 spaces between them
	f.write(s)  #each "s" is written
f.close()  #the file is closed
