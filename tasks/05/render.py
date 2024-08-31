import yaml
from rich import print
from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader, StrictUndefined

def open_yaml_file():
    with open('variables.yml', 'r') as f:
        data = yaml.safe_load(f)

    return data

def render(variables):
    environment = Environment(
        loader=FileSystemLoader('.'),
        trim_blocks=True,
        lstrip_blocks=True,
        undefined=StrictUndefined
    )
    template = environment.get_template('site1.j2')
    rendered_content = template.render(variables=variables)
    return rendered_content

def write_to_file(text, filename):
    with open(f"{filename}.txt", 'w') as f:
        f.write(text)

def send_ssh_commands(commands):
    device = {
        'device_type': 'cisco_ios',
        'host': '172.31.1.110',
        'username': 'admin',
        'password': 'cisco'
    }
    connection = ConnectHandler(**device)
    output = connection.send_command(commands)
    print(output)


def main():
    data = open_yaml_file()
    print(data)
    for router in data:
        print(f"Configuring {router['hostname']}")
        all_interfaces_config =  render(router)
        write_to_file(all_interfaces_config, router['hostname'])
        # send_ssh_commands(all_interfaces_config)

if __name__ == "__main__":
    main()