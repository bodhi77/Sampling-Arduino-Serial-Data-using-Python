import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [14, 7]
plt.rcParams["figure.autolayout"] = True

n = 50
vxz = 90
vy = 0
spxz = [vxz]*n
spy = [vy]*n


for i in range(n):
    spxz.append(vxz)
    spy.append(vy)

headers = ['xnf', 'xf', 'ynf', 'yf', 'znf', 'zf']

df = pd.read_csv('alpha0.001.csv')
df2 = df.tail(df.shape[0] -7)
print(df2)

xnf = df2['xnf']
xf = df2['xf']
ynf = df2['ynf']
yf = df2['yf']
znf = df2['znf']
zf = df2['zf']
val = []

for i in range(7,107):
    val.append(i)

plt.plot(val, xnf, label= "xnf")
plt.plot(val, xf, label= "xf")
plt.plot(val, spxz, label= "spx")

plt.plot(val, ynf, label= "ynf")
plt.plot(val, yf, label= "yf")
plt.plot(val, spy, label= "spy")

plt.plot(val, znf, label= "znf")
plt.plot(val, zf, label= "zf")
plt.plot(val, spxz, label= "spz")

plt.legend(['xnf','xf','spx','ynf','yf','znf','zf'], prop={'size': 10})

plt.show()