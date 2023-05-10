import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10,10,0.1)
y=2*x**2+3*x-4
plt.plot(x,y,color='red',linewidth=2)

#vẽ trục Ox
y=np.zeros(x.shape)         
plt.plot(x,y,color='blue',linewidth=1)
#vẽ trục Oy
y=np.arange(-10,250,1)
x=np.zeros(y.shape)
plt.plot(x,y,color='green',linewidth=3)


plt.xlabel('x')
plt.ylabel('y')
plt.title('Đồ thị hàm số')
plt.plot(x,y,color='black',linewidth=1)
plt.show()