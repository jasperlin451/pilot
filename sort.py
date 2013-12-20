#take in student availabilities for a given subject
#sort students into X number of groups, X is an input
#optimal way to sort data into number of groups
def Sorter(data,numberofgroups,times,roomList):
    i=0 #increment i if there is no more people avail at the time slot
    counter=0 #counter of number of groups made
    while counter<numberofgroups: #keep sorting until number of groups is made
        #check if there is an available room at the time
        #if room is available, sort
        isRoomavail,room,index=checkRoom(roomList,times[i])
        if isRoomAvail==1:
            temp=sorted(data, key=lambda student: student.avail[i])
            #count number of 1 avail and #1 preference
            #if number is greater than 8 make into a group
        else:
            i=i+1
    return(roomList,waitlist,data)

def checkRoom(roomList,checkTime):
    for a in range(len(roomList)):
        if roomList[a].time==checkTime and roomList[a].available==1:
            return (1,roomList[a].classroom,a)
    return (0,'None',[])
