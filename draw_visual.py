import matplotlib.pyplot as plt
from  randomwalk import RandomWalk
while True:
    rw=RandomWalk(50000)
    rw.fill_work()
    plt.figure(dpi=128,figsize=(10,6))          #调整屏幕尺寸
    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
    plt.axes().get_xaxis().set_visible(False)   #设置x轴不可见
    plt.axes().get_yaxis().set_visible(False)   #设置y轴不可见
    plt.show()
    keep_running=input("continue(y/n)?")
    if keep_running=="n":
        break
