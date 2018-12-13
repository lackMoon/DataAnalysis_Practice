import json
import pygal.maps.world
from pygal.style import LightColorizedStyle,RotateStyle
from country_codes import get_country_code
filename='population_data.json'
country_population={}
with open(filename) as f:
    pop_data=json.load(f)
for pop in pop_data:
    if pop['Year']=='2010':
        country_name=pop['Country Name']
        population=int(float(pop['Value']))
        code=get_country_code(country_name)
        if code:
            country_population[code]=population
population_low,population_mid,population_high={},{},{}
for cc,pops in country_population.items():
    if pops<10000000:
        population_low[cc]=pops
    elif pops<1000000000:
        population_mid[cc]=pops
    else:
        population_high[cc]=pops
wm_style=RotateStyle('#336699',base_style=LightColorizedStyle)
wm=pygal.maps.world.World(style=wm_style)
wm.title="World Population in 2010"
wm.add('low population',population_low)
wm.add('mid population',population_mid)
wm.add('high population',population_high)
wm.render_to_file('world_population.svg')
