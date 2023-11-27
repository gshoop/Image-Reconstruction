import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from cycler import cycler
mpl.rcParams['axes.prop_cycle'] = cycler(color='brk')

name = "sc442Ps_dcs_"

XDIVI = 80
YDIVI = 80
ZDIVI = 80

CONES = 10000

x_start, x_end = -20,20
y_start, y_end = -20,20
z_start, z_end = -20,20

TotalIt = 20
SAVEEVERY = 1

plotlist = [ 1 ]
plotlist += range( SAVEEVERY , TotalIt + SAVEEVERY , SAVEEVERY )

svname = name + "_C" + str(CONES) + "_x" + str(XDIVI) + "y" + str(YDIVI) + "z" + str(ZDIVI)

xspace = np.linspace( x_start , x_end , XDIVI )
yspace = np.linspace( y_start , y_end , YDIVI )
fig , axs = plt.subplots(4,5)
fig.suptitle('44-Sc Point Source %d Compton Cones\n Normalized Activity Profile' %(CONES) )
images = []
l = 0
m = 0
for It in plotlist:

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

    DF = pd.DataFrame(fx)
    DF.to_csv(file_name + '.csv')
    

    if m < 5 and l < 4:
        print(l)
        print(m)
        print("space")
        images.append(axs[l,m].step( xspace , fx/max(fx) , where = 'mid' ))
        axs[l,m].set_title( str(It) + " Iteration(s)" )
        m += 1
    else:
        m = 0
        l += 1
        if l == 4:
            break
        print(l)
        print(m)
        print("space")
        images.append(axs[l,m].step( xspace , fx/max(fx) , where = 'mid' ))
        axs[l,m].set_title( str(It) + " Iteration(s)" )
        m += 1

    
    #plt.tight_layout()

plt.show()
fig.savefig('../Images/Prof_' + file_name + '.png')
plt.close(fig)
