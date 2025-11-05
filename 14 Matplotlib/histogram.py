import matplotlib.pyplot as plt
import numpy as np

# Histogram Example
data = np.random.randn(1000)

plt.hist(data, bins=30, edgecolor='black')
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
