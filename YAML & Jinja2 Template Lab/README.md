**YAML and Jinja2 Template**

*This is note from my early study in network automation, so this is far from perfection. Please use as reference only.*

**There are 3 files:**
- Python Loader, to combine template file and context file in YAML and write it into a file in txt format.
- YAML context file, edit this file to add the parameters for the devices.
- Jinja2 template file, this is the skeleton of the configuration file, we fill the variables with the data from context file

**Rendering**
To create the config file from those 3 files above, I'm using Powershell and navigate to the local directory of the project then execute with command:

```shell
PS E:\Loader Test 1> python Config_Loader.py config_template.j2 config.yml
```

`Loader Test 1` is the local directory where the project located, and `python Config_Loader.py config_template.j2 config.yml` is the command used for rendering the configuration file.

If succeeded, you can see the file configuration named "rendered_config.txt" in the Loader Test 1 folder created. You may see the configuration result in that file.

