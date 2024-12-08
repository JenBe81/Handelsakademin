import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.colors import Normalize

print("Task: Plotting in Matploglib can be done in either of two ways, which ones? Which way is the commended approach?")
print("Either explicitly or implicitly. Explicitly means creating Figures and Axes and calls methods to configure them in a specific way. Inplicitly refers to using pyplot functions for plotting that will themselves setup everything for you")
print("Implicit may be used for quick testing but genreally the explicit way is recommended.")

print("\nTask: Explain shortly what a figure, exes, axis and an artist is in Matplotlib.")
print("The all describe the different parts of the matplotlib plot. Figure is the drawing area, Artist is everything visisble on the figure. Exes sets up the plotting area, e.g. setting labels, title, ticks and so on. Axis is an object to Axes, usually two or three and are what we normally refer to as exis when plotting graphs. ")

print("\nTask: When plotting in Matploglib, what is the expected input data type?")
print("The expected input data type is numpy.array. If other data types are to be plotted it is recommended to convert them to numpy.array before plotting.")

print("\nTask: Create a plot of the function y = x^2 [from -4 to 4], hint use the np.linspace function, both in the oo approach and the pyplot approach. Your plot hsould have a title and axis-labels")

# Creating the x-values and y-values to be plotted
num_samples = 1000
x_values = np.linspace(-4, 4, num_samples)
y_values = x_values ** 2

# setting up the plot using the OO approach
fig, ax = plt.subplots()
ax.plot(x_values, y_values, label='quatratic', color = 'red')
ax.set_title("Function y = x^2")
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.yaxis.set_ticks_position('both')
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.legend()
#plt.show()

# setting up the plot using the implicit approach
plt.plot(x_values, y_values, label="y = x^2")
plt.title("Function y = x^2")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
#plt.legend()
#plt.show()

print("\nTask: Create a figure containing 2 subplots where the first is a scatter plot and the second is a bar plot. You have the data below.")
# Data for scatter plot
np.random.seed(15)
random_data_x = np.random.randn(1000)
random_data_y = np.random.randn(1000)
x = np.linspace(-2, 2, 100)
y = x**2

# Data for bar plot
fruit_data = {'grapes': 22, 'apple': 8, 'orange': 15, 'lemon': 20, 'lime': 25}
names = list(fruit_data.keys())
values = list(fruit_data.values())

fix, axs = plt.subplots(2, 1, figsize=(10, 8))
random_colors = np.random.rand(len(random_data_x))
axs[0].scatter(random_data_x,
               random_data_y,
               s=100,              # Size of each data point
               c=random_colors,    # Color of data points
               alpha=0.7,          # Transparency (0 - fully transparent, 1 - fully opaque)
               marker='o',         # Marker style (e.g. 'o' - circle, 's' - square, '*' - star)
               edgecolors='black', # Edge color for markers
               linewidths=1.5)     # Line width for marker edges
axs[0].set_xlabel('random x values')
axs[0].set_ylabel('random y values')

axs[1].bar(names,
       values,
       color='skyblue',       # Bar color
       edgecolor='black',     # Edge color
       width=0.6,             # Bar width (default is 0.8)
       align='center',        # Alignment ('center' or 'edge')
       hatch='/')             # Hatch pattern (e.g., '/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*')

ax.set_ylabel('Quantity')
plt.tight_layout()
plt.show()