import numpy as np
import matplotlib.pyplot as plt

# Gravitational constant and planetary parameters
G = 6.674e-11           # Gravitational constant (m^3 kg^-1 s^-2)
M = 5.972e24            # Mass of the Earth (kg)
mu = G * M              # Standard gravitational parameter (m^3 s^-2)
planet_radius = 6.371e6 # Radius of the Earth (m)
# Time step and duration
dt = 1                  # Time step (s)
n_steps = 10000         # Number of steps
x0 = -5e7               # Initial x-position (m), far left from the planet
vy0 = 0                 # Initial y-velocity (m/s), no vertical velocity

def algo(b, vinf):

    # Initial conditions for the spacecraft
    y0 = b                  # Initial y-position (m), equal to impact parameter

    # Compute radial distance and initial x-velocity using energy conservation
    ro = (x0**2 + y0**2)**0.5
    vx0 = (vinf**2 + (2*mu)/ro)**0.5

    # Initialize position and velocity lists
    x = [x0]
    y = [y0]
    vx = [vx0]
    vy = [vy0]

    # Numerical integration using Euler's method
    for i in range(n_steps):
        r = np.sqrt(x[-1]**2 + y[-1]**2)            # Distance from the planet
        ax = -mu * x[-1] / r**3                     # Acceleration in x due to gravity
        ay = -mu * y[-1] / r**3                     # Acceleration in y due to gravity

        vx_new = vx[-1] + ax * dt                   # Update velocity in x
        vy_new = vy[-1] + ay * dt                   # Update velocity in y

        x_new = x[-1] + vx_new * dt                 # Update position in x
        y_new = y[-1] + vy_new * dt                 # Update position in y

        # Append updated values to the lists
        x.append(x_new)
        y.append(y_new)
        vx.append(vx_new)
        vy.append(vy_new)
    
    return x, y # Returning the list of x and y values

vinf = 16.01e3          # Asymptotic incoming speed (m/s)
b = 8.973e6             # Impact parameter (m)
x1 , y1 = algo(b, vinf)

# Plot the trajectory
plt.figure(figsize=(8, 8))
plt.plot(np.array(x1)/1e3, np.array(y1)/1e3, label='Trajectory')  # Position in km

# Add the planet as a filled circle
circle = plt.Circle((0,0),planet_radius/1e3,color='r',alpha=0.2,label='Planet Surface')
plt.gca().add_artist(circle)

# Plot formatting
plt.xlabel("x (km)")
plt.ylabel("y (km)")
plt.title("Hyperbolic Flyby Around a Planet")
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()

# Calculation of deflection angle and velocity gain
alpha2 = (b**2 * vinf**4) / (mu)**2
alpha2 = (1 + alpha2)**0.5
alpha2 = 1 / alpha2

delv = (2*vinf*alpha2)/1e3
deflection_deg = (2 * np.arcsin(alpha2) * 180) / np.pi

print("Velocity gain: ", delv) # In km/s
print("Deflection angle:", deflection_deg)  # In degrees
