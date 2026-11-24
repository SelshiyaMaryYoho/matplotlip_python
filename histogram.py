# Histogram
# Definition: A histogram is used to show the distribution of numerical data. 
# It groups values into intervals called bins.

# Example: Students' marks distribution

import matplotlib.pyplot as plt

# Data
marks = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# Create histogram
plt.hist(marks, bins=5, label="Marks")

# Add title and labels
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

# Show legend
plt.legend()

# Display chart
plt.show()