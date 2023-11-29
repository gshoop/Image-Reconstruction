import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from cycler import cycler
from scipy.optimize import curve_fit
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import splrep, PPoly



def fit_gaussian(x_data, y_data):
    initial_guess = [max(y_data), 0, 3]
    popt, _ = curve_fit(gaussian, x_data, y_data, p0=initial_guess)
    return popt

def gaussian(x, amp, mean, stddev):
    return amp * np.exp(-(((x - mean) / (2 * stddev))**2))


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
print(plotlist)

svname = name + "_C" + str(CONES) + "_x" + str(XDIVI) + "y" + str(YDIVI) + "z" + str(ZDIVI)

fwhm_arr = np.zeros(TotalIt)
fwhm_arr_y = np.zeros(TotalIt)
fwhm_arr_z = np.zeros(TotalIt)

xspace = np.linspace( x_start , x_end , XDIVI )
yspace = np.linspace( y_start , y_end , YDIVI )
zspace = np.linspace( z_start , z_end , ZDIVI )

fig , axs = plt.subplots(4,5)
fig.suptitle('Sc-44 Point Source %d Compton Cones\n Normalized Activity Profile' %(CONES) )
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

    # x-profile --------------------------------------------------------------
    DF = pd.DataFrame(fx)
    DF.to_csv(file_name + '.csv')
    # Get FWHM
    fit_params = fit_gaussian(xspace,fx/max(fx))

    xg = np.linspace(x_start,x_end,1000)
    yg = gaussian(xg, *fit_params)
    
    spline = UnivariateSpline(xg, yg - np.max(yg)/2, s=0)

    if len(spline.roots()) < 2:
        fwhm = 2*np.sqrt(2*np.log(2))*fit_params[2]
    else:
        r1, r2 = spline.roots()
        fwhm = r2-r1
    fwhm_arr[It-1] = fwhm
    # y-profile --------------------------------------------------------------
    DF = pd.DataFrame(fy)
    DF.to_csv(file_name + '_ydir' + '.csv')
    # Get FWHM
    fit_params = fit_gaussian(yspace,fy/max(fy))

    xg = np.linspace(y_start,y_end,1000)
    yg = gaussian(xg, *fit_params)
    
    spline = UnivariateSpline(xg, yg - np.max(yg)/2, s=0)

    if len(spline.roots()) < 2:
        fwhm = 2*np.sqrt(2*np.log(2))*fit_params[2]
    else:
        r1, r2 = spline.roots()
        fwhm = r2-r1
    fwhm_arr_y[It-1] = fwhm
    # z-profile --------------------------------------------------------------
    DF = pd.DataFrame(fz)
    DF.to_csv(file_name + '_zdir' + '.csv')
    # Get FWHM
    fit_params = fit_gaussian(zspace,fz/max(fz))

    xg = np.linspace(z_start,z_end,1000)
    yg = gaussian(xg, *fit_params)
    
    spline = UnivariateSpline(xg, yg - np.max(yg)/2, s=0)

    if len(spline.roots()) < 2:
        fwhm = 2*np.sqrt(2*np.log(2))*fit_params[2]
    else:
        r1, r2 = spline.roots()
        fwhm = r2-r1
    fwhm_arr_z[It-1] = fwhm

    #-------------------------------------------------------------------------
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

DF = pd.DataFrame(fwhm_arr)
DF.to_csv('FWHM' + file_name + '.csv')
DFy = pd.DataFrame(fwhm_arr_y)
DFy.to_csv('FWHM' + file_name + 'ydir' + '.csv')
DFz = pd.DataFrame(fwhm_arr_z)
DFz.to_csv('FWHM' + file_name + 'zdir' + '.csv')


fig2, ax2 = plt.subplots()
ax2.plot(np.arange(1,21),fwhm_arr,'og')
ax2.set_title('FWHM 44Sc Point Source x-direction')
ax2.set_xlabel('Iteration #')
ax2.set_ylabel('FWHM (mm)')
ax2.grid(True)
plt.show()

fig3, ax3 = plt.subplots()
ax3.plot(np.arange(1,21),fwhm_arr_y,'oc')
ax3.set_title('FWHM 44Sc Point Source y-direction')
ax3.set_xlabel('Iteration #')
ax3.set_ylabel('FWHM (mm)')
ax3.grid(True)
plt.show()

fig4, ax4 = plt.subplots()
ax4.plot(np.arange(1,21),fwhm_arr_z,'om')
ax4.set_title('FWHM 44Sc Point Source z-direction')
ax4.set_xlabel('Iteration #')
ax4.set_ylabel('FWHM (mm)')
ax4.grid(True)
plt.show()