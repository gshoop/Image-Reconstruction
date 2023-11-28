import csv
import numpy as np
from scipy.optimize import curve_fit
from pylab import *
import scipy.optimize as opt
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

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
    initial_guess = [max(y_data), -0.5, 4]
    popt, _ = curve_fit(gaussian, x_data, y_data, p0=initial_guess)
    return popt

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
        r1, r2 = spline.roots()

        fwhm = 2*np.sqrt(2*np.log(2))*fit_params[2]
        axvspan(r1,r2, facecolor='g', alpha=0.5)
        #axvspan(fit_params[1]-fwhm/2, fit_params[1]+fwhm/2, facecolor='y', alpha=0.5)

    plt.legend()
    plt.show()

# Example usage
file_path = '../sc44Ps_RS2023_dcs__C1000_x40y40z40_I10.csv'
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
    fit_params = fit_gaussian(x_data, y_data/max(y_data))

    print('Fitted Parameters for Gaussian 1:')
    print('Amplitude:', fit_params[0])
    print('Mean:', fit_params[1])
    print('Standard Deviation:', fit_params[2])

    xg = np.linspace(-20,20,1000)
    yg = gaussian(xg, *fit_params)

    ymax = max(yg)
    halfmax = ymax/2
    print("half-max: " + str(halfmax))

    spline = UnivariateSpline(xg, yg - np.max(yg)/2, s=0)
    r1, r2 = spline.roots()

    print("new fwhm: " + str(r2-r1))

    fwhm = 2*np.sqrt(2*np.log(2))*fit_params[2]
    print("fwhm: " + str(fwhm))

    plot_fit(x_data, y_data, fit_params,single_fit)
