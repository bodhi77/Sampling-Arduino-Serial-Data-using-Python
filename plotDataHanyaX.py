import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [14, 7]
plt.rcParams["figure.autolayout"] = True

n = 50
v = 90
sp = [v]*n

for i in range(n):
    sp.append(v)

headers = ['xnf', 'xf']

df = pd.read_csv('alpha0.001.csv')
df2 = df.tail(df.shape[0] -7)

df3 = pd.read_csv('alpha0.03.csv')
df4 = df3.tail(df.shape[0] -7)

df5 = pd.read_csv('alpha0.05.csv')
df6 = df5.tail(df.shape[0] -7)

df7 = pd.read_csv('alpha0.6.csv')
df8 = df7.tail(df.shape[0] -7)

df9 = pd.read_csv('alpha0.9.csv')
df10 = df9.tail(df.shape[0] -7)

xnf1 = df2['xnf']
xf1 = df2['xf']

xnf2 = df4['xnf']
xf2 = df4['xf']

xnf3 = df6['xnf']
xf3 = df6['xf']

xnf4 = df8['xnf']
xf4 = df8['xf']

xnf5 = df10['xnf']
xf5 = df10['xf']

val = []

for i in range(7,107):
    val.append(i)

plt.plot(val, sp, label= "sp")
plt.plot(val, xnf1, label= "xnf1 (a=0.001)")
plt.plot(val, xf1, label= "xf1 (a=0.001)")

plt.plot(val, xnf2, label= "xnf2 (a=0.03)")
plt.plot(val, xf2, label= "xf2 (a=0.03)")

plt.plot(val, xnf3, label= "xnf3 (a=0.05)")
plt.plot(val, xf3, label= "xf3 (a=0.05)")

plt.plot(val, xnf4, label= "xnf4 (a=0.6)")
plt.plot(val, xf4, label= "xf4 (a=0.6)")

plt.plot(val, xnf5, label= "xnf4 (a=0.9)")
plt.plot(val, xf5, label= "xf4 (a=0.9)")

plt.legend(['sp','xnf1 (a=0.001)','xf1 (a=0.001)','xnf2 (a=0.03)','xf2 (a=0.03)','xnf3 (a=0.05)','xf3 (a=0.05)','xnf4 (a=0.6)','xf4 (a=0.6)','xnf5 (a=0.9)','xf5 (a=0.9)'], prop={'size': 10})

plt.show()