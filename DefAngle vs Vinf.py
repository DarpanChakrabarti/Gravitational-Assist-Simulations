import numpy as np
import matplotlib.pyplot as plt

G = 6.674e-11  # m^3 kg^-1 s^-2 
M = 5.972e24   # kg (mass of Earth)
vinf = np.linspace(5e3, 25e3, 1000)  # m/s
b_val = 8.973e6 # Impact parameter range (m)
mu = G * M

alpha_squared = (b_val**2 * vinf**4) / mu**2 # Calculate deflection angle in degrees
delta_rad = 2 * np.arcsin(1 / np.sqrt(1 + alpha_squared))
delta_deg = np.degrees(delta_rad)

# Plot
plt.figure(figsize=(8, 5)) 
plt.plot(vinf / 1e3, delta_deg, color='darkblue')
plt.xlabel('Asymptotic velocity $V_{\infty}$ (km/s)')
plt.ylabel('Deflection angle $\\delta$ (degrees)')
plt.title('Deflection angle vs. Asymptotic velocity')
plt.grid(True)
plt.show()