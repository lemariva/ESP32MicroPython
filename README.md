# ESP32-MicroPython
Basic functions/libraries for ESP32/ESP8266 and WiPy2.0/3.0 running MicroPython.

More info: [lemariva.com](https://lemariva.com/micropython)

ftp.py
------------
Small FTP server
 
#### Limitations
* Passive mode only
* A single data connection at a time
* Data transfer is assumed to be in binary mode (ascii setting is ignored)
* Operation blocks the thread
* No authentication support

#### Supports
* Changing directories (cd/CWD)
* Directory listing (ls/LIST with no parameters)
* File retrievals (get/RETR)
* File uploads (put/STOR)


ntptime.py
-------------
Get the epoch time from time1.google.com


timeutils.py
------------
Implements `machine.RTC()` with `ntp_sync()`, `gmtime()` and `formatdate()` -RFC 2822 date format- as functions


md5.py
------------
Encode a string using an MD5 algorithm.
```
>>> import md5
>>> md5.digest('foo')
'acbd18db4cc2f85cedef654fccc4a4d8
```


Changelog
------------
Revision 0.2 


License
-----------
Check files
