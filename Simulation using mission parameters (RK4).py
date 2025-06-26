import numpy as np
import matplotlib.pyplot as plt

# Physical constants
GRAVITATIONAL_CONSTANT = 6.674e-11  # m^3 kg^-1 s^-2
EARTH_MASS = 5.972e24               # kg
EARTH_RADIUS = 6.371e6              # meters

# Simulation settings
TIME_STEP = 0.01                    # seconds
MAX_SIMULATION_STEPS = 8000000      # total steps
INITIAL_X_POSITION = -5e8           # meters
INITIAL_Y_VELOCITY = 0              # m/s

def compute_gravitational_acceleration(x_position, y_position):

    distance = np.sqrt(x_position**2 + y_position**2)
    force_magnitude = (GRAVITATIONAL_CONSTANT * EARTH_MASS) / (distance**2)
    acceleration_x = -force_magnitude * (x_position / distance)
    acceleration_y = -force_magnitude * (y_position / distance)
    return acceleration_x, acceleration_y

def simulate_flyby_trajectory(impact_parameter, approach_velocity):
    
    # Set initial conditions
    initial_y_position = impact_parameter
    initial_distance = np.sqrt(INITIAL_X_POSITION**2 + initial_y_position**2)
    initial_x_velocity = np.sqrt(approach_velocity**2 + 
                                (2 * GRAVITATIONAL_CONSTANT * EARTH_MASS) / initial_distance)
    
    # Initialize position arrays
    x_positions = np.zeros(MAX_SIMULATION_STEPS + 1)
    y_positions = np.zeros(MAX_SIMULATION_STEPS + 1)
    x_positions[0] = INITIAL_X_POSITION
    y_positions[0] = initial_y_position
    
    # Initialize velocity components
    velocity_x = initial_x_velocity
    velocity_y = INITIAL_Y_VELOCITY
    
    # Runge-Kutta 4 integration
    for step in range(MAX_SIMULATION_STEPS):
        current_x = x_positions[step]
        current_y = y_positions[step]
        
        # First RK4 step
        acc_x1, acc_y1 = compute_gravitational_acceleration(current_x, current_y)
        velocity_change_x1 = acc_x1 * TIME_STEP
        velocity_change_y1 = acc_y1 * TIME_STEP
        position_change_x1 = velocity_x * TIME_STEP
        position_change_y1 = velocity_y * TIME_STEP
        
        # Second RK4 step
        midpoint_x = current_x + position_change_x1/2
        midpoint_y = current_y + position_change_y1/2
        acc_x2, acc_y2 = compute_gravitational_acceleration(midpoint_x, midpoint_y)
        velocity_change_x2 = acc_x2 * TIME_STEP
        velocity_change_y2 = acc_y2 * TIME_STEP
        position_change_x2 = (velocity_x + velocity_change_x1/2) * TIME_STEP
        position_change_y2 = (velocity_y + velocity_change_y1/2) * TIME_STEP
        
        # Third RK4 step
        midpoint_x = current_x + position_change_x2/2
        midpoint_y = current_y + position_change_y2/2
        acc_x3, acc_y3 = compute_gravitational_acceleration(midpoint_x, midpoint_y)
        velocity_change_x3 = acc_x3 * TIME_STEP
        velocity_change_y3 = acc_y3 * TIME_STEP
        position_change_x3 = (velocity_x + velocity_change_x2/2) * TIME_STEP
        position_change_y3 = (velocity_y + velocity_change_y2/2) * TIME_STEP
        
        # Fourth RK4 step
        next_x = current_x + position_change_x3
        next_y = current_y + position_change_y3
        acc_x4, acc_y4 = compute_gravitational_acceleration(next_x, next_y)
        velocity_change_x4 = acc_x4 * TIME_STEP
        velocity_change_y4 = acc_y4 * TIME_STEP
        position_change_x4 = (velocity_x + velocity_change_x3) * TIME_STEP
        position_change_y4 = (velocity_y + velocity_change_y3) * TIME_STEP
        
        # Combine RK4 steps
        combined_position_change_x = (position_change_x1 + 2*position_change_x2 + 
                                      2*position_change_x3 + position_change_x4)/6
        combined_position_change_y = (position_change_y1 + 2*position_change_y2 + 
                                      2*position_change_y3 + position_change_y4)/6
        combined_velocity_change_x = (velocity_change_x1 + 2*velocity_change_x2 + 
                                      2*velocity_change_x3 + velocity_change_x4)/6
        combined_velocity_change_y = (velocity_change_y1 + 2*velocity_change_y2 + 
                                      2*velocity_change_y3 + velocity_change_y4)/6
        
        # Update position and velocity
        x_positions[step+1] = current_x + combined_position_change_x
        y_positions[step+1] = current_y + combined_position_change_y
        velocity_x = velocity_x + combined_velocity_change_x
        velocity_y = velocity_y + combined_velocity_change_y
        
        # Stop simulation if spacecraft moves far away
        if (x_positions[step+1] > 0 and 
            np.sqrt(x_positions[step+1]**2 + y_positions[step+1]**2) > 2*abs(INITIAL_X_POSITION)):
            x_positions = x_positions[:step+2]
            y_positions = y_positions[:step+2]
            break
    
    return x_positions, y_positions

# Run simulation
APPROACH_VELOCITY = 16.01e3  # m/s
IMPACT_PARAMETER = 8.973e6   # m
x_trajectory, y_trajectory = simulate_flyby_trajectory(IMPACT_PARAMETER, APPROACH_VELOCITY)

# Plot results
plt.figure(figsize=(10, 8))
plt.plot(x_trajectory/1000, y_trajectory/1000, label='Trajectory')
earth_disk = plt.Circle((0, 0), EARTH_RADIUS/1000, color='blue', alpha=0.2, label='Planet Surface')
plt.gca().add_artist(earth_disk)
plt.xlabel('x(km)')
plt.ylabel('y(km)')
plt.title('Hyperbolic Flyby Around a Planet')
plt.grid(True)
plt.axis('equal')
plt.legend()
plt.show()

# Calculate theoretical deflection angle
standard_gravitational_parameter = GRAVITATIONAL_CONSTANT * EARTH_MASS
impact_distance = IMPACT_PARAMETER
approach_speed = APPROACH_VELOCITY
alpha_parameter = 1 / np.sqrt(1 + (impact_distance**2 * approach_speed**4) / 
                             standard_gravitational_parameter**2)
theoretical_deflection_angle = 2 * np.arcsin(alpha_parameter) * (180/np.pi)

# Calculate numerical deflection angle
final_x_change = x_trajectory[-1] - x_trajectory[-2]
final_y_change = y_trajectory[-1] - y_trajectory[-2]
numerical_deflection_angle = np.arctan2(abs(final_y_change), abs(final_x_change)) * (180/np.pi)

# Display results
print("Theoretical deflection angle:", theoretical_deflection_angle, "degrees")
print("Numerical deflection angle:", numerical_deflection_angle, "degrees")
difference_percentage = (abs(theoretical_deflection_angle - numerical_deflection_angle) / 
                        theoretical_deflection_angle * 100)
print("Percentage difference: ", difference_percentage)
