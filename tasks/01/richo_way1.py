import json

def open_json_file():
    with open('interfaces.json', 'r') as f:
        data = json.load(f)
    return data

def render_interface(interface_data):

    interface_template = f"""
interface {interface_data["interface"]}
  description {interface_data["description"]}
  ip address {interface_data["ip_address"]} {interface_data["subnet_mask"]}
  speed {interface_data["speed"]}
  duplex {interface_data["duplex"]}
  {interface_data["shut_down"]}"""
    
    return interface_template

def write_to_file(text):
    with open("interfaces_richo.txt", "w") as f:
        f.write(text)

def main():
    data = open_json_file()
    all_interfaces_config =  str()
    for interface in data:
        all_interfaces_config += render_interface(interface)
        all_interfaces_config += "\n!"

    write_to_file(all_interfaces_config)

if __name__ == "__main__":
    main()