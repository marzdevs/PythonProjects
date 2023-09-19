import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
x = np.linspace(0, 10, 50)  # Create an array of 50 points from 0 to 10
y_line = 2 * x + 1  # Line plot data (y = 2x + 1)
y_scatter = np.random.rand(50)  # Scatter plot data (random numbers)
categories = ['Category A', 'Category B', 'Category C']
values = [30, 45, 15]  # Bar chart data

# Create subplots
plt.figure(figsize=(12, 4))

# Line Plot
plt.subplot(131)
plt.plot(x, y_line, label='y = 2x + 1', color='blue', linestyle='-')
plt.title('Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Scatter Plot
plt.subplot(132)
plt.scatter(x, y_scatter, label='Random Data', color='green', marker='o')
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Bar Chart
plt.subplot(133)
plt.bar(categories, values, color='purple')
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()