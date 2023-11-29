from scapy.layers.l2 import *
from scapy.all import *

eth = Ether()
arp = ARP()

eth.dst="ff:ff:ff:ff:ff:ff"
arp.pdst = "192.168.1.1/24"

bcPckt = eth/arp
bcPckt.show()

ans, unans = srp(bcPckt, timeout=5)

# ans.summary()
print("#"*30)
# unans.summary()

for snd, rcv in ans:
    print(rcv.psrc, " : ", rcv.src)