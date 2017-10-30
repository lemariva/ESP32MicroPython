# ESP32-MicroPython
Basic functions/libraries for ESP32 running MicroPython

ftp.py
------------
Small FTP server
 
###Limitations

*Passive mode only
*A single data connection at a time
*Data transfer is assumed to be in binary mode (ascii setting is ignored)
*Operation blocks the thread
*No authentication support

###What is supported
*Changing directories (cd/CWD)
*Directory listing (ls/LIST with no parameters)
*File retrievals (get/RETR)
*File uploads (put/STOR)


ntptime.py
-------------
Get the epoch time from time1.google.com


timeutils.py
------------
Implements machine.RTC() with ntp_sync(), gmtime() and formatdate() -RFC 2822 date format- as functions


Changelog
------------
Revision 0.2 


License
-----------
Check files