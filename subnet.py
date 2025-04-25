import ipaddress

def subnet_info(ip, subnet):
    network = ipaddress.IPv4Network(f"{ip}/{subnet}", strict=False)
    print("Network Address:", network.network_address)
    print("Broadcast Address:", network.broadcast_address)
    print("Subnet Mask:", network.netmask)
    print("No. of Hosts:", network.num_addresses - 2)

subnet_info("192.168.1.10", 24)