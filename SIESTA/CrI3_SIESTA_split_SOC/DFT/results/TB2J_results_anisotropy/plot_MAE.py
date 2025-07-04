import matplotlib.pyplot as plt
import numpy as np

def plot_MCA(fname):
    """
    plot the third column of a file against the first column.
    """
    data = np.loadtxt(fname)
    x = data[:, 0]/np.pi * 180  # Convert radians to degrees
    y = data[:, 2] - data[0, 2]
    plt.plot(x, y,  color='blue', marker='o', linestyle='-')
    plt.xlabel('$\phi$')
    plt.ylabel('$\Delta E$(meV)')
    plt.grid()
    plt.show()

plot_MCA("MAE.dat")
