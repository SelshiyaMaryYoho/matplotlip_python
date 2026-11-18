# 1. What is Matplotlib?
# Matplotlib is a Python library used to create graphs and charts from data.

# We use Matplotlib to visualize data and understand it easily.

# For example:
# - Line chart – to show changes over time.
# - Bar chart – to compare values.
# - Histogram – to show the distribution of data.
# - Scatter plot – to show the relationship between two values.
# -pip install matplotlib
# Line Chart
# Definition: A line chart is used to show changes or trends over time.

# Example: Monthly sales.

# X-axis: Horizontal line (bottom).
# Y-axis: Vertical line (left).
# Title: Name of the graph.
# Legend: Explains what the line, bars, or points represent.

import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 120, 180, 200]

# Create line chart
plt.plot(months, sales, label="Sales")

# Add title and labels
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

# Show legend
plt.legend()

# Display chart
plt.show()