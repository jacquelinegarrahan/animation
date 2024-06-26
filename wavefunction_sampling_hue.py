import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image
import random

def wavefunction(x, y, t, w=1, phi=0):
    # Simple harmonic wavefunction
    return np.sin(w * (x + y) + t + phi)

def get_color(hue):
    # Convert hue to RGB using matplotlib
    return plt.cm.hsv(hue/360)  # Normalized hue to [0, 1]

def generate_frame(t, N, entanglement_phase):
    frame = np.zeros((N, N, 3))
    for i in range(N):
        for j in range(N):
            # Calculate hue from wavefunction
            hue = wavefunction(i, j, t) * 180 + 180  # Normalize to [0, 360]
            entangled_hue = wavefunction(i, j, t, phi=entanglement_phase) * 180 + 180
            avg_hue = (hue + entangled_hue) / 2
            avg_hue = random.choice([hue, entangled_hue])
            frame[i, j] = get_color(avg_hue)[:3]
    return frame

def update_plot(frame_number, N, entanglement_phase, img):
    frame = generate_frame(frame_number * np.pi / 5, N, entanglement_phase)
    img.set_array(frame)
    return img

N = 100  # Image resolution (100x100 pixels)
fig, ax = plt.subplots()

# Set aspect ratio and remove axes
ax.axis('off')

# Adjust figure margins
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

img_plot = ax.imshow(np.zeros((N, N, 3)), interpolation='nearest', aspect='auto')

ani = FuncAnimation(fig, update_plot, frames=100, fargs=(N, np.pi/4, img_plot), interval=100)

# Save the animation as an MP4
ani.save('wavefunction_animation.mp4', writer='ffmpeg', fps=10)
plt.close()