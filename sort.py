#timeCombinations is all the combos generated for each subject
#subject is the list of subject with same index as timeCombinations
#roomList should initially be empty list that is scanned from excel
import copy
import itertools
import collections
import room

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
            if index==len(timeCombos)-1: #if the last subject combination works
                split=subjectSplit(filled) #split the rooms by subject 
                #check to see if the value of new combination is greater than previous combination
                global value, finalCombo
                va,studentAssignments=checkCombinationValue(split)
                if va>value: #the combination we found improves it 
                    temp2,leaderCombos=checkLeaders(split,remain)
                    if temp2==1: #if there are leader slots that fit into combination slot
                        value=va
                        finalCombo=[]
                        #assign students to rooms
                        #!!!!finalRoomList=assignStudents(studentAssignments)
                        global subjects
                        for leaderMeetingTimes in leaderCombos:
                            for subLeader,subjectRoomList,sub in zip(leaderMeetingTimes,finalRoomList,subjects):
                                #add the subLeader Room to the subjectRoomList
                                global roomList
                                subjectRoomList.append(room.Room(roomList[subLeader].time,roomList[subLeader].classroom)
                                #last element of the list
                                subjectRoomList[-1].subject=sub
                                subjectRoomList[-1].leaderMeeting=1
                            #finalRoomList is the list with students and leader meeting times
                            finalCombo.append(copy.deepcopy(finalRoomList)) #potential to be very slow
                            #delete the added rooms so that the process can be done again
                            for delete in finalRoomList:
                                del delete[-1]
            else:
                recursiveSorter(filled,remain,index+1)

#determine if a particular room combination works
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
def checkCombinationValue(splitRooms):
    #based
   # for classes in breakdown:  


def assignStudents(studentAssignments):




def subjectSplit(filledRooms):
     global subjectClasses
     counter=0
     split=[]
     for classes in subjectClasses:
         split.append(filledRooms[counter:counter+classes])
         counter=counter+classes
     return(split)

def checkLeaders(splitRooms,emptyRooms):
    #splitRooms is list of list of rooms being used, split by subject
    search=emptyRooms[:]
    subjectCombo=[] #list of rooms by subject that can be used for leaders meetings
    finalList=[]
    for subject in splitRooms: #figure out which days are free for leaders to use
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





 
 
