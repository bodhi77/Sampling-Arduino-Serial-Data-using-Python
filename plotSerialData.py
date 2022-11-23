import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

headers = ['xnf', 'xf']

df = pd.read_csv('alpha0.001.csv')
df2 = df.tail(df.shape[0] -7)
print(df2)

xnf = df2['xnf']
xf = df2['xf']
val = []

for i in range(7,107):
    val.append(i)

plt.plot(val, xnf, label= "xnf")
plt.plot(val, xf, label= "xf")
plt.plot(val,90)

plt.legend(['xnf','xf'], prop={'size': 10})

plt.show()