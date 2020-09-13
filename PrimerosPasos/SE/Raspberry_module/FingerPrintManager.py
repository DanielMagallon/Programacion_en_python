from pyfingerprint.pyfingerprint import PyFingerprint

import os
import threading
import time

from Sockets_module.sconnection_client import Socket_client,Socket_wait2wait
#from ..Sockets_module.sconnection_client import Socket_client,Socket_wait2wait

import socket
from tkinter import Tk,Label,Text,RIDGE,SUNKEN,Button,StringVar,messagebox,Entry
from PIL import ImageTk,Image

def getImage(imagePath) -> ImageTk.PhotoImage:
    img = Image.open(imagePath).resize((200, 200), Image.ANTIALIAS)

    return ImageTk.PhotoImage(image=img)

class GUI_signup():
    from Mysqsl_module import Connector as consql

    def __init__(self,clear: bool):

        self.id_user = -1
        self.checked = False

        self.reader = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

        if clear:
            self.reader.clearDatabase()

        if (self.reader.verifyPassword() == False):
           raise ValueError('The given fingerprint sensor password is wrong!')

        options = ['User name:','User password:','Check in time:','Departure time:']
        self.txtWidgets = {}

        self.gui = Tk(className='Sign up a new fingerprint')


        self.gui.geometry("700x600+450+70")
        self.gui.config(bg="#3465A4")

        self.photo = getImage(os.path.dirname(__file__)+"/reader.gif")
        self.gui.iconphoto(False, self.photo)

        r = 0
        for op in options:
            lbl = Label(text=op, relief=RIDGE)
            lbl.grid(row=r, column=0,padx=10, pady=10)
            lbl.config(width=20,height=2)
            txt = Text(bg="white",relief=SUNKEN,  width=50,height=2,fg="black")

            txt.grid(row=r, column=1)
            self.txtWidgets.update({op: txt})
            r+=1

        self.txtVarAction = StringVar()
        self.lblAction = Label(bg="#3465A4",fg="white",textvariable=self.txtVarAction)
        self.lblAction.grid(row=r,column=0,padx=10,pady=20)
        self.txtVarAction.set("Not reading finger yet")
        r+=1

        self.lblImageFinger = Label(bg="#729FCF",fg="black")
        self.lblImageFinger['image'] = self.photo
        self.lblImageFinger.grid(row=r, column=0, padx=10, pady=10)

        self.btnReadFinger = Button(text="Read fingerprint",command=self.startFingerPrint)
        self.btnReadFinger.grid(row=r+1, column=0, padx=10)
        self.btnReadFinger.config(width=20, height=2)

        btnStore = Button(text="Store data in database",command=self.storageDatabase)
        btnStore.grid(row=r,column=1)



    def storageDatabase(self):

        for txts in self.txtWidgets.values():

            if not txts.get(1.0,'end').strip():
                messagebox.showerror(message="All data files must be typed",
                                     title="Values empty")
                return

        if self.id_user==-1:
            messagebox.showerror(message="You must scan your finger to get your id",
                                 title="Not scanned finger yet")
            return

        msg,flag = self.consql.exeProcedure('Insert_user',[self.id_user,
                       self.txtWidgets['User name:'].get(1.0,'end').strip(),
                       self.txtWidgets['User password:'].get(1.0, 'end').strip(),
                       self.txtWidgets['Check in time:'].get(1.0, 'end').strip(),
                       self.txtWidgets['Departure time:'].get(1.0, 'end').strip()],(0,1))

        if flag==0:
            messagebox.showerror(title='Error in insertion',message=msg)
        else:
            self.id_user=-1
            self.lblImageFinger['image']=self.photo
            messagebox.showinfo(title='All is ok',message=msg)

    def startFingerPrint(self):
        threading.Thread(target=self.readFingerPrint, args=("Thread Reader")).start()

    def readFingerPrint(self,*argss):

        try:

            print('Waiting for finger...')
            self.txtVarAction.set("Waiting for finger...")

            while (self.reader.readImage() == False):
                pass

            self.reader.convertImage(0x01)

            result = self.reader.searchTemplate()
            positionNumber = result[0]

            if (positionNumber >= 0):
                print('Template already exists at position #' + str(positionNumber))
                self.txtVarAction.set("Template already\nexists")
                return

            print('Remove finger...')
            self.txtVarAction.set("Remove finger...")
            time.sleep(2)

            print('Waiting for same finger again...')
            self.txtVarAction.set('Waiting for same finger again...')

            ## Wait that finger is read again
            while (self.reader.readImage() == False):
                pass

            print('Downloading image (this take a while)...')
            self.txtVarAction.set('Downloading image\n(this take a while)...')

            imagePath = os.path.dirname(__file__)+"/fingerprint.bmp"
            self.reader.downloadImage(imagePath)

            self.reader.convertImage(0x02)

            if (self.reader.compareCharacteristics() == 0):
                print('Fingers do not match')
                self.txtVarAction.set('Fingers do not match')
                return

            self.reader.createTemplate()

            self.id_user = self.reader.storeTemplate()+1

            print('The image was saved to "' + imagePath + '".')
            print('Finger enrolled successfully!')

            self.txtVarAction.set('Finger enrolled successfully!')

            self.fingerImage = getImage(imagePath)
            self.lblImageFinger['image'] = self.fingerImage
            print('New template position #' + str(self.id_user-1))


        except Exception as e:
            print('Operation failed!')
            self.txtVarAction.set('Operation failed!')
            print('Exception message: ' + str(e))
            return

    def run(self):
        self.gui.mainloop()



class FPManager(Tk):

    import pickle

    def __init__(self):
        Tk.__init__(self)
        self.geometry('+500+100')
        self.txtVarAction = StringVar(value="Not finger print yet")
        self.lblAction = Label(fg="white")
        self.lblAction['textvariable']=self.txtVarAction
        self.lblAction.grid(row=0,column=0,padx=10,pady=15)

        self.gif = getImage(os.path.dirname(__file__)+"/reader.gif")
        self.lblImageFinger = Label()
        self.lblImageFinger['image']=self.gif
        self.lblImageFinger.grid(row=1,column=0,padx=10,pady=5)

        self.btnRead = Button(text="Read finger",command=self.startReader)
        self.btnRead.grid(row=2,column=0,pady=10)

        self.txtVarUser = StringVar(value="Not user identified yet")
        self.lblUser = Label(fg="white",textvariable=self.txtVarUser)
        self.lblUser.grid(row=0,column=1,padx=10)

        self.txtVarPassword = StringVar()
        self.txtInPassword = Entry(width=30,textvariable=self.txtVarPassword)
        self.txtInPassword['state']='disabled'
        self.txtInPassword.grid(row=1,column=1,padx=5)

        self.btnChekAcces = Button(text="Access",command=self.checkAccess)
        self.btnChekAcces['state'] = 'disabled'
        self.btnChekAcces.grid(row=2,column=1,padx=10,pady=5)

        self.sclient = Socket_client("Thread_client:daniel",('localhost',1234),functionGet=self.getData)

        self.reader = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

            # f.clearDatabase()
        if (self.reader.verifyPassword() == False):
           raise ValueError('The given fingerprint sensor password is wrong!')

    def checkAccess(self):
        self.sclient.sendData(data=("check-pass", (self.positionNumber + 1,self.txtVarPassword.get())))

    def startReader(self):
        threading.Thread(target=self.setFinger,args=("Thread Reader")).start()

    def setFinger(self,*args):
        try:
            print('Waiting for finger...')
            self.txtVarAction.set('Waiting for finger...')
            ## Wait that finger is read
            while (self.reader.readImage() == False):
                pass

            ## Converts read image to characteristics and stores it in charbuffer 1
            self.reader.convertImage(0x01)

            ## Searchs template
            result = self.reader.searchTemplate()

            self.positionNumber = result[0]
            #accuracyScore = result[1]

            if (self.positionNumber == -1):
                self.txtVarAction.set('No match found')
                print('No match found!')
            else:
                print("Match found")
                self.sclient.sendData(data=("check-id",(self.positionNumber+1,)))



        except IOError as e:
            print('Operation failed!')
            self.txtVarAction.set('Operation failed')
            print('Exception message: ' + str(e))




    def getData(self,data):

        msgTuple = self.pickle.loads(data)

        if msgTuple[0]=='check-id':
            self.txtInPassword['state'] = 'normal'
            self.txtVarUser.set('Welcome '+msgTuple[1])
            self.btnChekAcces['state'] = 'normal'

        elif msgTuple[0]=='check-pass':
            if msgTuple[1]:
                messagebox.showinfo(title="Welcome",message="Access successfully")
            else:
                messagebox.showerror(title="Error",message="Access denied")


    def run(self):
        self.mainloop()



#app = GUI_signup(True)
#app.run()

app = FPManager()
app.run()