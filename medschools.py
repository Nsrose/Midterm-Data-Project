import random 

medschools = []
for i in range(1, 51):
	medschools.append("Ms" + str(i))


students = []
for i in range(1, 51):
	students.append("Std" + str(i))

medschooldict = {}
for i in medschools:
	school = i 
	medschooldict[i] = []

studentdict = {}
for i in students:
	student = i
	studentdict[i] = []

def isnum(x):
	return isinstance(x, (int))

def randomize(listvalues):
	randlist = range(0, len(listvalues)) 
	auxlist = []
	index = 0
	while index<len(listvalues):
		auxlist.append(index)
		index +=1
	index = 0
	while index<len(listvalues): 
		auxlist = filter(isnum, randlist)
		place_to_insert = random.randint(0, len(auxlist)-1)
		randlist.insert(auxlist[place_to_insert], listvalues[index])
		randlist.remove(randlist[auxlist[place_to_insert]+1])
		index+=1
	return randlist 

for i in medschooldict:
	medschooldict[i].append(randomize(students))

for i in studentdict:
	studentdict[i].append(randomize(medschools))


def unstable(student, medschool, assignedmedschool, assignedstudent):
	if studentdict[student][0].index(medschool) < studentdict[student][0].index(assignedmedschool) and medschooldict[medschool][0].index(student) < medschooldict[medschool][0].index(assignedstudent):
		return "unstable"
	else:
		return "stable"

print unstable('Std3', 'Ms47', 'Ms32', 'Std28')