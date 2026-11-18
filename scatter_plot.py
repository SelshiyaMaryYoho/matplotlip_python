# Scatter Plot
# Definition: A scatter plot is used to show the relationship between two numerical variables.

# Example: Study hours and exam marks.



import matplotlib.pyplot as plt

# Data
study_hours = [1, 2, 3, 4, 5, 6]
marks = [40, 50, 60, 65, 80, 90]

# Create scatter plot
plt.scatter(study_hours, marks, label="Students")

# Add title and labels
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

# Show legend
plt.legend()

# Display chart
plt.show()