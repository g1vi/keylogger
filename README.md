# Python keylogger
Basic keylogger for red teamers.  

Based on `pynput` listeners, the keylogger stores each keystroke and saves it in a log file on the local drive called `key_record.txt`. A basic sanitization of the keystrokes is performed by removing backspaces and adding newlines to facilitate the analysis of the log.  

If no key is detected in 5 minutes, a line is inserted in the log indicating no activity has been detected in the last 5 minutos. Each 2 hours, the log is sent to an email address. Note if a gmail account is used, the access for low secure apps must be enabled beforehand.  

The following parameters can be configured modificating the script:
- Name of the log file
- Inactivity time (default is 5 mins)
- Email sending frquency (default is 2 hours)
- Email account

### Use
Generate an .exe with `pyinstaller` and execute in target machine.

### License
Feel free to use or modify whenever and wherever you like
