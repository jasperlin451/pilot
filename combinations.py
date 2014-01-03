#outputs all the possible combinations of times for a specific subject
#combination with replacement
#possibleTimes is scanned in from each subject as is numberofClasses
import itertools

def combinations(possibleTimes,numberofClasses,classData):
    combo=[]
    for c in itertools.combinations_with_replacement(possibleTimes,numberofClasses):
        a=checkStudents(classData,c,possibleTimes)
        if a==1:
            combo.append(c)
    return(combo)

#returns time slots
#work on also returning leader meeting days

def checkStudents(data,combination,possibleTimes):
    temp=data
    for i in range(len(combination)):
        index=possibleTimes.index(combination[i])
        temp=sorted(temp,key=lambda student: student.avail[index])
        #remove the first 10 from list if 1 or 2
        #meaning a class can be made
        try:
            x=temp[9].avail[index]
            if x==3:
                return(0)
            else:
                del temp[0:10]
        except(IndexError):
             return(0)
    return (1)
