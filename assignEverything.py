#Output format
#Group #, Day, Time, Room
#Pilot leader
#First Last, JHED ID, Hopkins ID, email

def assign(roomList,studentData,finalRoomCombo,finalStudentAssignments,leaderRooms,leaderAssignments,subjectNames):
    for subjectRooms,subjectAssignments,subjectName,subjectLeaders,subjectData,leaderMeeting in zip(finalRoomCombo,finalStudentAssignments,subjectNames,leaderAssignments,studentData,leaderRooms): #iterate by subject
        f=open(subjectName+'.txt','w')
        #print class data
        counter=1
        for room,classAssignments,leader in zip(subjectRooms,subjectAssignments,subjectLeaders):
            f.write('Group '+str(counter)+', '+roomList[room].time+', '+roomList[room].classroom)
            f.write(leader.name) #PILOT leader
            for student in classAssignments:
                f.write(subjectData[student].name+', '+subjectData[student].jhu+', '+subjectData[student].email)
            f.write('\n')
            counter=counter+1
        #print leader data
        f.write('Leaders')
        f.write(leaderMeeting.classroom)
        for x in subjectLeaders:
            f.write(x.name)
        f.close()
