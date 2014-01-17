#timeCombinations is all the combos generated for each subject
#subject is the list of subject with same index as timeCombinations
#roomList should initially be empty list that is scanned from excel
import copy
import itertools
import collections

finalCombo=[]
timeCombinations=[]
subjects=[]
value=0
def Sorter(data,timeCombinations,subject,classes,rooms):
    global timeCombos,subjects,classData,subjectClasses,roomList
    roomList=rooms
    timeCombos=timeCombinations
    subjects=subject
    classData=data
    subjectClasses=classes
    recursiveSorter([],list(range(len(roomList))),0)
    return(finalCombo)

#take time combos for each subject and apply to roomList

def recursiveSorter(filledRooms,remainRooms,index):
    global timeCombos,subjects
    for combo in timeCombos[index]:
        #check if the combination works
        temp1,filled,remain=checkCombination(filledRooms,remainRooms,combo,subjects[index])
        if temp1==1:
            if index==len(timeCombos)-1:
                split=subjectSplit(filled) 
                #see if leaders meetings will fit
                temp4,leaderCombos=checkLeaders(split,remain)
                if temp4==1:
                    for combination in leaderCombos:
                        studentRooms=filled[:]
                        for i in combination: #fill the leader meeting time slots
                            studentRooms.append(i)
                        #calculate value of particular room combination
                        #if value is greater than previous value, replace combination
                        # global classData,subjects 
                        # va=calculateValue(temp2,classData,subjects)
                        global value,finalCombo,roomList
                        temp=[]
                        if len(finalCombo)<3:
                            for i in range(len(studentRooms)):
                                temp.append(copy.deepcopy(roomList[studentRooms[i]]))
                                temp[i].available=0 
                                if i<8:
                                    temp[i].subject='Calc II'
                                elif(i<18):
                                    temp[i].subject='Chem I'
                                elif(i<19):
                                    temp[i].subject='Calc II'
                                    temp[i].leaderMeeting=1
                                else:
                                    temp[i].subject='Chem I'
                                    temp[i].leaderMeeting=1
                            finalCombo.append(temp)
               # if va>value
               #    finalCombos=temp2[:]
                #   value=va
            else:
                recursiveSorter(filled,remain,index+1)

def checkCombination(b,a,combination,subject):
    remainRooms=a[:]
    filledRooms=b[:]
    for time in combination:
        temp=[]
        global roomList
        for z in remainRooms:
            temp.append(roomList[z].time)
        try:
             v=temp.index(time)
             filledRooms.append(remainRooms[v])
             del remainRooms[v]
        except (ValueError):
             return(0,[],[])
    return (1,filledRooms,remainRooms)

#calculate if the room combination is favorable
#first preference=+3
#can make=+1
def calculateValue(rooms,data,subject,numberofClasses):
    #seperate into subjects
    breakdown=[]
    counter=0
    for i in numberofClasses:
        breakdown.append(rooms[counter:counter+i-1])
        counter=counter+i
    #based
   # for classes in breakdown:  

def subjectSplit(filledRooms):
     global subjectClasses
     counter=0
     split=[]
     for classes in subjectClasses:
         split.append(filledRooms[counter:counter+classes])
         counter=counter+classes
     return(split)

def checkLeaders(splitRooms,emptyRooms):
    search=emptyRooms[:]
    subjectCombo=[] #list of rooms by subject that can be used for leaders meetings
    finalList=[]
    for subject in splitRooms:
        days=['Sunday','Monday','Tuesday','Wednesday','Thursday'] 
        for usedRoom in subject:
            try:
                global roomList
                temp=roomList[usedRoom].time
                days.remove(temp.split(' ',4)[0])
            except(ValueError): #day has already been removed
                pass
            if len(days)==0:
                #combination uses all the days of the week, leaders can't be assigned
                return(0,[])
        possibleDays=days[:]
        possibleRoom=[]
        for day in possibleDays: #possible meeting days
            for room in search: #go through each possible room
                if day==roomList[room].time.split(' ',4)[0]: #if the remaining room matches day 
                    possibleRoom.append(room) 
        subjectCombo.append(possibleRoom) #final result is leader times for subject 
    #make combinations from remaining rooms 
    for combo in itertools.product(*subjectCombo):
        #check for overlapping rooms
        count=collections.Counter(combo)
        failed=0
        for i in count:
            if count[i]!=1: #combination is overlapping, wont work
                #skip this particular combination
                failed=1
                break
        if failed==0:
            finalList.append(combo) 
    return(1,finalList)





 
 
