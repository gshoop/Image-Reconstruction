import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from cycler import cycler
from scipy.optimize import curve_fit
from scipy.interpolate import UnivariateSpline



def fit_gaussian(x_data, y_data):
    initial_guess = [max(y_data), -0.5, 4]
    popt, _ = curve_fit(gaussian, x_data, y_data, p0=initial_guess)
    return popt

def gaussian(x, amp, mean, stddev):
    return amp * np.exp(-(((x - mean) / (2 * stddev))**2))


mpl.rcParams['axes.prop_cycle'] = cycler(color='brk')

name = "sc44Ps_RS2023_dcs_"

XDIVI = 40
YDIVI = 40
ZDIVI = 40

CONES = 1000

x_start, x_end = -20,20
y_start, y_end = -20,20
z_start, z_end = -20,20

TotalIt = 20
SAVEEVERY = 1

plotlist = [ 1 ]
plotlist += range( SAVEEVERY , TotalIt + SAVEEVERY , SAVEEVERY )
plotlist = plotlist[1:TotalIt+1]
print(plotlist)

svname = name + "_C" + str(CONES) + "_x" + str(XDIVI) + "y" + str(YDIVI) + "z" + str(ZDIVI)

fwhm_arr = np.zeros(TotalIt)
print(fwhm_arr)
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
    print("Iteration: " + file_name)

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

    # Get FWHM
    fit_params = fit_gaussian(xspace,fx/max(fx))

    xg = np.linspace(x_start,x_end,1000)
    yg = gaussian(xg, *fit_params)
    spline = UnivariateSpline(xg, yg - np.max(yg)/2, s=0)
    r1, r2 = spline.roots()
    fwhm = r2-r1
    fwhm_arr[It-1] = fwhm

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
print(fwhm_arr)
plt.show()
fig.savefig('../Images/Prof_' + file_name + '.png')
plt.close(fig)

plt.figure(2)
plt.plot(np.arange(1,21),fwhm_arr)
plt.show()