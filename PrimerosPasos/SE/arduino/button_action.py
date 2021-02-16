import serial
import os

ser = serial.Serial("/dev/ttyACM0",9600)

while True:
    data = ser.readline().decode().replace("\n","")

    if data:
        data = data[0:-1]
        print(f"I execute {data}")
        #os.popen(data)
        os.popen("konsole");
        #os.popen('mkdir ~/Desktop/edgarin')
        print("Finished")
      

#os.popen("konsole")
