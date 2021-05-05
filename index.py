# Importing Libraries
import serial
import time
arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
while True:
    num = input("""1. Distance sensor 1
2. Distance sensor 2
3. Both Distance Sensors
4. Reflectance Sensor
5. All Sensors
6. Calibrate Reflectance Sensor
Enter A Number:
    """) # Taking input from user
    value = write_read(num)
    print(value) # printing the value
