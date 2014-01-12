#outputs all the possible combinations of times for a specific subject
#combination with replacement
#possibleTimes is scanned in from each subject as is numberofClasses
import itertools

def combinations(possibleTimes,numberofClasses,classData,roomCount):
    combo=[]
    for a in itertools.combinations_with_replacement(possibleTimes,numberofClasses):
        b=checkStudents(classData,a,possibleTimes)
        c=checkRooms(a,roomCount)
        if b==1 and c==1:
            combo.append(a)
    return(combo)

#returns time slots

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

#check to see if the combination is possible based on number of rooms available
def checkRooms(combo,roomCount):
    temp=set(combo)
    comboTimes=list(temp)
    comboRooms=[]
    for b in comboTimes:
        comboRooms.append(combo.count(b))
    for i in range(len(comboTimes)): #check to see if combo rooms more than available rooms
        if roomCount[1][roomCount[0].index(comboTimes[i])]<comboRooms[i]:
            return(0)
    return(1)
