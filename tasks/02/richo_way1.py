import json
from jinja2 import Template

def open_json_file():
    with open('interfaces.json', 'r') as f:
        data = json.load(f)
    return data

def open_template():
    with open('interfaces_richo.j2', 'r') as f:
        template = f.read()
    return template

def render_interface(interface_data, template):
    jinjaTemplate = Template(template)
    rendered_content = jinjaTemplate.render(interfaces=interface_data)
    return rendered_content

def write_to_file(text):
    with open("interfaces_richo.txt", "w") as f:
        f.write(text)

def main():
    data = open_json_file()
    template = open_template()
    all_interfaces_config =  render_interface(data, template)
    write_to_file(all_interfaces_config)

if __name__ == "__main__":
    main()