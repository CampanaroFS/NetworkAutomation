import json

devices = {"R1": "192.168.1.10", 
           "R2": "192.168.1.20"}

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

def push_config(interface, ip):
    print("Seding command to" + ip)
    int_config = []
    for all_int in interface:
        int_config = render_config(all_int)
        print(int_config)
   

if __name__ == "__main__":
   data = open_file()
   push_config(data, devices["R1"])