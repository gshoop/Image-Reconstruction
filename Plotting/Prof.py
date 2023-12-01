import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from cycler import cycler
from scipy.optimize import curve_fit
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import splrep, PPoly



def fit_gaussian(x_data, y_data):
    mean = sum(x_data*y_data)/sum(y_data)
    sigma = sum(y_data*(x_data-mean)**2)/sum(y_data)
    initial_guess = [max(y_data), mean, sigma]
    popt, pcov = curve_fit(gaussian, x_data, y_data, p0=initial_guess)
    return popt, pcov

def gaussian(x, amp, mean, stddev):
    return amp * np.exp(-(((x - mean) / (2 * stddev))**2))


mpl.rcParams['axes.prop_cycle'] = cycler(color='brk')

name = "as72Ps_RS2023_dcs_"

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
fwhm_arr_y = np.zeros(TotalIt)
fwhm_arr_z = np.zeros(TotalIt)

xspace = np.linspace( x_start , x_end , XDIVI )
yspace = np.linspace( y_start , y_end , YDIVI )
zspace = np.linspace( z_start , z_end , ZDIVI )

fig , axs = plt.subplots(4,5)
fig.suptitle('As-72 Point Source %d Compton Cones\n Normalized Activity Profile' %(CONES) )
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
    fit_params, pcov = fit_gaussian(xspace,fx/max(fx))

    xg = np.linspace(x_start,x_end,1000)
    yg = gaussian(xg, *fit_params)
    
    spline = UnivariateSpline(xg, yg - np.max(yg)/2, s=0)

    if len(spline.roots()) < 2:
        fwhm = 2*np.sqrt(2*np.log(2))*fit_params[2]
    else:
        r1, r2 = spline.roots()
        fwhm = r2-r1
    fwhm_arr[It-1] = np.abs(fwhm)

    # y-profile --------------------------------------------------------------
    DF = pd.DataFrame(fy)
    DF.to_csv(file_name + '_ydir' + '.csv')
    # Get FWHM
    fit_params, pcov = fit_gaussian(yspace,fy/max(fy))

    xg = np.linspace(y_start,y_end,1000)
    yg = gaussian(xg, *fit_params)
    
    spline = UnivariateSpline(xg, yg - np.max(yg)/2, s=0)

    if len(spline.roots()) < 2:
        fwhm = 2*np.sqrt(2*np.log(2))*fit_params[2]
        print("FWHM - y - :" + str(fwhm))
    else:
        r1, r2 = spline.roots()
        fwhm = np.abs(r2-r1)
    fwhm_arr_y[It-1] = np.abs(fwhm)
    # z-profile --------------------------------------------------------------
    DF = pd.DataFrame(fz)
    DF.to_csv(file_name + '_zdir' + '.csv')
    # Get FWHM
    fit_params, pcov = fit_gaussian(zspace,fz/max(fz))

    xg = np.linspace(z_start,z_end,1000)
    yg = gaussian(xg, *fit_params)
    
    spline = UnivariateSpline(xg, yg - np.max(yg)/2, s=0)

    if len(spline.roots()) < 2:
        fwhm = 2*np.sqrt(2*np.log(2))*fit_params[2]
    else:
        r1, r2 = spline.roots()
        fwhm = r2-r1
    fwhm_arr_z[It-1] = np.abs(fwhm)

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
fig.savefig('../Images/Prof_' + file_name + '.png')
plt.close(fig)

DF = pd.DataFrame(fwhm_arr)
DF.to_csv('FWHM' + file_name + '.csv')
DFy = pd.DataFrame(fwhm_arr_y)
DFy.to_csv('FWHM' + file_name + 'ydir' + '.csv')
DFz = pd.DataFrame(fwhm_arr_z)
DFz.to_csv('FWHM' + file_name + 'zdir' + '.csv')


popt_g, pcov_g = fit_gaussian(xspace,fx/max(fx))
perr_g = np.sqrt(np.diag(pcov_g))
print("x-dir ----------------------------------------------")
print("amp = {:0.3f} (+/-) {:0.3f}".format(popt_g[0],perr_g[0]))
print("mean = {:0.3f} (+/-) {:0.3f}".format(popt_g[1],perr_g[1]))
print("stddev = {:0.3f} (+/-) {:0.3f}".format(popt_g[2],perr_g[2]))

xg = np.linspace(x_start,x_end,1000)
yg = gaussian(xg, *popt_g)

fig1, ax1 = plt.subplots()
fig1.suptitle('As-72 Point Source %d Compton Cones\n Normalized Activity Profile' %(CONES))
ax1.set_xlabel('x (mm)')
ax1.set_ylabel('Probability density')
ax1.fill_between(xspace,fx/max(fx), step="pre", alpha=0.4)
ax1.step(xspace,fx/max(fx),linewidth=1,label='Profile')
ax1.plot(xg,yg,'r',linewidth=1.5,label='Gaussian fit')
ax1.text(-18,0.7,'FWHM = {:5.3f}'.format(fwhm_arr[It-1]),bbox={'facecolor': 'blue', 'alpha':0.2})
ax1.text(5,0.7,'$a$ = {:0.3f} (+/-) {:0.3f}\n$\mu$ = {:0.3f} (+/-) {:0.3f}\n$\sigma^2$ = {:0.3f} (+/-) {:0.3f}'.format(popt_g[0],perr_g[0],popt_g[1],perr_g[1],popt_g[2]**2,perr_g[2]), bbox={'facecolor': 'blue', 'alpha':0.2})
ax1.grid(True)
ax1.legend()
plt.show()
fig1.savefig('../Images/gauss_' + file_name + 'xdir.png',dpi=300)
fig1.savefig('../Images/gauss_' + file_name + 'xdir.eps',dpi=300)
plt.close(fig1)

# ydir
popt_g, pcov_g = fit_gaussian(yspace,fy/max(fy))
perr_g = np.sqrt(np.diag(pcov_g))
print("y-dir ----------------------------------------------")
print("amp = {:0.3f} (+/-) {:0.3f}".format(popt_g[0],perr_g[0]))
print("mean = {:0.3f} (+/-) {:0.3f}".format(popt_g[1],perr_g[1]))
print("stddev = {:0.3f} (+/-) {:0.3f}".format(popt_g[2],perr_g[2]))

xg = np.linspace(y_start,y_end,1000)
yg = gaussian(xg, *popt_g)

fig1, ax1 = plt.subplots()
fig1.suptitle('As-72 Point Source %d Compton Cones\n Normalized Activity Profile' %(CONES))
ax1.set_xlabel('y (mm)')
ax1.set_ylabel('Probability density')
ax1.fill_between(yspace,fy/max(fy), step="pre", alpha=0.4)
ax1.step(yspace,fy/max(fy),linewidth=1,label='Profile')
ax1.plot(xg,yg,'r',linewidth=1.5,label='Gaussian fit')
ax1.text(-18,0.7,'FWHM = {:5.3f}'.format(fwhm_arr_y[It-1]),bbox={'facecolor': 'blue', 'alpha':0.2})
ax1.text(5,0.7,'$a$ = {:0.3f} (+/-) {:0.3f}\n$\mu$ = {:0.3f} (+/-) {:0.3f}\n$\sigma^2$ = {:0.3f} (+/-) {:0.3f}'.format(popt_g[0],perr_g[0],popt_g[1],perr_g[1],popt_g[2]**2,perr_g[2]), bbox={'facecolor': 'blue', 'alpha':0.2})
ax1.grid(True)
ax1.legend()
plt.show()
fig1.savefig('../Images/gauss_' + file_name + 'ydir.png',dpi=300)
fig1.savefig('../Images/gauss_' + file_name + 'ydir.eps',dpi=300)
plt.close(fig1)

# zdir
popt_g, pcov_g = fit_gaussian(zspace,fz/max(fz))
perr_g = np.sqrt(np.diag(pcov_g))
print("x-dir ----------------------------------------------")
print("amp = {:0.3f} (+/-) {:0.3f}".format(popt_g[0],perr_g[0]))
print("mean = {:0.3f} (+/-) {:0.3f}".format(popt_g[1],perr_g[1]))
print("stddev = {:0.3f} (+/-) {:0.3f}".format(popt_g[2],perr_g[2]))

xg = np.linspace(z_start,z_end,1000)
yg = gaussian(xg, *popt_g)

fig1, ax1 = plt.subplots()
fig1.suptitle('As-72 Point Source %d Compton Cones\n Normalized Activity Profile' %(CONES))
ax1.set_xlabel('z (mm)')
ax1.set_ylabel('Probability density')
ax1.fill_between(zspace,fz/max(fz), step="pre", alpha=0.4)
ax1.step(zspace,fz/max(fz),linewidth=1,label='Profile')
ax1.plot(xg,yg,'r',linewidth=1.5,label='Gaussian fit')
ax1.text(-18,0.7,'FWHM = {:5.3f}'.format(fwhm_arr_z[It-1]),bbox={'facecolor': 'blue', 'alpha':0.2})
ax1.text(5,0.7,'$a$ = {:0.3f} (+/-) {:0.3f}\n$\mu$ = {:0.3f} (+/-) {:0.3f}\n$\sigma^2$ = {:0.3f} (+/-) {:0.3f}'.format(popt_g[0],perr_g[0],popt_g[1],perr_g[1],popt_g[2]**2,perr_g[2]), bbox={'facecolor': 'blue', 'alpha':0.2})
ax1.grid(True)
ax1.legend()
plt.show()
fig1.savefig('../Images/gauss_' + file_name + 'zdir.png',dpi=300)
fig1.savefig('../Images/gauss_' + file_name + 'zdir.eps',dpi=300)
plt.close(fig1)


#fig2, ax2 = plt.subplots()
#ax2.plot(np.arange(1,21),fwhm_arr,'og')
#ax2.set_title('FWHM 44Sc Point Source x-direction')
#ax2.set_xlabel('Iteration #')
#ax2.set_ylabel('FWHM (mm)')
#ax2.grid(True)
#plt.show()
#
#fig3, ax3 = plt.subplots()
#ax3.plot(np.arange(1,21),fwhm_arr_y,'oc')
#ax3.set_title('FWHM 44Sc Point Source y-direction')
#ax3.set_xlabel('Iteration #')
#ax3.set_ylabel('FWHM (mm)')
#ax3.grid(True)
#plt.show()
#
#fig4, ax4 = plt.subplots()
#ax4.plot(np.arange(1,21),fwhm_arr_z,'om')
#ax4.set_title('FWHM 44Sc Point Source z-direction')
#ax4.set_xlabel('Iteration #')
#ax4.set_ylabel('FWHM (mm)')
#ax4.grid(True)
#plt.show()