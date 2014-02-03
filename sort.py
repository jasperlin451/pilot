#timeCombinations is all the combos generated for each subject
#subject is the list of subject with same index as timeCombinations
#roomList should initially be empty list that is scanned from excel
import itertools
import collections
import room

finalStudentAssignments=[]
finalLeaderCombo=[]
finalCombo=[]
exit=False
def Sorter(data,timeCombinations,subject,classes,rooms,subjectTimeSlots,per):
    global timeCombos,subjects,classData,subjectClasses,roomList,timeSlots,studentsper
    timeSlots=subjectTimeSlots
    roomList=rooms
    timeCombos=timeCombinations
    subjects=subject
    classData=data
    subjectClasses=classes
    studentsper=per
    recursiveSorter([],list(range(len(roomList))),0)
    return(finalCombo, finalStudentAssignments, finalLeaderCombo)

#take time combos for each subject and apply to roomList

def recursiveSorter(filledRooms,remainRooms,index):
    global timeCombos,subjects,exit
    for combo in timeCombos[index]:
        if exit==False:
            #check if the combination works
            temp1,filled,remain=checkCombination(filledRooms,remainRooms,combo,subjects[index])
            if temp1==1:
                if index==len(timeCombos)-1: #if the last subject combination works
                    split=subjectSplit(filled) #split the rooms by subject 
                    #check to see if the value of new combination is greater than previous combination
                    temp2,leaderCombos=checkLeaders(split,remain)
                    if temp2==1: #if there are leader slots that fit into combination slot
                        studentAssignments=checkCombinationValue(split)
                        global finalStudentAssignments,finalCombo,finalLeaderCombo
                        finalStudentAssignments=studentAssignments
                        finalCombo=split
                        finalLeaderCombo=leaderCombos
                        exit=True
                        break
                else:
                    recursiveSorter(filled,remain,index+1)
        else:
            break

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

#calculate if the room combination is favorable,first preference=+3,can make=+1
def checkCombinationValue(splitRooms):
    studentAssignments=[] #list of lists of lists (subject, rooms, people)i
    global classData,roomList, timeSlots,studentsper
    for subject,studentData,possibleTimes,classSize in zip(splitRooms,classData,timeSlots,studentsper): #each subject
        subjectAssignments=[]
        for classrooms in subject: #each room
            temp=[]
            index=possibleTimes.index(roomList[classrooms].time)
            studentData=sorted(studentData,key=lambda student: (student.pref, student.avail[index]))
            for students in studentData:
                if len(temp)<classSize:
                    if int(students.avail[index])<3 and students.taken==False:
                        students.taken=True
                        temp.append(students)
                if len(temp)==classSize:
                    subjectAssignments.append(temp)
                    break
        studentAssignments.append(subjectAssignments)
        
    return(studentAssignments)    

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
                days.remove(temp.split(' ',3)[0])
            except(ValueError): #day has already been removed
                pass
            if len(days)==0:
                #combination uses all the days of the week, leaders can't be assigned
                return(0,[])
        finalList.append(days)
    return(1,finalList)





 
 
