import json
from netmiko import ConnectHandler

devices = {
           'device_type': 'cisco_ios',
           'R1': '192.168.1.10', 
           'R2': '192.168.1.20',
           'username': 'cisco',
           'password': 'cisco',}

def open_file():
    with open("interfaces.json", "r") as data:
       json_dict = json.load(data)
       
    return json_dict

def render_config(interface):
    
        interface_template = f"""
        interface {interface["interface"]}
        description {interface["description"]}
        ip address {interface["ip_address"]} {interface["subnet_mask"]}
        speed {interface["speed"]}
        duplex {interface["duplex"]}
        port_status {interface["shut_down"]}"""

        return interface_template

def push_config(interface, hostname):
    print("Seding command to " + hostname + " (" + devices[hostname] + "):")
    int_config = []
    for all_int in interface:
        int_config = render_config(all_int)
        """with ConnectHandler(**device) as ssh:
            ssh.enable()
            send_command = ssh.send_config_set(int_config)
            print(send_command)"""
        print(int_config)        


def main():
    data = open_file()
    for hostname in devices.keys():
        push_config(data, hostname)


if __name__ == "__main__":
   main()
       