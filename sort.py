#timeCombinations is all the combos generated for each subject
#subject is the list of subject with same index as timeCombinations
#roomList should initially be empty list that is scanned from excel
finalCombos=[]
timeCombinations=[]
subjects=[]
def Sorter(timeCombinations,subject,roomList):
    global timeCombos,subjects
    timeCombos=timeCombinations
    subjects=subject
    recursiveSorter([],roomList,0)
    return(finalCombos)

#take time combos for each subject and apply to roomList

def recursiveSorter(filledRooms,remainRooms,index):
    fill=[]
    remain=[]
    global timeCombos,subjects
    for combo in timeCombos[index]:
        #check if the combination works
        temp1,temp2,temp3=checkCombination(filledRooms,remainRooms,combo,subjects[index])
        if temp1==1:
            fill.append(temp2)
            remain.append(temp3)
    for e,d in zip(fill,remain):   
        if index==len(timeCombos)-1:
           global finalCombos
           finalCombos.append(e)
        else:
           recursiveSorter(e,d,index+1)

def checkCombination(a,b,c,d):
    fill=a[:]
    remain=b[:]
    for i in c:
        temp=[]
        for z in remain:
            temp.append(z.time)
        try:
             v=temp.index(i)
             remain[v].available=0
             remain[v].subject=d
             fill.append(remain[v])
             remain.pop(v)
        except (ValueError):
             return(0,[],[])
    return (1,fill,remain)
