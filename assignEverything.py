def assign(roomList,studentData,finalRoomCombo,finalStudentAssignments,leaderRooms,leaders,subjects):
    for i,j,k,l,m in zip(finalRoomCombo,finalStudentAssignments,subjects,leaders,studentData): #iterate by subject
        for a,b,c in zip(i,j,l):
            roomList[a].group=[m[d] for d in b]
            roomList[a].leader=c
            roomList[a].subject=k

    for z,y,w in zip(leaderRoooms,leaders,subjects):
        roomList[z].leaderMeeting=1
        roomList[z].group=y
        roomList[z].subject=w
    return(roomList)
