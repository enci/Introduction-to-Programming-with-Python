import numpy
 
pastalist = ["pasta 1",8,"pasta 2",10,"pasta 3",12,"pasta 4",4,"pasta 5",20]
np = len(pastalist)
 
pastanumber = 2*numpy.random.randint(0, (np/2))
pastatime = pastanumber + 1
 
print("pasta number =",pastanumber)
print("pasta time =",pastatime)
 
print("Take",pastalist[pastanumber],"out of the package, and put it in a large boiling pot of water. Boil for",pastalist[pastatime],"minutes.")