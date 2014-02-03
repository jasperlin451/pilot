#Output format
#Group #, Day, Time, Room
#Pilot leader
#First Last, JHED ID, Hopkins ID, email

def assign(roomList,finalRoomCombo,finalStudentAssignments,leaderRooms,leaderAssignments,subjectNames):
    for subjectRooms,subjectAssignments,subjectName,subjectLeaders,leaderMeeting in zip(finalRoomCombo,finalStudentAssignments,subjectNames,leaderAssignments,leaderRooms): #iterate by subject
        f=open(subjectName+'.txt','w')
        #print class data
        counter=1
        for room,classAssignments,leader in zip(subjectRooms,subjectAssignments,subjectLeaders):
            f.write('Group '+str(counter)+', '+roomList[room].time+', '+roomList[room].classroom)
            f.write(leader.name) #PILOT leader
            for student in classAssignments:
                f.write(student.name+', '+student.jhu+', '+student.mail)
            f.write('\n')
            counter=counter+1
        #print leader data
        f.write('Leaders')
        f.write(leaderMeeting.classroom)
        for x in subjectLeaders:
            f.write(x.name)
        f.close()

def assign2(roomList,finalRoomCombo,finalStudentAssignments,subjectNames):
    for subjectRooms,subjectAssignments,subjectName in zip(finalRoomCombo,finalStudentAssignments,subjectNames): #iterate by subject
        f=open(subjectName+'.txt','w')
        #print class data
        counter=1
        for room,classAssignments in zip(subjectRooms,subjectAssignments):
            f.write('Group '+str(counter)+','+roomList[room].time+','+roomList[room].classroom+'\n')
            for student in classAssignments:
                f.write(student.name+', '+student.jhu+', '+student.mail+'\n')
            f.write('\n')
            counter=counter+1
        f.close()

