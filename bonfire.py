from tkinter import*
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from sys import argv
from shutil import copy
import os
import time
from threading import Timer
from threading import Thread, Event

###### ROOT SETTINGS ########
root = Tk()
root.title('Filelink Shrine')
root.geometry('250x400')
root.resizable(0,0)
root.configure(background='#563B2A')
root.iconbitmap('FS.ico')

bg_image = PhotoImage(file="gui.gif")
background = Label(root, image=bg_image)
background.place(x = 0, y = 0)


#############################

######## INIT VARS ##########

#############################

######### FUNCTIONS #########
class Repeat(Thread): # (timer)
    def __init__(self,delay,function,*args,**kwargs):
        Thread.__init__(self)
        self.abort = Event()
        self.delay = delay
        self.args = args
        self.kwargs = kwargs
        self.function = function
    def stop(self):
        self.abort.set()
    def run(self):
        while not self.abort.isSet():
            self.function(*self.args,**self.kwargs)
            self.abort.wait(self.delay)

def chooseDst1():
    dstDir = askdirectory()
    chooseDst1.dstDir = dstDir
    chooseDst1.real = True
    Destination1.configure(image=highlighted)
    print(dstDir)
def chooseDst2():
    dstDir = askdirectory()
    chooseDst2.dstDir = dstDir
    chooseDst2.real = True
    Destination2.configure(image=highlighted)
    print(dstDir)
def chooseDst3():
    dstDir = askdirectory()
    chooseDst3.dstDir = dstDir
    chooseDst3.real = True
    Destination3.configure(image=highlighted)
    print(dstDir)
def chooseDst4():
    dstDir = askdirectory()
    chooseDst4.dstDir = dstDir
    chooseDst4.real = True
    Destination4.configure(image=highlighted)
    print(dstDir)
def chooseDst5():
    dstDir = askdirectory()
    chooseDst5.dstDir = dstDir
    chooseDst5.real = True
    Destination5.configure(image=highlighted)
    print(dstDir)
def chooseDst6():
    dstDir = askdirectory()
    chooseDst6.dstDir = dstDir
    chooseDst6.real = True
    Destination6.configure(image=highlighted)
    print(dstDir)
def chooseDst7():
    dstDir = askdirectory()
    chooseDst7.dstDir = dstDir
    chooseDst7.real = True
    Destination7.configure(image=highlighted)
    print(dstDir)
def chooseDst8():
    dstDir = askdirectory()
    chooseDst8.dstDir = dstDir
    chooseDst8.real = True
    Destination8.configure(image=highlighted)
    print(dstDir)

def copyFile(): 
    copy(srcFile, chooseDst1.dstDir)
    print('updated destination 1 copy\n')
def copyFile2(): 
    copy(srcFile, chooseDst2.dstDir)
    print('updated destination 2 copy\n')
def copyFile3(): 
    copy(srcFile, chooseDst3.dstDir)
    print('updated destination 3 copy\n')
def copyFile4(): 
    copy(srcFile, chooseDst4.dstDir)
    print('updated destination 4 copy\n')

def srcCopy5(): 
    timestr = time.strftime("(%Y.%m.%d)-(%Hh.%Mm.%Ss)")
    dstName = ('/' + fileTitle + timestr + fileExt)
    copy(srcFile, chooseDst5.dstDir + dstName)
    print('added source control copy to destination 5\n')
def srcCopy6(): 
    timestr = time.strftime("(%Y.%m.%d)-(%Hh.%Mm.%Ss)")
    dstName = ('/' + fileTitle + timestr + fileExt)
    copy(srcFile, chooseDst6.dstDir + dstName)
    print('added source control copy to destination 6\n')
def srcCopy7(): 
    timestr = time.strftime("(%Y.%m.%d)-(%Hh.%Mm.%Ss)")
    dstName = ('/' + fileTitle + timestr + fileExt)
    copy(srcFile, chooseDst7.dstDir + dstName)
    print('added source control copy to destination 7\n')
def srcCopy8(): 
    timestr = time.strftime("(%Y.%m.%d)-(%Hh.%Mm.%Ss)")
    dstName = ('/' + fileTitle + timestr + fileExt)
    copy(srcFile, chooseDst8.dstDir + dstName)
    print('added source control copy to destination 8\n')

def timedCopy():    
    atLeastOne = 0

    try:
        seconds = int(Timer.get())
        minutes = (seconds*60)      
    except ValueError:
        messagebox.showinfo("Brings me souls.", 
        "Please enter an interval length in minutes. For example:\n50\nWould set a 50 minute interval between copies.")
        sys.exit()
    else:
        pass

    try:
        chooseDst1.real
    except AttributeError:
        print('Destination 1 has not been selected.')
        atLeastOne += 1
    else:
        r = Repeat(minutes,copyFile)
        r.start()

    try:
        chooseDst2.real
    except AttributeError:
        print('Destination 2 has not been selected.')
        atLeastOne += 1
    else:
        r = Repeat(minutes,copyFile2)
        r.start()

    try:
        chooseDst3.real
    except AttributeError:
        print('Destination 3 has not been selected.')
        atLeastOne += 1
    else:
        r = Repeat(minutes,copyFile3)
        r.start()
    
    try:
        chooseDst4.real
    except AttributeError:
        print('Destination 4 has not been selected.')
        atLeastOne += 1
    else:
        r = Repeat(minutes,copyFile4)
        r.start()
    
    try:
        chooseDst5.real
    except AttributeError:
        print('Destination 5 has not been selected.')
        atLeastOne += 1
    else:
        r = Repeat(minutes,srcCopy5)
        r.start()

    try:
        chooseDst6.real
    except AttributeError:
        print('Destination 6 has not been selected.')
        atLeastOne += 1
    else:
        r = Repeat(minutes,srcCopy6)
        r.start()

    try:
        chooseDst7.real
    except AttributeError:
        print('Destination 7 has not been selected.')
        atLeastOne += 1
    else:
        r = Repeat(minutes,srcCopy7)
        r.start()

    try:
        chooseDst8.real
    except AttributeError:
        print('Destination 8 has not been selected.')
        atLeastOne += 1
    else:
        r = Repeat(minutes,srcCopy8)
        r.start()
    
    if(atLeastOne >= 8):
        messagebox.showinfo("Brings me vessels.", 
        "Please choose at least one destination.")
        sys.exit()
    else:
        Start.configure(image = stopbutton, command=stopProcess)

def stopProcess():
    try:
        chooseDst1.real
    except AttributeError:
        print('Destination 1 has not been selected.')
    else:
        copyFile()

    try:
        chooseDst2.real
    except AttributeError:
        print('Destination 2 has not been selected.')
    else:
        copyFile2()

    try:
        chooseDst3.real
    except AttributeError:
        print('Destination 3 has not been selected.')
    else:
        copyFile3()
    
    try:
        chooseDst4.real
    except AttributeError:
        print('Destination 4 has not been selected.')
    else:
        copyFile4()
    
    try:
        chooseDst5.real
    except AttributeError:
        print('Destination 5 has not been selected.')
    else:
        srcCopy5()

    try:
        chooseDst6.real
    except AttributeError:
        print('Destination 6 has not been selected.')
    else:
        srcCopy6()

    try:
        chooseDst7.real
    except AttributeError:
        print('Destination 7 has not been selected.')
    else:
        srcCopy7()

    try:
        chooseDst8.real
    except AttributeError:
        print('Destination 8 has not been selected.')
    else:
        srcCopy8()
    
    messagebox.showinfo("Farewell ashen one.", "Final copies made. Ready to quit.")
    os._exit(0)   

def openReadme():
   os.startfile('readme.txt')
#############################

####### DEFINE BUTTONS ######
## Images ##
highlighted = PhotoImage(file="buttonhighlight.gif")
unhighlighted = PhotoImage(file="buttondark.gif")
startbutton = PhotoImage(file="startbutton.gif")
stopbutton = PhotoImage(file="stopbutton.gif")
questionbutton = PhotoImage(file='questionbutton.gif')

Destination1 = Button(root, 
        command = chooseDst1,
        image = unhighlighted,
        relief = FLAT, bd = 0, highlightthickness = 0, 
        highlightcolor = '#563B2A', highlightbackground = '#563B2A',
        bg = '#563B2A'       
        )
Destination2 = Button(root,  
        command = chooseDst2,
        image = unhighlighted,
        relief = FLAT, bd = 0, highlightthickness = 0, 
        highlightcolor = '#563B2A', highlightbackground = '#563B2A',
        bg = '#563B2A'        
        )
Destination3 = Button(root,  
        command = chooseDst3,
        image = unhighlighted,
        relief = FLAT, bd = 0, highlightthickness = 0, 
        highlightcolor = '#563B2A', highlightbackground = '#563B2A',
        bg = '#563B2A'        
        )
Destination4 = Button(root,  
        command = chooseDst4,
        image = unhighlighted,
        relief = FLAT, bd = 0, highlightthickness = 0, 
        highlightcolor = '#563B2A', highlightbackground = '#563B2A',
        bg = '#563B2A'        
        )
Destination5 = Button(root,  
        command = chooseDst5,
        image = unhighlighted,
        relief = FLAT, bd = 0, highlightthickness = 0, 
        highlightcolor = '#563B2A', highlightbackground = '#563B2A',
        bg = '#563B2A'        
        )
Destination6 = Button(root,  
        command = chooseDst6,
        image = unhighlighted,
        relief = FLAT, bd = 0, highlightthickness = 0, 
        highlightcolor = '#563B2A', highlightbackground = '#563B2A',
        bg = '#563B2A'        
        )
Destination7 = Button(root,  
        command = chooseDst7,
        image = unhighlighted,
        relief = FLAT, bd = 0, highlightthickness = 0, 
        highlightcolor = '#563B2A', highlightbackground = '#563B2A',
        bg = '#563B2A'        
        )
Destination8 = Button(root,  
        command = chooseDst8,
        image = unhighlighted,
        relief = FLAT, bd = 0, highlightthickness = 0, 
        highlightcolor = '#563B2A', highlightbackground = '#563B2A',
        bg = '#563B2A'        
        )

Timer = Entry(root,
        relief = FLAT, bd = 0, highlightthickness = 0,
        width = 7, justify = CENTER,
        font = 'roboto'
        )
Start = Button(root,  
        command = timedCopy,
        image = startbutton, 
        relief = FLAT, bd = 0, highlightthickness = 0, 
        highlightcolor = '#563B2A', highlightbackground = '#563B2A', 
        bg = '#563B2A'
        )
Question = Button(root,  
        command = openReadme,
        image = questionbutton, 
        relief = FLAT, bd = 0, highlightthickness = 0, 
        highlightcolor = '#563B2A', highlightbackground = '#563B2A', 
        bg = '#563B2A'
        )
####### PLACE BUTTONS #######
Question.place(x = 216, y = 10)
Timer.place(x= 159, y = 67)
Destination1.place(x = 27, y = 174)
Destination2.place(x = 79, y = 174)
Destination3.place(x = 27, y = 238)
Destination4.place(x = 79, y = 238)
Destination5.place(x = 131, y = 174)
Destination6.place(x = 183, y = 174)
Destination7.place(x = 131, y = 238)
Destination8.place(x = 183, y = 238)
Start.place(x = 52, y = 346)
#############################

######### ON START ##########
srcFile = filedialog.askopenfilename(
    initialdir = "C:",
    title = "Speak thine heart's desired file to manage.",
    filetypes = (("text files","*.txt"),("doc files","*.doc"),
    ("docx files","*.docx"),("all files","*.*"))
    )
fileSep = os.path.splitext(srcFile)
fileExt = (fileSep[1])
fileNam = os.path.basename(srcFile)
fileTitle = os.path.splitext(fileNam)[0]

print(srcFile)
print(fileExt)
#############################

root.mainloop()
