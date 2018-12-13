import pygal
from die import Die
die1=Die()
die2=Die(10)
results=[]
frequencies=[]
for roll_num in range(50000):
    result=die1.roll()+die2.roll()
    results.append(result)
max_results=die1.num_sides+die2.num_sides
for value in range(2,max_results+1):
    frequency=results.count(value)
    frequencies.append(frequency)
hist=pygal.Bar()
hist.title="Results of rolling D6-1 and D6-2"
hist.x_labels=[]
for x in range(2,17):
    hist.x_labels.append(x)
hist.x_title="Result"
hist.y_title="Frequency"
hist.add('D61+D62',frequencies)
hist.render_to_file('die_visual.svg')
