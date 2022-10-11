import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def animate(i):
    idx = np.linspace(0,1,100);
    val = idx;
    plt.cla()
    plt.plot(idx, val, marker='o')

ani = FuncAnimation(plt.gcf(), animate, interval=2)
plt.show()