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

md5hash.py
------------
Encode a string using an MD5 algorithm.
```
>>> from md5hash import md5
>>> m = md5()
>>> m.update('foo')
>>> m.hexdigest()
'acbd18db4cc2f85cedef654fccc4a4d8'
```

maes.py
------------
Simple AES cipher implementation in pure Python following PEP-272 API

```
import maes
import ubinascii

class AESCipher():
    def __init__(self, key):
        self.bs = 16
        self.key = key

    def encrypt(self, raw):
        raw = self._pad(raw)
        cipher = maes.new(self.key, maes.MODE_ECB)
        crypted_text = cipher.encrypt(raw)
        crypted_text_b64 = ubinascii.b2a_base64(crypted_text)
        return crypted_text_b64

    def decrypt(self, enc):
        enc = ubinascii.a2b_base64(enc)
        cipher = maes.new(self.key, maes.MODE_ECB)
        raw = cipher.decrypt(enc)
        return self._unpad(raw).decode('utf-8')

    def _pad(self, s):
        padnum = self.bs - len(s) % self.bs
        return s + padnum * chr(padnum).encode()

    @staticmethod
    def _unpad(dec):
        s = bytes(bytearray(dec))
        return s[:-ord(s[len(s)-1:])]


>>> key = b'0cc103aaf3df5dff'
>>> cypher = AESCipher(key)
>>> enc = cypher.encrypt(b'foo')
>>> print(enc)
b'S8IpdJ+PpVYutZB5sWXGkA==\n'
>>> cypher.decrypt(enc)
'foo'
```

Changelog
------------
Revision 0.3


License
-----------
Check files
