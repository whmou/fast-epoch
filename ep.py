import time
import sys
import os

def notify(title, message):
    os.system(
        "osascript -e 'display notification \"{0}\" with title \"{1}\"'".format(message, title))

try:
    input=int(sys.argv[1])
    if len(sys.argv[1]) > 12:
        input = input/1000
    date= time.strftime('%Y/%m/%d %H:%M:%S',  time.gmtime(input))
    notify(input, date)
except:
    pass
