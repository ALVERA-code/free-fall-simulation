import numpy as np
import matplotlib.pyplot as plt

# constants
g = 9.81
dt = 0.1
t_max = 300

# Felix parameters
m = 80              # mass (kg)
Cd = 1.0            # drag coefficient
A = 0.7             # cross-sectional area (m^2)

# atmosphere
rho0 = 1.225        # density at ground
H = 8400            # scale height

# initial conditions
v = 0
h = 39000           # starting height (m)

# lists
time = []
velocity = []
height = []

t = 0

while t <= t_max and h > 0:
    # air density decreases with height
    rho = rho0 * np.exp(-h / H)
    
    # drag force
    drag = 0.5 * rho * Cd * A * v**2
    
    # direction: drag opposes motion
    if v > 0:
        drag = drag
    else:
        drag = -drag
    
    # acceleration
    a = g - drag / m
    
    # update velocity and position
    v = v + a * dt
    h = h - v * dt   # subtract because falling down
    
    # store data
    time.append(t)
    velocity.append(v)
    height.append(h)
    
    t += dt
    
print("Max velocity:", max(velocity), "m/s")

# plots
plt.figure(figsize=(10,4))

plt.subplot(1,3,1)
plt.plot(time, velocity)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity vs Time")

plt.subplot(1,3,2)
plt.plot(time, height)
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Height vs Time")

plt.subplot(1,3,3)
plt.plot(velocity,height)
plt.xlabel("Velocity (m/s)")
plt.ylabel("Height (m)")
plt.title("Velocity vs Height")

plt.tight_layout()
plt.show()

