# Bar Chart
# Definition: A bar chart is used to compare values between different categories.

# Example: Comparing students' marks.

import matplotlib.pyplot as plt

# Data
students = ["Arun", "Priya", "Kumar", "Divya"]
marks = [80, 90, 70, 95]

# Create bar chart
plt.bar(students, marks, label="Marks")
# Add title and labels
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

# Show legend
plt.legend()

# Display chart
plt.show()