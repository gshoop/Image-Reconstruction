import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
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


for It in plotlist:

    fig, ax = plt.subplots()
    fig.suptitle('44-Sc Point Source %d Compton Cones' %(CONES) )
    images = []

    ax.set_xlabel('x direction (mm)')
    ax.set_ylabel('y direction (mm)')
    ax.yaxis.set_label_position("right")
    
    file_name = svname + "_I" + str(It)

    F=open ('../Output/' + file_name + '.csv', 'r')

    fx = np.zeros(XDIVI)
    fy = np.zeros(YDIVI)
    fz = np.zeros(ZDIVI)

    fxz = [[ 0 for i in range(XDIVI) ]  for k in range(ZDIVI)]
    fxy = [[ 0 for i in range(XDIVI) ]  for k in range(YDIVI)]
    fyz = [[ 0 for i in range(YDIVI) ]  for k in range(ZDIVI)]

    for line in F:
        line=line.strip()
        columns=line.split(",")
        i = int(columns[4])
        j = int(columns[5])
        k = int(columns[6])

        fxz[k][i] += float(columns[0])
        fxy[j][i] += float(columns[0])
        fyz[k][j] += float(columns[0])
        fx[i] += float(columns[0])
        fy[j] += float(columns[0])
        fz[k] += float(columns[0])

    heatmap = ax.imshow(fxy, cmap = 'jet', origin = 'lower', extent = [x_start,x_end,y_start,y_end])


    ax.set_title( str(It) + " Iteration(s)" )
    #plt.tight_layout()
    cbar = fig.colorbar(heatmap)

    
    fig.savefig('../Images/Distribution_' + file_name + '.png')
    plt.close(fig)
