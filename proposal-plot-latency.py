import re
import numpy as np
import matplotlib.pyplot as plt

with open("/Volumes/Untitled/benchmarks/normalpages-2.txt") as f1:
    data1 = f1.read()
x=[]
y=[]

for s in data1.split('\n'):

    for token in s.split():
        try:
            print float(token)
            y1 = re.findall("\d+", s)
            #y2 = re.findall("\d+\.\d+", s)
            t = int(y1[0])
            r = int(y1[1])#float
            x.append(t)
            y.append(r)
            print y1
        except ValueError:
            print ""
x2=[1456443432074853, 1456443517090546, 1456443623105308, 1456443751116818 ]
fig1 = plt.figure()
'''
plt.axvline(x=1456443432074853, ymin=0, ymax = 1, linewidth=1, color='r')
plt.axvline(x=1456443517090546, ymin=0, ymax = 1, linewidth=1, color='r')
plt.axvline(x=1456443623105308, ymin=0, ymax = 1, linewidth=1, color='r')
plt.axvline(x=1456443751116818, ymin=0, ymax = 1, linewidth=1, color='r')
'''
x = [(t/1000000 - 1.4564433e9) for t in x]
#x = [t/1.4564433e9 for t in x]

ax1 = fig1.add_subplot(111)
#ax1.plot(x2,y2, 'ro')
ax1.set_title("Latency time series")
ax1.set_xlabel('Time in s')
ax1.set_ylabel('Latency in ms')
#ax1.set_yscale('log', basex=2)
#ax1.set_xscale('log', basex=2)
axes = plt.gca()
axes.set_ylim([-5,1000])
ax1.plot(x,y)
plt.show()