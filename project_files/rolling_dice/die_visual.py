import pygal

from die import Die

# Create D6
die_1 = Die()
die_2 = Die()

roll_times = 1000000

# Make some rolls, and store results in a list
results = []
for _ in range(roll_times):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# Analyze results
frequencies = []
min_result = min(results)
max_result = die_1.num_sides + die_2.num_sides

for value in range(min_result, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling two die " + str(roll_times) + " times."
hist.x_labels = list(range(min_result, max_result+1))
hist.x_title = "Result"
hist.y_title = "Frequency Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('graphs/dice_visual.svg') 
