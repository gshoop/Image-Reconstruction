import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from cycler import cycler
mpl.rcParams['axes.prop_cycle'] = cycler(color='brk')

name = "sc442Ps_dcs_"

XDIVI = 40
YDIVI = 40
ZDIVI = 40

CONES = 10000

x_start, x_end = -20,20
y_start, y_end = -20,20
z_start, z_end = -20,20

TotalIt = 20
SAVEEVERY = 1

plotlist = [ 1 ]
plotlist += range( SAVEEVERY , TotalIt + SAVEEVERY , SAVEEVERY )

svname = name + "_C" + str(CONES) + "_x" + str(XDIVI) + "y" + str(YDIVI) + "z" + str(ZDIVI)

fig = plt.figure( figsize = (9,9) )

axx = fig.add_subplot( 2 , 2 , 1 )
axx.set_xlabel('x direction (mm)')
axx.set_ylabel(' % of maximum')
xspace = np.linspace( x_start , x_end , XDIVI )

axy = fig.add_subplot( 2 , 2 , 2 )
axy.set_xlabel('y direction (mm)')
axy.set_ylabel(' % of maximum')
yspace = np.linspace( y_start , y_end , YDIVI )
axy.yaxis.set_label_position("right")

axz = fig.add_subplot( 2 , 2 , 3 )
axz.set_xlabel('z direction (mm)')
axz.set_ylabel(' % of maximum')
zspace = np.linspace( z_start , z_end , ZDIVI )

ax = fig.add_subplot( 2 , 2 , 4 )
ax.set_xlabel('x direction (mm)')
ax.set_ylabel('z direction (mm)')
ax.yaxis.set_label_position("right")

for It in plotlist:

    file_name = svname + "_I" + str(It)
    csv_name = file_name

    F=open ('../Output/' + file_name + '.csv', 'r')

    fx = np.zeros(XDIVI)
    fy = np.zeros(YDIVI)
    fz = np.zeros(ZDIVI)

    fxz = [[ 0 for i in range(XDIVI) ]  for k in range(ZDIVI)]
    fxy = [[ 0 for i in range(XDIVI) ]  for k in range(YDIVI)]

    for line in F:
        line=line.strip()
        columns=line.split(",")
        i = int(columns[4])
        j = int(columns[5])
        k = int(columns[6])

        fxz[k][i] += float(columns[0])
        fxy[j][i] += float(columns[0])
        fx[i] += float(columns[0])
        fy[j] += float(columns[0])
        fz[k] += float(columns[0])

    heatmap = ax.imshow(fxy, cmap = 'jet', origin = 'lower', extent = [x_start,x_end,y_start,y_end])

    axx.step( xspace , fx/max(fx) , where = 'mid' )
    axy.step( yspace , fy/max(fy) , where = 'mid' )
    axz.step( zspace , fz/max(fz) , where = 'mid' )

    ax.set_title( str(It) + " Iteration(s)" )
    plt.tight_layout()
fig.colorbar(heatmap)
plt.show()
fig.savefig('../Images/Profile_' + file_name + '.png')
plt.close(fig)
