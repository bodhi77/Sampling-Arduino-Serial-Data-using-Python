import serial
import matplotlib.pyplot as plt
import numpy as np

connected = False

comPort = '/dev/ttyACM0'        

ser = serial.Serial(comPort, 115200)    # Sets up serial connection (make sure baud rate is correct - matches Arduino)

while not connected:
    serin = ser.read()
    connected = True

plt.ion()                               # Sets plot to animation mode

fig1 = plt.figure()
fig2 = plt.figure()
fig3 = plt.figure()
fig4 = plt.figure()

ax1 = fig1.add_subplot(111)
ax2 = fig2.add_subplot(111)
ax3 = fig3.add_subplot(111)
ax4 = fig4.add_subplot(111)

length = 20                             # Determines length of data taking session (in data points); length/10 = seconds

w = [0]*length                          # Create empty variable of length of test
x = [0]*length               
y = [0]*length
z = [0]*length

wline, = ax1.plot(w)                    # Sets up future lines to be modified
xline, = ax2.plot(x)                    
yline, = ax3.plot(y)
zline, = ax4.plot(z)

ax1.set_ylim(0,64535)                       # Sets the y axis limits - 16 bits resolution
ax2.set_ylim(0,64535)
ax3.set_ylim(0,64535)
ax4.set_ylim(0,64535)

for i in range(length):                 # While you are taking data
    data = ser.readline()               # Reads until it gets a carriage return (/n).
    sep = data.split(",")                  # Splits string into a list at the tabs

    w.append(int(sep[0]))               # Add new values as int to current list
    x.append(int(sep[1]))   
    y.append(int(sep[2]))
    z.append(int(sep[3]))

    del w[0]
    del x[0]
    del y[0]
    del z[0]

    wline.set_xdata(np.arange(len(w)))  # Sets wdata to new list length  
    xline.set_xdata(np.arange(len(x)))  
    yline.set_xdata(np.arange(len(y)))  
    zline.set_xdata(np.arange(len(z)))  

    wline.set_ydata(w)                  # Sets ydata to new lists 
    xline.set_ydata(x)                 
    yline.set_ydata(y)
    zline.set_ydata(z)

    print(i)
    print(sep)

    
#    ax1.plot(sep[0])
    ax1.pause(0.001)
    ax1.grid(True)                   
    fig1.canvas.draw()# Draws new plot
    fig1.canvas.savefig('a.png')

    
    ax2.pause(0.001)                   
    ax2.grid(True)
    fig2.canvas.draw()                    # Draws new plot

   
    ax3.pause(0.001)                   
    ax3.grid(True)
    fig3.canvas.draw()                        # Draws new plot

    
    ax4.pause(0.001)                   
    ax4.grid(True)
    fig4.canvas.draw()                      # Draws new plot

plt.savefig('a.png')
plt.show()

ser.close()     