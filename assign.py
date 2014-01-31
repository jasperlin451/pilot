#subjectData is number of groups per subject
#times is pilot meetingTimes per subject
from itertools import combinations, permutations

def assignLeaders(leaderData, timeCombos, roomList, subjectData, times):
    max = 0
    best = None
    best2 = None
    for combo in timeCombos:
        worked = attempt(combo, leaderData, roomList, subjectData, times)
        if worked[0] > max:
            best = combo
            best2 = worked[1]
    return best, best2
    
def attempt(combo, leaderData, roomList, subjectData, times):
    #calculate value based on leader assignment returned from recursive assigning
    x = recurse(combo, leaderData, roomList, subjectData, times,0)
    return(x)
    
def recurse(combo, leaderData, roomList, subjectData, times, index):
    subject = subjectData[index]
    leadTime = roomList[combo[index]].time
    classTimes = times[index]
    leads = []
    value = 0
    max = 0
    best = []
    leaderData=sorted(leaderData, key=lambda leader: leader.subjectPreference[index])
    for leader in leaderData:
        if (leadTime in leader.availability) and (leader.subjectPreference[index] < 3) and (leader.taken is False):
            leads.append(leader)
            leader.taken == True
    if (index == len(subjectData) - 1):         #Base Case
        combo, value = checkCombos(leads, subject, classTimes, roomList, index)    
        if combo is None:
            return 0, None
        else:
            temp = []
            temp.append(combo)
            return value, temp
        
    possibles = combinations(leads, subject)
    for possible in possibles:
        combo = checkCombos(possible, subject, classTimes, roomList, index)
        if not (combo[0] is None):
            value = combo[1]
            afterValue, leaderList = recurse(combo, leaderData, roomList, subjectData, times, index+1)
            if not (afterValue is 0):
                if (index is 0):
                    if (value + afterValue) > max:
                        best = leaderList.insert(0, combo[1])
                else:
                    return value + afterValue, leaderList.insert(0, combo[1])
    
    if (index is 0):
        return max, best
    else:
        return 0, None
        
def checkCombos(leads, subject, classTimes, roomList, index):
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
        if w is True:
            return perm, value
            
    return None, 0
