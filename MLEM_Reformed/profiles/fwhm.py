import csv
import numpy as np
from scipy.optimize import curve_fit
from pylab import *
import scipy.optimize as opt
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline, splrep, sproot, splev
from matplotlib.font_manager import FontProperties

# Function to fit a double Gaussian curve
def double_gaussian(x, amp1, mean1, stddev1, amp2, mean2, stddev2):
    return (amp1 * np.exp(-((x - mean1) / (2 * stddev1))**2) +
            amp2 * np.exp(-((x - mean2) / (2 * stddev2))**2))

def gaussian(x, amp, mean, stddev):
    return amp * np.exp(-(((x - mean) / (2 * stddev))**2))

# Load data from CSV file
def load_data(file_path):
    x_data = []
    y_data = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header row if it exists
        for row in csv_reader:
            x_data.append(float(row[0]))
            y_data.append(float(row[1]))
    return np.array(x_data), np.array(y_data)

# Fit the double Gaussian curve to the data
def fit_double_gaussian(x_data, y_data):
    initial_guess = [max(y_data)/2, -5.5, 1,
                     max(y_data)/2, 5.5, 1]
    popt, _ = curve_fit(double_gaussian, x_data, y_data, p0=initial_guess)
    return popt

def fit_gaussian(x_data, y_data):
    mean = sum(x_data*y_data)/sum(y_data)
    sigma = sum(y_data*(x_data-mean)**2)/sum(y_data)
    initial_guess = [max(y_data), mean, sigma]
    popt, pcov = curve_fit(gaussian, x_data, y_data, p0=initial_guess)
    return popt, pcov

# Plot the data and fitted curve
def plot_fit(x_data, y_data, fit_params,single_fit):
    plt.step(x_data, y_data/max(y_data), label='Data')
    x_data = np.linspace(-20,20,1000)
    if single_fit == 0:
        plt.plot(x_data, double_gaussian(x_data, *fit_params), 'r', label='Fit')

    else:
        plt.plot(x_data, gaussian(x_data, *fit_params), 'r', label='Fit')

        yg = gaussian(x_data, *fit_params)
        spline = UnivariateSpline(xg, yg - np.max(yg)/2, s=0)
        #r1, r2 = spline.roots()

        print(spline.roots())

        fwhm = 2*np.sqrt(2*np.log(2))*fit_params[2]
        axvspan(fit_params[1] - fwhm/2,fit_params[1] + fwhm/2, facecolor='g', alpha=0.5)
        #axvspan(fit_params[1]-fwhm/2, fit_params[1]+fwhm/2, facecolor='y', alpha=0.5)

    plt.legend()
    plt.show()

# Example usage
file_path = '../as72Ps_RS2023_dcs__C1000_x40y40z40_I1.csv'
sc44_path = '../FWHMsc44Ps_RS2023_dcs__C1000_x40y40z40_I20.csv'
as72_path = '../FWHMas72Ps_RS2023_dcs__C1000_x40y40z40_I20.csv'
ga68_path = '../FWHMga68Ps_RS2023_dcs__C300_x40y40z40_I20.csv'

sc44_80vx_path = '../FWHMsc44Ps_RS2023_dcs__C1000_x80y80z80_I20.csv'

sc44_5k_path = '../FWHMsc44Ps_RS2023_dcs__C5000_x40y40z40_I20.csv'
sc44_10k_path = '../FWHMsc44Ps_RS2023_dcs__C10000_x40y40z40_I20.csv'

sc44_ydir_path = '../FWHMsc44Ps_RS2023_dcs__C1000_x40y40z40_I20ydir.csv'
sc44_ydir5k_path = '../FWHMsc44Ps_RS2023_dcs__C5000_x40y40z40_I20ydir.csv'
sc44_ydir10k_path = '../FWHMsc44Ps_RS2023_dcs__C10000_x40y40z40_I20ydir.csv'

sc44_zdir_path = '../FWHMsc44Ps_RS2023_dcs__C1000_x40y40z40_I20zdir.csv'
sc44_zdir5k_path = '../FWHMsc44Ps_RS2023_dcs__C5000_x40y40z40_I20zdir.csv'
sc44_zdir10k_path = '../FWHMsc44Ps_RS2023_dcs__C10000_x40y40z40_I20zdir.csv'

as72_ydir_path = '../FWHMas72Ps_RS2023_dcs__C1000_x40y40z40_I20ydir.csv'
as72_zdir_path = '../FWHMas72Ps_RS2023_dcs__C1000_x40y40z40_I20zdir.csv'

ga68_ydir_path = '../FWHMga68Ps_RS2023_dcs__C300_x40y40z40_I20ydir.csv'
ga68_zdir_path = '../FWHMga68Ps_RS2023_dcs__C300_x40y40z40_I20zdir.csv'



TotalIter = 20
it = np.arange(1,21)

a, fwhm_sc44 = load_data(sc44_path)
b, fwhm_as72 = load_data(as72_path)
c, fwhm_ga68 = load_data(ga68_path)

e, fwhm_sc44_5k = load_data(sc44_5k_path)
f, fwhm_sc44_10k = load_data(sc44_10k_path)

g, fwhm_sc44_ydir = load_data(sc44_ydir_path)
h, fwhm_sc44_zdir = load_data(sc44_zdir_path)

i, fwhm_sc44_ydir_5k = load_data(sc44_ydir5k_path)
j, fwhm_sc44_ydir_10k = load_data(sc44_ydir10k_path)

k, fwhm_as72_ydir = load_data(as72_ydir_path)
l, fwhm_ga68_ydir = load_data(ga68_ydir_path)

m, fwhm_as72_zdir = load_data(as72_zdir_path)
n, fwhm_ga68_zdir = load_data(ga68_zdir_path)

o, fwhm_sc44_zdir_5k = load_data(sc44_zdir5k_path)
p, fwhm_sc44_zdir_10k = load_data(sc44_zdir10k_path)

q, fwhm_sc44_80vox = load_data(sc44_80vx_path)

x, y_data = load_data(file_path)
x_data = np.linspace(-20,20,40)

single_fit = 1

if single_fit == 0:
    double_fit_params = fit_double_gaussian(x_data, y_data/max(y_data))
    # Print the fitted parameters for each Gaussian
    print('Fitted Parameters for Gaussian 1:')
    print('Amplitude:', double_fit_params[0])
    print('Mean:', double_fit_params[1])
    print('Standard Deviation:', double_fit_params[2])

    print('\nFitted Parameters for Gaussian 2:')
    print('Amplitude:', double_fit_params[3])
    print('Mean:', double_fit_params[4])
    print('Standard Deviation:', double_fit_params[5])

    # Plot the data and fitted curve
    plot_fit(x_data, y_data, double_fit_params)
else:
    fit_params, pcov_g = fit_gaussian(x_data, y_data/max(y_data))

    print('Fitted Parameters for Gaussian 1:')
    print('Amplitude:', fit_params[0])
    print('Mean:', fit_params[1])
    print('Standard Deviation:', fit_params[2])

    xg = np.linspace(-20,20,1000)
    yg = gaussian(xg, *fit_params)

    ymax = max(yg)
    halfmax = ymax/2
    print("half-max: " + str(halfmax))

    fwhm = 2*np.sqrt(2*np.log(2))*fit_params[2]
    print("fwhm: " + str(fwhm))

    #plot_fit(x_data, y_data, fit_params,single_fit)

err = 0
for i in it:
    err += (fwhm_sc44_80vox[i-1] - ((fwhm_sc44_80vox[i-1]+fwhm_sc44[i-1])/2))**2

rmse = np.sqrt(err*1/TotalIter)

bas = np.sum(np.abs(fwhm_sc44-fwhm_sc44_80vox))

print(fwhm_sc44[4]-fwhm_sc44_80vox[4])

print(bas/TotalIter)

print("rmse: " + str(rmse))

fig, ax = plt.subplots()

fig.set_figheight(6)
fig.set_figwidth(10)

ax.set_title('FWHM z-direction',fontsize=14)
ax.set_xlabel('Iteration #')
ax.set_ylabel('FWHM (mm)')
ax.plot(it,fwhm_sc44_zdir,'o--',linewidth=1,label="Sc-44")
ax.plot(it,fwhm_as72_zdir,'d-.',linewidth=1,label="As-72")
ax.plot(it,fwhm_ga68_zdir,'s:',linewidth=1,label="Ga-68")
ax.xaxis.set_ticks(np.arange(0,21,1))
ax.grid(True)
ax.legend()

plt.show()
fig.savefig('FWHM_comp_zdir.png',dpi=300)
fig.savefig('FWHM_comp_zdir.eps',dpi=300)
plt.close()