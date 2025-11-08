# Blackhole-sim🌌
🌌 Black Hole Light Ray Simulator
A 2D interactive simulation that visualizes how light rays behave near a black hole using simplified gravitational physics. Click anywhere on the screen to emit a photon—it will orbit, spiral inward, and disappear once it crosses the event horizon.

I built this to explore how black holes look, not just how they’re described. The simulation includes a thermal-inspired color gradient to represent rising energy and temperature as light approaches the singularity:

White → Red: Outer region (redshift, lower energy)
Red → Blue: Near the photon sphere (increasing temperature)
Blue → Dark Blue: Just outside the event horizon (extreme gravity)
Light rays that cross the event horizon are removed—just like in reality, nothing escapes.

🔧 Tech Stack
Python
Pygame
Newtonian gravity with damping (simplified model for visual intuition)
⚠️ Note: This isn’t a general relativity simulator—it’s a visual metaphor grounded in real concepts, built for curiosity and learning. 

📝 Why I Made This
I’ve always been fascinated by black holes—especially how they warp light and space. Instead of just watching videos or reading articles, I wanted to build something that lets you play with those ideas in real time.

This project started as a weekend experiment and turned into a deeper dive into orbital mechanics, color theory, and how to turn physics into visuals.

Made with curiosity. 

⚠️No photons were harmed (but many were swallowed).

## ⚙️ Parameterization Guide

To make the simulation more customizable and enable easy experimentation, you can adjust the following constants in `Blackholesimulation.py`:

```python
# Simulation Parameters
G = 2500        # Gravitational 'strength'; higher values = stronger attraction
DAMPING = 0.98  # Simulates energy loss / drag (range: 0.9 - 1.0 is typical)

# Black hole radii
bh_radius = int(min(width, height) * 0.04)              # Event horizon
photon_sphere = bh_radius * 8                           # Photon sphere radius
influence_radius = photon_sphere * 2                    # Where color transitions begin

# Color gradient stages (adjust these for different visual looks)
WHITE = (255, 255, 255)
DARK_BLUE = (0, 0, 139)
```

**How To Experiment:**
- Increase `G` for more dramatic gravity and faster photon in-spiral.
- Adjust `DAMPING` for more/less "drag"; set closer to `1.0` for nearly frictionless motion.
- Change `bh_radius`, `photon_sphere`, and `influence_radius` to scale the size of the black hole and transition zones.
- Modify `WHITE` or `DARK_BLUE` to experiment with the color gradient.

**Pro Tip:**  
For rapid prototyping, define these parameters at the top of your script and modify them through command line arguments or a config file for advanced use.
