import matplotlib.pyplot as plt

# Pie Chart Example
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [25, 30, 20, 25]
colors = ['red', 'yellow', 'pink', 'brown']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart Example')
plt.show()
