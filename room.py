class Room:
    def __init__(self,time,roomName):
        self.classroom=roomName
        self.time=time
        self.available=1
        self.group=''
        self.leader=''
        self.subject=''
        self.leaderMeeting=0
