import csv
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Function to fit a double Gaussian curve
def double_gaussian(x, amp1, mean1, stddev1, amp2, mean2, stddev2):
    return (amp1 * np.exp(-((x - mean1) / (2 * stddev1))**2) +
            amp2 * np.exp(-((x - mean2) / (2 * stddev2))**2))

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
    initial_guess = [max(y_data)/2, -5.5, 3,
                     max(y_data)/2, 5.5, 3]
    popt, _ = curve_fit(double_gaussian, x_data, y_data, p0=initial_guess)
    return popt

# Plot the data and fitted curve
def plot_fit(x_data, y_data, fit_params):
    plt.step(x_data, y_data/max(y_data), label='Data')
    x_data = np.linspace(-20,20,1000)
    plt.plot(x_data, double_gaussian(x_data, *fit_params), 'r', label='Fit')
    plt.legend()
    plt.show()

# Example usage
file_path = 'sc442Ps_dcs__C10000_x80y80z80_I7.csv'
x, y_data = load_data(file_path)
x_data = np.linspace(-20,20,80)
fit_params = fit_double_gaussian(x_data, y_data/max(y_data))

# Print the fitted parameters for each Gaussian
print('Fitted Parameters for Gaussian 1:')
print('Amplitude:', fit_params[0])
print('Mean:', fit_params[1])
print('Standard Deviation:', fit_params[2])

print('\nFitted Parameters for Gaussian 2:')
print('Amplitude:', fit_params[3])
print('Mean:', fit_params[4])
print('Standard Deviation:', fit_params[5])

# Plot the data and fitted curve
plot_fit(x_data, y_data, fit_params)
