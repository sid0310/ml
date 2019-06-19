#!/usr/bin/python3

import  matplotlib.pyplot    as   plt
x=[2,3]
x1=[4,3,8]
y1=[2,9,7]
y=[9,5]

plt.xlabel("time")
plt.ylabel("speed")
plt.plot(x,y,label="water")   
plt.plot(x1,y1,label="sand")   
plt.bar(x,y)  
plt.bar(x1,y1)  
plt.grid(color='green')   
plt.legend()   
plt.xlim(0,12)  
plt.ylim(0,15)   
plt.show()