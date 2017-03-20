import serial
ser = serial.Serial('/dev/ttyACM0', 115200)


while True:
    data = ser.read()
    for byte in data:
        print(ser.read(1))
