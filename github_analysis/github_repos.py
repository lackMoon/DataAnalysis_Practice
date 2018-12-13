import requests
import pygal
from pygal.style import LightColorizedStyle,LightenStyle

url='https://api.github.com/search/repositories?q=language:python&sort=stars'
response=requests.get(url)
response_dict=response.json()
repo_dicts=response_dict["items"]
names,star_plots=[],[]
for repo in repo_dicts:
    names.append(repo['name'])
    star_plot={
        'value':repo['stargazers_count'],
        'label':str(repo['description']),
        'xlink':repo['html_url'],
    }
    star_plots.append(star_plot)
my_style=LightenStyle('#333366',base_style=LightColorizedStyle)
my_config=pygal.Config()
my_config.x_label_rotation=30
my_config.show_legend=False
my_config.title_font_size=24
my_config.label_font_size=14
my_config.major_label_font_size=18
my_config.truncate_label=15
my_config.show_y_guides=False
my_config.width=1000
chart=pygal.Bar(config=my_config,style=my_style)
chart.title="Most starred Python projects on Github"
chart.x_labels=names
chart.add('',star_plots)
chart.render_to_file('github_repo.svg')