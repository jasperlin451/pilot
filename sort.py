#timeCombinations is all the combos generated for each subject
#subject is the list of subject with same index as timeCombinations
#roomList should initially be empty list that is scanned from excel
import copy
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
        temp1,temp2,temp3=checkCombination(filledRooms,remainRooms,combo,subjects[index])
        if temp1==1:
            if index==len(timeCombos)-1:
               #calculate value of particular room combination
               #if value is greater than previous value, replace combination
              # global classData,subjects 
              # va=calculateValue(temp2,classData,subjects)
               global value,finalCombo,roomList
               temp=[]
               for i in range(len(temp2)):
                   temp.append(copy.deepcopy(roomList[temp2[i]]))
                   temp[i].available=0 
                   if i<8:
                       temp[i].subject='Calc II'
                   else:
                       temp[i].subject='Chem I'
               finalCombo.append(temp)
               # if va>value
               #    finalCombos=temp2[:]
                #   value=va
            else:
               recursiveSorter(temp2,temp3,index+1)

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
