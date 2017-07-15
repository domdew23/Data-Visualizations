import json

from collections import OrderedDict
from country_codes import get_country_code
from pygal.style import RotateStyle, LightColorizedStyle
from pygal.maps import world as maps


def build_dict(country_name, population, pop_dict):
	code = get_country_code(country_name)
	if code:
		pop_dict[code] = population
	else:
		pass


def group_countries(cc_populations):
	# Group countries into 3 population levels
	cc_pops1, cc_pops2, cc_pops3 = {}, {}, {}
	for cc, pop in cc_populations.items():
		if pop < 10000000:
			cc_pops1[cc] = pop
		elif pop < 1000000000:
			cc_pops2[cc] = pop
		else:
			cc_pops3[cc] = pop
	return cc_pops1, cc_pops2, cc_pops3


def print_sorted(d, x):
	sorted_dict = OrderedDict(sorted(d.items(), key=lambda t: t[x]))

	for c,p in sorted_dict.items():
		print(c + ": " + str(p))


# Load the data into a list
filename = 'json_files/population_data.json'
with open(filename) as file:
	pop_data = json.load(file)

# Build a dictionary of population data
cc_populations = {}

# Print the 2010 population for each country
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		build_dict(country_name, population, cc_populations)

cc_pops1, cc_pops2, cc_pops3 = group_countries(cc_populations)

# See how many countries are in each level
print(len(cc_pops1), len(cc_pops2), len(cc_pops3))

wm_style = RotateStyle('#336699', base_style = LightColorizedStyle)
wm = maps.World(style=wm_style)
wm.title = "World Population in 2010, by Country"
wm.add('0 - 10 million', cc_pops1)
wm.add('10 million - 1 billion', cc_pops2)
wm.add('> 1 billion', cc_pops3)

wm.render_to_file('graphs/world_populations.svg')




