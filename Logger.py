import datetime
import logging
import os

from pynput.mouse import Listener


def on_click(x, y, button, pressed):
    if pressed:
        logging.info('{0},{1},{2}'.format(button, x, y))


date = datetime.datetime.now()
log_directory_path = "logs" + os.sep + str(date.day) + "." + str(date.month) + "." + str(date.year)
if not os.path.exists(log_directory_path):
    os.makedirs(log_directory_path)

log_directory_path = log_directory_path + os.sep + "mouse_log"
k = 1
while os.path.exists(log_directory_path + str(k) + ".csv"):
    k = k + 1

log_directory_path = log_directory_path + str(k) + ".csv"
logging.basicConfig(filename=log_directory_path, level=logging.DEBUG, format='%(message)s,%(asctime)s',
                    datefmt="%Y-%m-%d %H:%M:%S")

with Listener(on_click=on_click) as listener:
    listener.join()
