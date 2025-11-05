
import matplotlib.pyplot as plt

# Scatter Plot Example
x = [5, 7, 8, 10, 12, 14]
y = [12, 14, 17, 20, 23, 25]

plt.scatter(x, y, color='purple', marker='o')
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
