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





def generate_frame_y_symmetry(t, N, entanglement_phase):
    frame = np.zeros((N, N, 3))
    for i in range(N):
        for j in range(N):
            # Calculate hue from wavefunction
            hue = wavefunction(i, j, t) * 180 + 180  # Normalize to [0, 360]
            # Calculate entangled hue and assign to the pixel on the opposite end of the y-axis
            entangled_hue = wavefunction(i, N-1-j, t, phi=entanglement_phase) * 180 + 180
            # Store the regular hue at position (i, j)
            frame[i, j] = get_color(hue)[:3]
            # Store the entangled hue at position (i, N-1-j)
            frame[i, N-1-j] = get_color(entangled_hue)[:3]
    return frame

def update_plot(frame_number, N, entanglement_phase, img):
    frame = generate_frame_y_symmetry(frame_number * np.pi / 5, N, entanglement_phase)
    img.set_array(frame)
    return img

def main(filename, N, frames=100, interval=100):
    #N = 100  # Image resolution (100x100 pixels)
    fig, ax = plt.subplots()

    # Set aspect ratio and remove axes
    ax.axis('off')

    # Adjust figure margins
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

    img_plot = ax.imshow(np.zeros((N, N, 3)), interpolation='nearest', aspect='auto')

    ani = FuncAnimation(fig, update_plot, frames=frames, fargs=(N, np.pi/4, img_plot), interval=interval)

    # Save the animation as an MP4
    ani.save(f'{filename}.mp4', writer='ffmpeg', fps=10)
    plt.close()

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a filename.')
    parser.add_argument('filename', type=str, help='The path')
    parser.add_argument('N',type=int, help="N pixels")
    args = parser.parse_args()

    main(args.filename, args.N)
