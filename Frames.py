import tkinter as tk
from tkinter import filedialog

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
            
        button = tk.Button(self, text=self.text, font=('Comic Sans MS', 10),
                           command=lambda: self.callback())
        button.grid(column=1, row = self.number)
        
            
    def onlift(self, number):
        self.number = int(number)
        root.geometry('{}x{}'.format(self.width, self.height))
        self.onView()
        self.lift()
        
    def openFileFunc(self, entry):
        t = tkFileDialog.askopenfilename(**self.file_opt)
        self.entries.append(t)
        #print entry[0]
        entry[0].set(t)
        
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

        self.p1 = Page(self, 'This is page 1', height=200, width=300)
        self.p2 = getNum(self, 'Next page is 2', height=400, width=300)
        self.p3 = getInfo(self, 'Done', height=400, width=600)
        self.p1.callback = self.p2.onlift
        self.p2.callback = self.p3.onlift
        self.p3.callback = self.leave

        self.p1.place(x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(x=0, y=0, relwidth=1, relheight=1)
        self.p3.place(x=0, y=0, relwidth=1, relheight=1)

        self.p1.onlift()
    
    def leave(self):
        files = {}
        y = 0
        for name in self.p3.names:
            files[name.get()] = self.p3.entries[y]
            y += 1
        #print files
        root.destroy()

root = tk.Tk()
app = App(root)
root.mainloop()

