import matplotlib.pyplot as plt 

upper_bound = 1
lower_bound = 1001

x_values = list(range(upper_bound,lower_bound))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, edgecolor='none', c=y_values, cmap=plt.cm.Blues, s=40)

# Set chart title and label axis
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
plt.axis([0, 1100, 0, 1100000])

plt.savefig('graphs/squares_scatter_plot.png', bbox_inches='tight')
plt.show()