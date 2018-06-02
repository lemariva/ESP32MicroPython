#Copyright [2017] [Mauro Riva <lemariva@mail.com> <lemariva.com>]
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
#
#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.

# boot.py -- run on boot-up
import os
import pycom
from machine import UART
from network import WLAN

uart = UART(0, 115200)
os.dupterm(uart)

pycom.heartbeat(False)

# wlan access
ssid_ = <wlan-ssid>
wp2_pass = <wlan-password>

# configure the WLAN subsystem in station mode (the default is AP)
wlan = WLAN(mode=WLAN.STA)

wlan.scan()     # scan for available networks
wlan.connect(ssid=ssid_, auth=(WLAN.WPA2, wp2_pass))

while not wlan.isconnected():
    pycom.rgbled(0xFF0000)
    pass

pycom.rgbled(0x050505)
