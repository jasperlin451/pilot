#timeCombinations is all the combos generated for each subject
#subject is the list of subject with same index as timeCombinations
#roomList should initially be empty list that is scanned from excel
import copy
finalCombo=[]
timeCombinations=[]
subjects=[]
value=0
def Sorter(data,timeCombinations,subject,roomList,classes):
    global timeCombos,subjects,classData,subjectClasses
    timeCombos=timeCombinations
    subjects=subject
    classData=data
    subjectClasses=classes
    recursiveSorter([],roomList,0)
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
               global value,finalCombo
               finalCombo.append(temp2)
              # if va>value
               #    finalCombos=temp2[:]
                #   value=va
            else:
               recursiveSorter(temp2,temp3,index+1)

def checkCombination(a,b,c,d):
    
    fill=copy.deepcopy(a)
    remain=copy.deepcopy(b)
    for i in c:
        temp=[]
        for z in remain:
            temp.append(z.time)
        try:
             v=temp.index(i)
             #print(v,len(temp))
             remain[v].available=0
             remain[v].subject=d
             fill.append(remain[v])
             del remain[v]
        except (ValueError):
             return(0,[],[])
    return (1,fill,remain)

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
