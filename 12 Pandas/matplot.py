import matplotlib.pyplot as plt

x = [2, 6, 8, 10, 12]
y = [5, 12, 15, 18, 22]

z = [2,3,12,14,21]
m = [6,5,4,6,17]

# Line Plot
plt.plot(x,y, color = 'red')
plt.plot(z,m, color = 'green')

# Scatter Plot
plt.scatter(x,m, color = "purple")

plt.title("Line and Scatter Plot")

plt.show()