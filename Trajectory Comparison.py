import numpy as np
import matplotlib.pyplot as plt


G = 6.674e-11          
M = 5.972e24            
mu = G * M             
planet_radius = 6.371e6
dt = 1               
n_steps = 10000         
b = 8.973e6         
x0 = -5e7
vy0 = 0
planet_radius = 6.371e6

def algo(b, vinf):    #Defining the function algo

    y0 = b                             
    ro = (x0**2 + y0**2)**0.5
    
    vx0 = (vinf**2 + (2*mu)/ro)**0.5
               
    x = [x0]
    y = [y0]
    vx = [vx0]
    vy = [vy0]
    
    for i in range(n_steps):
        r = np.sqrt(x[-1]**2 + y[-1]**2)
        ax = -mu * x[-1] / r**3
        ay = -mu * y[-1] / r**3
    
        vx_new = vx[-1] + ax * dt
        vy_new = vy[-1] + ay * dt
    
        x_new = x[-1] + vx_new * dt
        y_new = y[-1] + vy_new * dt
    
        x.append(x_new)
        y.append(y_new)
        vx.append(vx_new)
        vy.append(vy_new)
    
    return x, y #Returning the computed lists of x and y values


x1, y1 = algo(8.973e6, 16.01e3) #Cassini
x2, y2 = algo(11.261e6, 8.949e3) #Galileo I

# Plot the trajectory
plt.figure(figsize=(8, 8))
plt.plot(np.array(x1)/1e3, np.array(y1)/1e3, label='Trajectory for Cassini')  
plt.plot(np.array(x2)/1e3, np.array(y2)/1e3, label='Trajectory for Galileo I')  

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