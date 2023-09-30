import matplotlib
import matplotlib.pyplot as mp
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y1 = 8/np.square(np.pi)*np.sin(x) #第一個正弦波
y2 = -8/(9*np.square(np.pi))*np.sin(3*x) #第二個正弦波
y3 = 8/(25*np.square(np.pi))*np.sin(5*x) #第三個正弦波 
y4 = -8/(49*np.square(np.pi))*np.sin(7*x) #第四個正弦波
y5 = 8/(81*np.square(np.pi))*np.sin(9*x) #第五個正弦波
y = np.zeros(x.size)
y_2 ,y_3, y_4, y_5= np.zeros(x.size), np.zeros(x.size), np.zeros(x.size), np.zeros(x.size)

for i in range(1, 1000):
    y += (8/np.square(np.pi))*(np.power(-1,i+1)/np.square(2*i-1))*np.sin((2*i-1)*x) #疊加一千個正弦波
for i in range(1, 2):
    y_2 += (8/np.square(np.pi))*(np.power(-1,i+1)/np.square(2*i-1))*np.sin((2*i-1)*x) #疊加二個正弦波
for i in range(1, 3):
    y_3 += (8/np.square(np.pi))*(np.power(-1,i+1)/np.square(2*i-1))*np.sin((2*i-1)*x) #疊加三個正弦波
for i in range(1, 4):
    y_4 += (8/np.square(np.pi))*(np.power(-1,i+1)/np.square(2*i-1))*np.sin((2*i-1)*x) #疊加四個正弦波
for i in range(1, 5):
    y_5 += (8/np.square(np.pi))*(np.power(-1,i+1)/np.square(2*i-1))*np.sin((2*i-1)*x) #疊加五個正弦波

mp.grid(linestyle='-.')
mp.plot(x, y, linewidth = 1)
mp.plot(x, y_2, linewidth = 1, linestyle='--')
mp.plot(x, y_3, linewidth = 1, linestyle='--')
mp.plot(x, y_4, linewidth = 1, linestyle='--')
mp.plot(x, y_5, linewidth = 1, linestyle='--')
mp.show()