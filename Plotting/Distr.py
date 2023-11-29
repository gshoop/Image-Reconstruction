import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
mpl.rcParams['axes.prop_cycle'] = cycler(color='brk')

name = "sc44Ps_RS2023_dcs_"

XDIVI = 80
YDIVI = 80
ZDIVI = 80

CONES = 1000

x_start, x_end = -20,20
y_start, y_end = -20,20
z_start, z_end = -20,20

TotalIt = 20
SAVEEVERY = 1

plotlist = [ 1 ]
plotlist += range( SAVEEVERY , TotalIt + SAVEEVERY , SAVEEVERY )
plotlist = plotlist[1:TotalIt+1]
svname = name + "_C" + str(CONES) + "_x" + str(XDIVI) + "y" + str(YDIVI) + "z" + str(ZDIVI)

fig , axs = plt.subplots(4,5)
fig.suptitle('44-Sc Point Source %d Compton Cones' %(CONES) )
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


    

    if m < 5 and l < 4:
        print(l)
        print(m)
        print("space")
        images.append(axs[l,m].imshow(fxz, cmap = 'jet', origin = 'lower', extent = [x_start,x_end,z_start,z_end]))
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
        images.append(axs[l,m].imshow(fxz, cmap = 'jet', origin = 'lower', extent = [x_start,x_end,z_start,z_end]))
        axs[l,m].set_title( str(It) + " Iteration(s)" )
        m += 1

    vmin = min(image.get_array().min() for image in images)
    vmax = max(image.get_array().max() for image in images)
    norm = plt.Normalize(vmin=vmin, vmax=vmax)

    for im in images:
        im.set_norm(norm)
    print(vmax)

    
    #plt.tight_layout()

cb_ax = fig.add_axes([0.02,0.05,0.01,0.9])
cbar = fig.colorbar(images[1], cax=cb_ax,)

plt.show()
fig.savefig('../Images/Distr_' + file_name + '.png')
plt.close(fig)
