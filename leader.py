class Leader:
    def __init__(self,firstname,lastname,subjectPreference,availability):
        self.name=firstname+' '+lastname
        self.subjectPreference = subjectPreference
        self.availability = availability
        self.taken = False
