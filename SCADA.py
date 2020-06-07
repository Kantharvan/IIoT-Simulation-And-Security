from pymodbus.server.asynchronous import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from twisted.internet.task import LoopingCall
import RPi.GPIO as GPIO

LED=18
BZ=17
SW=27
TRIG=24
ECHO=23
cur=0
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(BZ,GPIO.OUT)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(LED, GPIO.LOW)
GPIO.output(BZ, GPIO.HIGH)

store = ModbusSlaveContext(
    di = ModbusSequentialDataBlock(0, [0]*100),
    co = ModbusSequentialDataBlock(0, [0]*100),
    hr = ModbusSequentialDataBlock(0, [0]*100),
    ir = ModbusSequentialDataBlock(0, [0]*100))
context = ModbusServerContext(slaves=store, single=True)

values = [0,0]
def updating_writer(a):
    context  = a[0]
    register = 3
    slave_id = 0
    address  = 0
    GPIO.output(TRIG, False)
    time.sleep(0.5)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = int(distance)
    print "Distance:",distance,"cm"
    values[0] = distance
    if(distance  < 100):
        values[1]= values[1]+1
    context[slave_id].setValues(register,address,values)
    print("Ultrasonic value",values)

def read_context(a):
     context  = a[0]
     register = 3
     slave_id = 0
     address  = 10
     value = context[slave_id].getValues(register,address,10)
     if value[0]==0:GPIO.output(LED, GPIO.LOW)
     if value[0]==1:GPIO.output(LED, GPIO.HIGH)
     dateTimeObj = datetime.now()

     if(value[0]==0):
         print(" : LED OFF ")
     else:
         print(" : LED ON ")

read = LoopingCall(f=read_context, a=(context,))
read.start(.2)

write = LoopingCall(f=updating_writer, a=(context,))
write.start(.2)

StartTcpServer(context, address=('',510))