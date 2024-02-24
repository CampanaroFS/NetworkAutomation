import json
from jinja2 import Template

def get_jsonfile():
    with open('interfaces.json', 'r') as file:
        int = json.load(file)
    return int

def get_template():
    with open('interfaces_felipe.j2', 'r') as template:
        file = template.read()

    return file

def render_jinja(interface, template):
    int_template = Template(template)
    all_int = int_template.render(interfaces=interface)

    return all_int

def push_config(interfaces):
    with open('interfaces_felipe.txt', 'w') as file:
        file.write(interfaces)
         

if __name__ == "__main__":
    interfaces = get_jsonfile()
    template = get_template()
    all_int = render_jinja(interfaces, template)
    push_config(all_int)

   
    