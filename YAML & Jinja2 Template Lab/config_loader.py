import sys
import yaml
from jinja2 import Environment, FileSystemLoader

# Initialize the Jinja2 environment to load template from current directory
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template(sys.argv[1])

# Load the context YAML file into a Python dictionary
with open(sys.argv[2], 'r') as datafile:
    context = yaml.load(datafile)

# Render the template and print the resulting document
rendered_template = template.render(**context)
print(rendered_template)

# convert to file text.txt
with open("rendered_config.txt", "w") as f:
    f.write(rendered_template)
