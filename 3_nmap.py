import nmap

scanner = nmap.PortScanner()

ip = "192.168.1.55"
scanner.scan(ip, '0-255', '-sV')

print("port", "name", "product", "version")
for port in scanner[ip]['tcp'].keys():
    name = scanner[ip]['tcp'][port]['name']
    product = scanner[ip]['tcp'][port]['product']
    version = scanner[ip]['tcp'][port]['version']
    
    print(port, "|", name, "|", product, "|", version)




