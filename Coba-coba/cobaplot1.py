import serial
import matplotlib.pyplot as plt
import math

line=0
samples = 105
arduino_port = "/dev/ttyACM0" #serial port pada Arduino
baud = 115200 #atur baudrate
ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:" + arduino_port)

sensor_data = [] #store data

#menampilkan data ke terminal
getData=ser.readline()
dataString = getData.decode('utf-8')
data=dataString[0:][:-2]
print(data)

readings = data.split(",")
print(readings)

sensor_data.append(readings)
print(sensor_data)

# mengambil sampel
while line <= samples:
    getData=ser.readline()
    dataString = getData.decode('utf-8')
    data=dataString[0:][:-2]
    print(data)

    readings = data.split(",")
    print(readings)

    sensor_data.append(readings)
    print(sensor_data)

    line = line+1

dat1=[0] 
dat1.append(float(readings[0]))  
dat2=[0] 
dat2.append(float(readings[1]))

xs = [i / 5.0 for i in range(0, 100)]
xnf = [dat1]
xf = [dat2]

plt.plot(xs, xnf, 'r^', label='xnf')
plt.plot(xs, xf, 'b--', label='xf')

# Adjust the axes' limits: [xmin, xmax, ymin, ymax]
plt.axis([0, 200, 0, 360])

# Give the graph a title and axis labels
plt.title('My Sinewaves')
plt.xlabel('Radians')
plt.ylabel('Value')

# Show a legend
plt.legend()

# Save the image
plt.savefig('sinewaves.png')

# Draw to the screen
plt.show()