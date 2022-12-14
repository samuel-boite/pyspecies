import numpy as np

from pyspecies import models, pop

# Define population and interaction model
q = pop.Pop(
    space=(0, 1, 200),
    u0=lambda x: 1 + np.cos(2 * np.pi * x),
    v0=lambda x: 1 + np.sin(2 * np.pi * x),
    model=models.SKT(
        D=np.array([[1, 0, 1], [1e-3, 0, 0]]),
        R=np.array([[4, 2, 0], [1, 1, 0]])
    ),
)

# Run two simulation passes at different speeds
q.sim(duration=0.1, N=200)
q.sim(duration=2.9, N=200)

# Animate the result
q.anim()

# Plot a heatmap of the dominating species across time
q.heatmap()