#outputs all the possible combinations of times for a specific subject
#combination with replacement
#possibleTimes is scanned in from each subject as is numberofClasses
import itertools

def combinations(possibleTimes,numberofClasses,classData,roomCount,classSize):
    combo=[]
    for a in itertools.combinations_with_replacement(possibleTimes,numberofClasses):
        b=checkStudents(classData,a,possibleTimes,classSize)
        c=checkRooms(a,roomCount)
        if b==1 and c==1:
            combo.append(a)
    return(combo)

#returns time slots

def checkStudents(data,combination,possibleTimes,classSize):
    value=0
    for i in combination: #each room
        index=possibleTimes.index(i)
        data=sorted(data, key=lambda student: (student.pref,student.avail[index]))
        count=0
        for student in data:
            if count<classSize: #number of students in a class
                if int(student.avail[index])<3 and student.taken==False:
                    student.taken=True
                    count+=1
                    value=value+2/student.avail[index]
        if count !=classSize:#class was too small
            for reset in data:
                reset.taken=False
            return(0)
    #all the combinations worked,reset
    for students in data:
        students.taken=False
    if len(data)>100:
        if value<(classSize*len(combination)*1.8):
            return (0)
    elif len(data)>80:
        if value<(classSize*len(combination)*1.7):
            return(0)
    elif len(data)>50:
        if value<(classSize*len(combination)*1.6):
            return(0)
    else:
        if value<(classSize*len(combination)*1.5):
            return(0)
    return(1)

#check to see if the combination is possible based on number of rooms available
def checkRooms(combo,roomCount):
    temp=set(combo)
    comboTimes=list(temp)
    comboRooms=[]
    for b in comboTimes:
        comboRooms.append(combo.count(b))
    for i in range(len(comboTimes)): #check to see if combo rooms more than available rooms
        if roomCount[1][roomCount[0].index(comboTimes[i])]*.5<comboRooms[i]:
            return(0)
    return(1)
