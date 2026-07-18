# free-fall-simulation
Simulation of free fall with air resistance using numerical methods in Python

# Felix Baumgartner Free Fall Simulation
This project simulates high-altitude free fall using numerical methods in Python.

It models:
- Gravity
- Air resistance (drag force)
- Changing air density with altitude

The simulation is inspired by Felix Baumgartner’s supersonic jump.

## Physics Model

Air density:
ρ = ρ₀ exp(-h/H)

Drag force:
F = 0.5 * ρ * Cd * A * v²

Acceleration:
a = g - F/m

## Results

- Maximum velocity ≈ 277 m/s
- Shows terminal velocity behavior
- Highlights effect of atmospheric density

## Run the code

pip install numpy matplotlib
python simulation.py

## Insight

The simulation underestimates maximum velocity compared to real data (~373 m/s),
likely due to constant drag coefficient and lack of compressibility effects.

This highlights the importance of posture and high-speed aerodynamics.
