#!/usr/bin/env python3
"""Simple script to plot magnon band structure from saved data."""

from TB2J.magnon.magnon_band import MagnonBand
import matplotlib.pyplot as plt

def plot_magnon_bands(input_file, output_file=None, ax=None, color='blue', show=True):
    """Load and plot magnon band structure.
    
    Parameters
    ----------
    input_file : str
        JSON file containing band structure data
    output_file : str, optional
        Output file for saving the plot
    ax : matplotlib.axes.Axes, optional
        Axes for plotting. If None, creates new figure
    color : str, optional
        Color of the band lines (default: blue)
    show : bool, optional
        Whether to show the plot on screen (default: True)
    
    Returns
    -------
    matplotlib.axes.Axes
        The plotting axes
    """
    # Load band structure data
    bands = MagnonBand.load(input_file)
    
    # Create plot
    ax = bands.plot(
        ax=ax,
        filename=output_file,
        color=color,
        show=show
    )
    return ax

if __name__ == "__main__":
    # Usage example
    # Example usage
    import matplotlib.pyplot as plt
    
    # Create a figure and axis (optional)
    fig, ax = plt.subplots(figsize=(6, 4))
    
    # Plot bands with custom color on given axis
    plot_magnon_bands(
        input_file="magnon_bands.json",
        output_file="magnon_bands.png",
        ax=ax,
        color='red',
        show=True
    )
