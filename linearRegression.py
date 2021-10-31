import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
xArray=[]
yArray=[]

def my_linfit(xNPArr , yNPArr, totalPoints ) :
    a=((totalPoints*(sum(xNPArr*yNPArr)))-(sum(xNPArr)*sum(yNPArr)))/((totalPoints*(sum(pow(xNPArr,2))))-(pow(sum(xNPArr),2)))
    b=(sum(yNPArr)-(sum(xNPArr)*a))/totalPoints
    return a , b

def onclick(event):
   
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, event.xdata, event.ydata))
    plt.plot(event.xdata, event.ydata, ',')
    if event.button == 1:
        xArray.insert(0,event.xdata)
        yArray.insert(0,event.ydata)
        fig.canvas.draw()
    else:
        xNPArr=np.around((np.array(xArray)), decimals=2)
        yNPArr=np.around((np.array(yArray)), decimals=2)
        print(xNPArr)
        print(yNPArr)
        totalPoints=len(xNPArr)
        print(totalPoints)
        a,b = my_linfit(xNPArr , yNPArr, totalPoints ) 
        plt.plot(xNPArr , yNPArr , 'kx' )
        
        xp = np.arange((min(xNPArr)-1),(max(xNPArr)+1) ,0.2)
        ax.plot(xp,((a*xp)+b),'y')
        fig.canvas.draw()
        print(f"My_fit :_a={b}_and_b={b}")
        
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()

