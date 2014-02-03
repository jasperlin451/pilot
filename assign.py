#subjectData is number of groups per subject
#times is pilot meetingTimes per subject
from itertools import combinations, permutations
from collections import Counter

def assignLeaders(leaderData, leaderDays, roomList, subjectData, times):
    value,leaderAssign,usedRooms = recurse(leaderDays, leaderData, roomList, subjectData, times,0)
    return(leaderAssign,usedRooms)
    
def recurse(leaderDays, leaderData, roomList, subjectData, times, index):
    subject = subjectData[index]
    classTimes=[]
    for blah in times[index]:
        classTimes.append(roomList[blah].time)
    days=leaderDays[index]
    leads = []
    value = 0
    max = 0
    best = []
    possibleTimes=[]
    possibleRooms=[]
    #determine room times available
    for checkRoom in roomList:
        if (checkRoom.time.split(' ',3)[0] in days) and (checkRoom.taken==False) and (checkRoom.time not in possibleTimes):
            possibleTimes.append(checkRoom.time)
            possibleRooms.append(checkRoom)
    #sort by those times
    for time,leadRoom in zip(possibleTimes,possibleRooms):
        #find index
        for i in leaderData:
            if time in i.availability:
                indexer=i.availability.index(time)
                break
        leaderData=sorted(leaderData, key=lambda key: key.total, reverse=True)
        leaderData=sorted(leaderData, key=lambda key: key.subjectPreference[index])
        for leader in leaderData:
            if  (leader.subjectPreference[index] < 3) and (leader.taken is False) and (time in leader.availability):
                leads.append(leader) #potential leaders
        if len(leads)<subject: #not enough leaders
            return 0, None, None
        if (index == len(subjectData) - 1):         #Base Case
            possibles=combinations(leads,subject)
            for possible in possibles:
                combo, value = checkCombos(possible, subject, classTimes, roomList, index)
                if not (combo is None):
                    return value, combo, leadRoom    
            return value, combo, leadRoom
        #else:
        possibles = combinations(leads, subject)
        for possible in possibles:
            combo, value = checkCombos(possible, subject, classTimes, roomList, index)
            if not (combo is None):
                for lead in combo:
                    lead.taken=True
                leadRoom.taken=True
                afterValue, leaderList, leaderRooms = recurse(combo, leaderData, roomList, subjectData, times, index+1)
                if not (afterValue is 0):
                    return value + afterValue, leaderList.insert(0, combo), leaderRooms.insert(0,leadRoom)
                else:
                    for lead in combo:
                        lead.taken=False 
                    leadRoom.taken=False
    return 0, None, None
        
def checkCombos(leads, subject, classTimes, roomList, index):
    temp=[]
    for b in classTimes:
        temp1=[]
        for a in leads:
            if b in a.availability:
                temp1.append(a)
        temp.append(temp1)
    #assign the classTimes with the least leader availability first
    sortedindex = []
    for i in temp:
        sortedindex.append(len(i))
    sortedRooms=[]
    for n in zip(sortedindex,temp):
        sortedRooms.append(n)
    sortedRooms=sorted(sortedRooms, key=lambda test:test[0])
    finalCombo = []
    for count in range(len(classTimes)):
        currentLead = getLeast(classTimes, sortedRooms[0][1]) 
        if currentLead is None:
            return None, 0
        currentLead.taken = True
        finalCombo.append(currentLead)
        #update sortedRooms, removing first index, and then recount and resort
        del sortedRooms[0]
        length=[]
        for z in sortedRooms:
            count=0
            for leading in z[1]:
                if leading.taken==False:
                    count=count+1
            length.append(count)
        temp2=[]
        for p in zip(length,sortedRooms):
            temp2.append(p[1])
        sortedRooms=sorted(temp2, key=lambda test: test[0])

    return finalCombo, 10

def getLeast(classTimes, leaders):
    mini = 10000
    least = None
    for lead in leaders:
        if lead.taken==False:
            y = 0
            for t in lead.availability:
                if t in classTimes:
                    y+=1
            if y<mini:
                least = lead
    return least

'''for c in range(len(classTimes)):
        minimum=temp.index(min(temp))
        meetingTime=classTimes[index]
        temp2=[]
        for m in leads:
           if meetingTime in m.available:'''
        
'''
perms = permutations(leads, subject)
    for perm in perms:
        w = True
        value = 0
        for lead, time in zip(perm, classTimes):
            if not (roomList[time].time in lead.availability):
                w = False
            else:
                if (lead.subjectPreference[index] is 1):
                    value +=3
                else:
                    value +=1
        if w is True and value>subject*2:
            return perm, value
            
    return None, 0
'''

    
