import serial
ser = serial.Serial('/dev/ttyACM0', 115200)


while True:
    print(ser.read(1))
