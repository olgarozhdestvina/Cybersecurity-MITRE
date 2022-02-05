from scapy.all import *

packet = rdpcap('http.cap')
# packet[0].show()
p = packet[3]

# Changing a port for TCP
p[TCP].dport = 8080

# Wrap IP packet in TCP (defaults)
p = IP()/TCP()

# The same but with parameters
p = IP(dst='8.8.8.8')/TCP(dport=53)
p.show()