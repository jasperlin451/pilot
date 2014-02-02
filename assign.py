#subjectData is number of groups per subject
#times is pilot meetingTimes per subject
from itertools import combinations, permutations
from collections import Counter

def assignLeaders(leaderData, leaderDays, roomList, subjectData, times):
    value,leaderAssign,usedRooms = recurse(leaderDays, leaderData, roomList, subjectData, times,0)
    return(leaderAssign,usedRooms)
    
def recurse(leaderDays, leaderData, roomList, subjectData, times, index):
    subject = subjectData[index]
    classTimes = times[index]
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
    for time,leadRoom in zip(possibleTimes,possibleRoom):
        leaderData=sorted(leaderData, key=lambda leader: leader.total, reverse=True)
        indexer=leader.availibility.index(time)
        leaderData=sorted(leaderData, key=lambda leader: leader.availability[indexer], reverse=True)
        leaderData=sorted(leaderData, key=lambda leader: leader.subjectPreference[index])
        for leader in leaderData:
            if  (leader.subjectPreference[index] < 3) and (leader.taken is False) and (time in leader.availability):
                leads.append(leader) #potential leaders
        if len(leads)<subject: #not enough leaders
            return 0, None, None
        if (index == len(subjectData) - 1):         #Base Case
            combo, value = checkCombos(leads, subject, classTimes, roomList, index)    
            if combo is None:
                return 0, None, None
            else:
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
    temp=[[None]]*len(classTimes)
    for a in leads:
        for i,d in zip(classTimes,temp):
            if i in a.availability:
                d.append(a)
    #assign the classTimes with the least leader availability first
    sortedTimes = []
    i = 0
    for time in temp:
        if len(sortedTimes) is 0:
            sortedTimes.append(i)
        else:
            x = 0
            while(len(time) < len(temp[x])):
                x+=1
            sortedTimes.insert(x, i)
    finalCombo = []
    for time in sortedTimes:
        currentLead = getLeast(classTimes, time) #write later
        if currentLead is None:
            print ("noooooooooooooooooooooooooooooooo")
            return None, 0
            #Then it didn't work. Recurse?
        currentLead.taken = True
        finalCombo.append(currentLead)
    return finalCombo, 10

def getLeast(classTimes, time):
    min = 10000
    least = None
    for lead in time:
        if not lead.taken:
            y = 0
            for t in lead.availability:
                if t in classTimes:
                    y+=1
            if y<min:
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
#def checkDays(leaderDays,leaderCombo,roomList):
#    temp=[]
#    availRooms=[]
#    availTimes=[]
#    for rooms in roomList:
#        if rooms.taken==False:
#            availRooms.append(rooms)
#            availTimes.append(rooms.time)
#    for leader in leaderCombo:
#        for avail in leader.availability:
#            if avail.split(' ',3)[0] in leaderDays:
#                temp.append(avail)
#    a=Counter(temp).most_common()
#    for x in a:
#        if (x[0]==len(leaderCombo)): #all leaders free at this time
#            for w,z in zip(availRooms,availTimes):
#                if x[1]==z:
#                    w.taken=True
#                    return(1,w)
#    return(0,[])  
    





    
