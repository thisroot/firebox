import sys
import glob
import serial
import time

#=====================================
#  Support functions
#=====================================

def serialPorts():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

#=====================================
#  Excange functions
#=====================================
def openSerial(serPort, baudRate):
    global ser
    ser = serial.Serial(serPort, baudRate)
    waitForArduino()
    return ser


def sendToArduino(sendStr):
    ser.write(sendStr)

#======================================

def recvFromArduino():
    global startMarker, endMarker
    startMarker = 60
    endMarker = 62

    ck = ""
    x = "z" # any value that is not an end- or startMarker
    byteCount = -1 # to allow for the fact that the last increment will be one too many

    # wait for the start character
    while  ord(x) != startMarker:
        x = ser.read()

    # save data until the end marker is found
    while ord(x) != endMarker:
        if ord(x) != startMarker:
            ck = ck + x
            byteCount += 1
        x = ser.read()
        
    return(ck)
    print(ck)

#============================

def waitForArduino():
    # wait until the Arduino sends 'Arduino Ready' - allows time for Arduino reset
    # it also ensures that any bytes left over from a previous message are discarded
        global startMarker, endMarker
        startMarker = 60
        endMarker = 62

        msg = ""
        while msg.find("Arduino is ready") == -1:
            while ser.inWaiting() == 0:
                pass
            msg = recvFromArduino()

#======================================

def sendMessage(serPort,td, baudRate=19200):
    
    ser = openSerial(serPort,baudRate)
    numLoops = len(td)
    waitingForReply = False
    n = 0
    start = time.time()
    while n < numLoops:
        
        
        teststr = td[n]

        if waitingForReply == False:
            sendToArduino(teststr)
            print "==========="
            print "Sent from PC -- LOOP NUM " + str(n) + " TEST STR " + teststr
            waitingForReply = True

        if waitingForReply == True:
            while ser.inWaiting() == 0:
                pass
            dataRecvd = recvFromArduino()
            print "Reply Received: " + dataRecvd
            
        n += 1
        waitingForReply = False
    end = time.time()
    between = end - start
    print "Timing: " + str(between)
    print "==========="
    time.sleep(0.05)
    ser.close()


def findDevice(devName,baudRate=19200,numDev=0):
    waitingForReply = False

    for serPort in serialPorts():
        global ser
        ser = serial.Serial(serPort, baudRate)
        waitForArduino()
      
        request = '<getName,' + devName + ','+ str(numDev) +'>'        
        
        if waitingForReply == False:
            sendToArduino(request)
            waitingForReply = True
            
        if waitingForReply == True:
            while ser.inWaiting() == 0:
                pass

            dataRecvd = recvFromArduino()
            if(dataRecvd == devName):
                ser.close()
                return serPort
                
            waitingForReply = False
        ser.close()
    print "========================="
    print "deivice has not been found"
    print "========================="
    return False


#======================================

# THE DEMO PROGRAM STARTS HERE

#======================================

#serPort = findDevice('stimulator')
#if(serPort):
#    data = []
#    data.append("<fire,200,5>")
#    sendMessage(serPort,data)
    
    

