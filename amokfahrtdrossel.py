import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

IS_Speed = np.linspace(0., 70.0, 71*2)


duration = np.arange(1, 11, 1) # np.array([1., 2., 3., 4., 5., 6., 7., 8., 9., 10.0])
accelerationrequest = np.arange(30, 100, 10) # np.array([30., 40., 50., 60., 70., 80., 90.])

                # 1sec 2sec 3sec 4sec 5sec 6sec 7sec 8sec 9sec 10sec lange Beschleunigung (kann auch in Stücken akkumuliert sein)
d = np.array([  [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],    # <30% Kickdown (Parken und normale Fahrt)
                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.6],    #  40% Kickdown (schneller Beschleunigen / Eile)
                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.6, 1.0, 1.0],    #  50% Kickdown
                [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.6, 1.0, 1.0, 1.0],    #  60% Kickdown
                [ 0.0, 0.0, 0.0, 0.0, 0.3, 0.6, 1.0, 1.0, 1.0, 1.0],    #  70% Kickdown
                [ 0.0, 0.0, 0.0, 0.3, 0.6, 1.0, 1.0, 1.0, 1.0, 1.0],    #  80% Kickdown
                [ 0.0, 0.0, 0.3, 0.6, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0] ] ) # >90% Kickdown


# 3d yüzey için örnek veri hazırlama
# x = np.arange(-5, 5, 0.25)
# y = np.arange(-5, 5, 0.25)
# x, y = np.meshgrid(x, y)
# r = np.sqrt(x**2, y**2)

duration, accelerationrequest = np.meshgrid(duration, accelerationrequest)
ax = plt.subplot(111, projection='3d')
ax.plot_surface(duration, accelerationrequest, d, linewidth=0.1)

plt.xlabel('Kickdown Duration (sec)')
plt.ylabel('Pedal Position (%)')
#plt.zlabel('Drosselstaerke (%)')
plt.title('An example seed function for ADI Experiments')

plt.show()

# accumulation von dauer x beschleunigung in der letzten 10 sekunden
# beim bremsen reset von accumulator

# for speedindex in np.linspace(0,70,71):
#     for accelerationindex in np.linspace(0, 3, 71):
#         A[] = speedindex
