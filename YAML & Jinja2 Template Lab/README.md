# This is note from my early study in network automation, so this is far from perfection. Please use as reference only.

## There are 3 files:
1. Python Loader, to combine template file and context file in YAML and write it into a file in txt format.
2. YAML context file, edit this file to add the parameters for the devices.
3. Jinja2 template file, this is the skeleton of the configuration file, we fill the variables with the data from context file

## Rendering
To create the config file from those 3 files above, I'm using Powershell and navigate to the local directory of the project then execute with command:

'''powershell
PS E:\Loader Test 1> python Config_Loader.py config_template.j2 config.yml
'''
"<b>Loader Test 1</b>" is the local directory where the project located, and "<b>python Config_Loader.py config_template.j2 config.yml"</b> is the command used for rendering the configuration file.

If succeeded, you can see the file configuration named "<b>rendered_config.txt</b>" in the Loader Test 1 folder created. You may see the configuration result in that file.

