import tkinter as tk
from tkinter import filedialog
import studentImport
import leaderImport
import importRooms
import combinations
import sort
import assignEverything
import time

class Page(tk.Frame):
    def __init__(self, master, text, height, width, *args, **kwargs):
        tk.Frame.__init__(self, *args, borderwidth=20, **kwargs)
        self.height = height
        self.width = width
        button = tk.Button(self, text=text, font=('Comic Sans MS', 20),
                           command=lambda: self.callback())
        button.pack(side="top", fill="both", expand=True)
    def onlift(self):
        root.geometry('{}x{}'.format(self.width, self.height))
        self.lift()

class getInfo(tk.Frame):
    def __init__(self, master, text, height, width, *args, **kwargs):
        self.files = []
        tk.Frame.__init__(self, *args, borderwidth=20, **kwargs)
        self.height = height
        self.width = width
        self.grid()
        self.text = text
        self.file_opt = options = {}
        options['filetypes'] = [('all files','.*'), ('text files', '.txt')]
        options['initialdir'] = '.'

    def onView(self):
        self.entries = []
        self.names = []
        y = 0
        for x in range(0, self.number):
            num = y
            var = tk.StringVar()
            disp = tk.Label(self, textvariable=var)
            disp.grid(column = 0, row = y)
            var.set("Class " + str(y) + " filename")
            self.names.append(tk.Entry(self, width = 20))
            self.names[x].grid(column = 1, row = y)
            openFile = tk.Button(self, text = 'Open File', command=lambda entry = [var, y]: self.openFileFunc(entry))
            openFile.grid(column = 2, row = y)
            y += 1
        
        self.leadSheet = tk.StringVar()
        self.dispLead = tk.Label(self, textvariable=self.leadSheet)
        self.dispLead.grid(column = 0, row = self.number)
        self.leadSheet.set("Leader Spreadsheet filename")
        leadFile = tk.Button(self, text = 'Open File', command=lambda: self.updateLead())
        leadFile.grid(column = 2, row = self.number)   
        
        self.roomSheet = tk.StringVar()
        self.dispRoom = tk.Label(self, textvariable=self.roomSheet)
        self.dispRoom.grid(column = 0, row = self.number+1)
        self.roomSheet.set("Room Spreadsheet filename")
        roomFile = tk.Button(self, text = 'Open File', command=lambda: self.updateRoom())
        roomFile.grid(column = 2, row = self.number+1) 
         
        button = tk.Button(self, text=self.text, font=('Comic Sans MS', 10),
                           command=lambda: self.callback())
        button.grid(column=1, row = self.number+2)
        
    
    def updateRoom(self):
        self.roomSheet.set(filedialog.askopenfilename(**self.file_opt))
    
    def updateLead(self):
        self.leadSheet.set(filedialog.askopenfilename(**self.file_opt))
        
    def onlift(self, number):
        self.number = int(number)
        root.geometry('{}x{}'.format(self.width, self.height))
        self.onView()
        self.lift()
        
    def openFileFunc(self, entry):
        t = filedialog.askopenfilename(**self.file_opt)
        self.entries.append(t)
        #print entry[0]
        entry[0].set(t)
        
class getNum(tk.Frame):
    def __init__(self, master, text, height, width, *args, **kwargs):
        tk.Frame.__init__(self, *args, borderwidth=20, **kwargs)
        self.height = height
        self.width = width
        self.grid()
	    
        classNum = tk.Entry(self)
        classNum.insert(0, "0")
	    
        classNum.grid(column=1, row=0)
        button = tk.Button(self, text=text, font=('Comic Sans MS', 10), command=lambda: self.callback(classNum.get()))
        button.grid(column=1, row = 1)   
        
    def onlift(self):
        root.geometry('{}x{}'.format(self.width, self.height))
        self.lift()
        
class getClasses(tk.Frame):
    def __init__(self, master, text, size, number, height, width, *args, **kwargs):
        tk.Frame.__init__(self, *args, borderwidth=2, **kwargs)
        self.left = number
        self.height = height
        self.width = width
        self.number = number
        self.text = text
        self.grid()
        self.entries = []
        
        for x in range(0, len(size)):
            disp = tk.Label(self, text=size[x][0])
            disp.grid(column = 0, row = x)
            disp2 = tk.Label(self, text=size[x][1])
            disp2.grid(column = 1, row = x)
            num = tk.Entry(self)
            num.insert(0,"0")
            num.grid(column = 2, row = x)
            self.entries.append(num)
            
        update = tk.Button(self, text = "Update Totals", command=lambda:self.update())
        update.grid(column = 2, row = len(size))
        total = tk.Label(self, text="Total Number of Leaders: " + str(self.number))
        total.grid(column = 1, row = len(size)+1)
        self.remaining = tk.StringVar()
        self.remainingleads = tk.Label(self, textvariable=self.remaining)
        self.remainingleads.grid(column = 2, row = len(size)+1)
        self.remaining.set("Leaders Remaining: " + str(number))
        
        button = tk.Button(self, text=self.text, font=('Comic Sans MS', 10),
                           command=lambda: self.check())
        button.grid(column=1, row = self.number+2)
   
    def check(self):
        self.update()
        if (1==1): # (self.left == 0):
            self.callback()
     
    def update(self):
        t = 0
        for e in self.entries:
            t+= int(e.get())
        self.left = self.number - t
        self.remaining.set("Leaders Remaining: " + str(self.number -t))
        
    def onlift(self):
            root.geometry('{}x{}'.format(self.width, self.height))
            self.lift()

class App(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.p1 = Page(self, 'Welcome to the Scheduler. Click to Continue', height=400, width=600)
        self.p2 = getNum(self, 'Continue to file selection', height=400, width=600)
        self.p3 = getInfo(self, 'Done', height=400, width=600)
        self.p1.callback = self.p2.onlift
        self.p2.callback = self.p3.onlift
        self.p3.callback = self.getSizes

        self.p1.place(x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(x=0, y=0, relwidth=1, relheight=1)
        self.p3.place(x=0, y=0, relwidth=1, relheight=1)

        self.p1.onlift()
    
    def getSizes(self):
        files = {}
        y = 0
        self.returns = []
        size = []
        for name in self.p3.names:
            files[name.get()] = self.p3.entries[y]
            y += 1
        x = 0
        for f in files:
            self.returns.append(studentImport.scan(files[f], f))
            size.append([f, len(self.returns[x][0])])
            x+=1
        a,b,c = leaderImport.scan(self.p3.leadSheet.get())
        number = len(c)
        self.p4 = getClasses(self, 'Calculate', size, number, height=400, width=600)
        self.p4.place(x=0, y=0, relwidth=1, relheight=1)
        self.p4.callback = self.runCombos
        self.p4.onlift()
        
    def runCombos(self):
        starttime=time.time()
        names = []
        for i in self.p3.names:
            names.append(i.get())
        roomList, roomCount = importRooms.scan(self.p3.roomSheet.get())
        combos = []
        y = 0
        sizes = []
        for x in self.returns:
            print (str(x[1]) + str(int(self.p4.entries[y].get())) + str(x[0]) + str(roomCount))
            combos.append(combinations.combinations(x[1], int(self.p4.entries[y].get()) ,x[0] ,roomCount))
            sizes.append(int(self.p4.entries[y].get()))
            y+=1
        finalRoomCombo,finalStudentAssignments,finalWaitList,LeaderCombo=sort.Sorter([m[0] for m in self.returns],combos,names,sizes,roomList,[n[1] for n in self.returns])
        root.destroy()
        leaderRooms,leaders=assign.assignLeaders(c,LeaderCombo,roomList,sizes,finalRoomCombo)
        #assign everything
        roomList=assignEverything.assign(roomList,self.returns,finalRoomCombo,finalStudentAssignments,leaderRooms,leaders,names)
        for test in roomList:
             print(test.subject,test.time,len(test.group),test.leader)
        print(time.time()-starttime)
root = tk.Tk()
app = App(root)
root.mainloop()

