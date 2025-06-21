import numpy as np
import matplotlib.pyplot as plt

# Parameters for the hyperbolic trajectory
e = 1.5              # Eccentricity           
l = 1.0              # Semi-latus rectum
theta = np.linspace(-2*np.pi/3, 2*np.pi/3, 1000)    # Angular range

# Hyperbolic orbit equation in polar form
r = l / (1 + e * np.cos(theta))

# Convert polar coordinates to Cartesian for plotting
x = r * np.cos(theta)
y = r * np.sin(theta)

#Plot the trajectory and central body
plt.plot(x, y, label='Hyperbolic Trajectory', color='blue')
plt.plot(0, 0, 'ro', label='Planet (Focus)')
plt.title('Hyperbolic Flyby Trajectory')
plt.xlabel('x (units)')
plt.ylabel('y (units)')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()