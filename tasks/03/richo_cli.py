import typer
from jinja2 import Template

app = typer.Typer()


def open_template():
    with open('interfaces_richo.j2', 'r') as f:
        template = f.read()
    return template


def render_interface(interface_data, template):
    jinjaTemplate = Template(template)
    rendered_content = jinjaTemplate.render(interface=interface_data)
    return rendered_content


@app.command()
def goodbye(int: str, desc: str, ip: str, prefix: str, speed: int = 1000, duplex: str = "full", enabled: bool = True):
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
    typer.echo(all_interfaces_config)


if __name__ == "__main__":
    app()
