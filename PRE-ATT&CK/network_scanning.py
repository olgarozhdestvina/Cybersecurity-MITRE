from scapy.all import *

ports = [25, 50, 80, 443, 445, 8080, 8443]
host = '8.8.8.8'

def SynScan(host):
    ans, _ = sr(IP(dst=host)/TCP(sport=5555,dport=ports, flags='S'), timeout=2,verbose=0)
    print(f'Open ports at {host}:')
    print([s[TCP].dport for s,r in ans if s[TCP].dport == r[TCP].sport])

def DNSScan(host):
    ans, _ = sr(IP(dst=host)/UDP(sport=555,dport=53)/DNS(rd=1,qd=DNSQR(qname='google.com')), timeout=2, verbose=0)
    if ans:
        print(f'DNS Server at {host}')

SynScan(host)
DNSScan(host)