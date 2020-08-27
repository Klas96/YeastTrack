import numpy as np
import scipy.optimize as op
from matplotlib import pyplot as plt

def func(x,const,rate):
    return(const*np.exp(rate*x))

def fitExponential(array):
    print(len(array))
    fx = np.array(range(len(array)))
    fy = np.array(array)

    popt, pcov = op.curve_fit(func,fx,fy,p0=(fx[0], 0.1),maxfev = 6000)

    plt.plot(fx, fy, 'x', label='data')
    plt.plot(fx, func(fx, *popt), label='curve-fit')
    plt.legend(loc='upper left')

    return(popt)


#Put in epo in size plot
def plotDataWithExpo(array):
    xArr = range(0,31)
    const = 5.3338403*1000
    rate = 2.1211569/100
    yArr = []
    for i in range(len(xArr)):
        yArr.append(func(i,const,rate))
    plt.plot(xArr, yArr,color='C1',label="exponential fit")

    const = 8.493409*1000
    rate = 5.3318/1000
    xArr = range(36,95)
    yArr = []
    for i in range(len(xArr)):
        yArr.append(func(i,const,rate))
    plt.plot(xArr, yArr,color='C2',label="exponential fit")
    plt.plot(range(len(array)), array,'x',color='C0',label= "data")
    plt.ylabel('Growth Curves with exponential fit')
    plt.xlabel('Time')
    plt.title("Size")
    plt.xticks([])
    plt.yticks([])
    plt.legend()
    plt.show()
