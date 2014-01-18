import Tkinter as tk
import tkFileDialog
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
        tk.Frame.__init__(self, *args, borderwidth=20, **kwargs)
        self.height = height
        self.width = width
        self.grid()
        self.text = text
        '''
        entries = []
        self.classOneVar = tk.StringVar()
        self.classOne = tk.Label(self,textvariable=self.classOneVar)
        self.classOne.grid(column=0,row=0,sticky='EW')
        self.classOneVar.set(u"Class One Filename !")
        
        self.openFile = tk.Button(self, text='Open File', command=self.openFileFunc)'''
        self.file_opt = options = {}
        options['filetypes'] = [('all files','.*'), ('text files', '.txt')]
        options['initialdir'] = '.'
        '''
        self.openFile.grid(column = 1, row=0,sticky = 'EW')
        
        button = tk.Button(self, text=text, font=('Comic Sans MS', 10),
                           command=lambda: self.callback())
        button.grid(column=1, row = 1)
        '''
        
    def onView(self):
        self.entries = []
        y = 0
        for x in range(0, self.number):
            num = y
            var = tk.StringVar()
            disp = tk.Label(self, textvariable=var)
            disp.grid(column = 0, row = y)
            var.set("Class " + str(y) + " filename")
            openFile = tk.Button(self, text = 'Open File', command=lambda: self.openFileFunc(var))
            openFile.grid(column = 1, row = y)
            y += 1
            self.entries.append([num, var,disp, openFile])
        '''y = 0
        for x in range(0, self.number):
            openFile = tk.Button(self, text = 'Open File', command=lambda: self.openFileFunc(y))
            openFile.grid(column = 1, row = y)
            self.entries[y].append(openFile)
            y+=1'''
            
        button = tk.Button(self, text=self.text, font=('Comic Sans MS', 10),
                           command=lambda: self.callback())
        button.grid(column=1, row = self.number)
        
            
    def onlift(self, number):
        self.number = int(number)
        root.geometry('{}x{}'.format(self.width, self.height))
        self.onView()
        self.lift()
        
    def openFileFunc(self, y):
        print y
        y.set(tkFileDialog.askopenfilename(**self.file_opt))
        
class getNum(tk.Frame):
    def __init__(self, master, text, height, width, *args, **kwargs):
        tk.Frame.__init__(self, *args, borderwidth=20, **kwargs)
        self.height = height
        self.width = width
        self. grid()
	    
        classNum = tk.Entry(self)
        classNum.insert(0, "0")
	    
        classNum.grid(column=1, row=0)
        button = tk.Button(self, text=text, font=('Comic Sans MS', 10), command=lambda: self.callback(classNum.get()))
        button.grid(column=1, row = 1)
    
        
    def onlift(self):
        root.geometry('{}x{}'.format(self.width, self.height))
        self.lift()

class App(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        p1 = Page(self, 'This is page 1', height=200, width=300)
        p2 = getNum(self, 'Next page is 2', height=400, width=300)
        p3 = getInfo(self, 'Done', height=400, width=600)
        p1.callback = p2.onlift
        p2.callback = p3.onlift
        p3.callback = p1.onlift

        p1.place(x=0, y=0, relwidth=1, relheight=1)
        p2.place(x=0, y=0, relwidth=1, relheight=1)
        p3.place(x=0, y=0, relwidth=1, relheight=1)

        p1.onlift()

root = tk.Tk()
app = App(root)
root.mainloop()

