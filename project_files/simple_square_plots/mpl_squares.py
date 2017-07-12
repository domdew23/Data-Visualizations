import matplotlib.pyplot as plt

input_values = list(range(1,6))
squares = [x**2 for x in input_values]
plt.plot(input_values, squares, linewidth=5)

# Set the chart title and label axis
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.savefig('graphs/squares_plot.png', bbox_inches='tight')
plt.show()