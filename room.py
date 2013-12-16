class Room:
    def __init__(self,day,time,roomName):
        self.classroom=roomName
        self.time=time
        self.day=day
        self.available=1
        self.group=''
        self.leader=''
        self.subject=''

