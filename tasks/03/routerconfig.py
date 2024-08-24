import typer
from jinja2 import Template
import paramiko as p

app = typer.Typer()

def connect_to_router(ip, username, password):
    ssh_client = p.SSHClient()
    ssh_client.set_missing_host_key_policy(p.AutoAddPolicy())
    ssh_client.connect(ip, username=username, password=password)
    return ssh_client

def open_template():
    with open('interfaces_richo.j2', 'r') as f:
        template = f.read()
    return template


def render_interface(interface_data, template):
    jinjaTemplate = Template(template)
    rendered_content = jinjaTemplate.render(interface=interface_data)
    return rendered_content

def configure_router(ssh_client, cmd, int_config):
    ssh_client.send(cmd + "\n")
    for int_config in int_config:
        ssh_client.send(int_config + "\n")
        ssh_client.sleep(1)
    ssh_client.close()

@app.command()
def config_router_cli(int: str, desc: str, ip: str, prefix: str, speed: int = 1000, duplex: str = "full", enabled: bool = True):
    interface = {
        "interface": int,
        "description": desc,
        "ip_address": ip,
        "subnet_mask": prefix,
        "enabled": enabled,
        "speed": speed,
        "duplex": duplex
    }
    template = open_template()
    all_interfaces_config = render_interface(interface, template)
    try:
        ssh_client = connect_to_router("192.168.1.150", "cisco", "cisco") 
        typer.echo("Connected to the router.")
        configure_router(ssh_client, cmd="conf t", int=all_interfaces_config)
        type.echo("Configuration applied successfully.")
    except Exception as e:
        typer.echo(f"Error: {e}")


if __name__ == "__main__":
    app()
