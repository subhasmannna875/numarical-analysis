import numpy as np
import matplotlib.pyplot as plt
# Planck's constant (Joule second)
h = 6.626e-34

# Speed of light (meters per second)
c = 3.0e+8

# Boltzmann constant (Joules per Kelvin)
k = 1.38e-23

# Constants
T_cmb = 2.725  # Temperature of the CMB in Kelvin

# Function to calculate the black body spectrum
def black_body_spectrum(frequency, temperature):
    # Planck's law
    return (2 * h *c* frequency**3 ) * (1 / (np.exp((h *c* frequency*100) / (k * temperature)) - 1))*10**26
    #return (2 * h * c**2*frequency**5) / ( (np.exp((h * c*frequency*100) / ( k* temperature)) - 1))*10**29

# Load data from NASA
data = np.loadtxt('blackbodydata.txt')

# Extract frequency and CMB flux
frequency = data[:, 0]
cmb_flux = data[:, 1]

# Calculate black body spectrum
bb_spectrum = black_body_spectrum(frequency, T_cmb)
print("Data for BB Spectrum",bb_spectrum)
print(k)

# Plot the black body spectrum
plt.plot(frequency, bb_spectrum, label='Black Body Spectrum (T=2.725 K)',linestyle="--")

# Superimpose the CMB flux
plt.plot(frequency, cmb_flux, label='CMB Flux',linestyle="dotted")

# Find the wavelength at which the black body spectrum peaks
peak_wavelength_index = np.argmax(bb_spectrum)
peak_wavelength = 1/ (100*frequency[peak_wavelength_index])#here we change wave length from meater to cm
print(f"The wavelength at which the black body spectrum peaks is approximately {peak_wavelength:.2e} meters.")

# Add labels and legend
plt.xlabel('Frequency (Hz)')
plt.ylabel('Spectral Radiance')
plt.legend()

# Save the plot to a PDF file
plt.savefig('cmb_spectrum_plot.pdf')

# Show the plot
plt.show()
