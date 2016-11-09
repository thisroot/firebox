## **FireBox**

Python library for connecting PC to Arduino through Serial port

``` python
import firebox as fb

serPort = fb.findDevice('stimulator')
if(serPort):
    data = []
    data.append("<fire,200,5>")
    fb.sendMessage(serPort,data)
```


#### Features:
* Serch device on a name
* Packet transmission commands to device

#### <i class="icon-anchor"> Import library
``` python
import firebox as fb
```
#### <i class="icon-search"> Find device

``` python
serPort = fb.findDevice('stimulator')
```

#### <i class="icon-male"> Request body

``` python
data = []
data.append("<fire,200,5>")
```
The request concluded in stop characters ** <...> ** it takes 3 arguments, first is a string, other is integers.

#### <i class="icon-flash"> Command

``` python
fb.sendMessage(serPort,data)
```
If the data transfer is successful, you can to see next message in console, 
```
=========== 
Sent from PC -- LOOP NUM 0 TEST STR <fire,200,5>
Reply Received: fired
Timing: 0.213000059128
===========
```

#### <i class="icon-book">  Methods.

#####  List of ports
``` python
serialPorts()
```
#####  Open port
``` python
openSerial(serPort, baudRate)
```
#####  send message on to the device
``` python
sendToArduino(sendStr)
```
##### recive message
``` python
recvFromArduino()
```
##### waiting device
``` python
waitForArduino()
```
##### Send message
``` python
sendMessage(serPort,td, baudRate=19200)
```
##### Find device
``` python
findDevice(devName,baudRate=19200,numDev=0)
```

