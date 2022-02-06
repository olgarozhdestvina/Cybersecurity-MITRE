# Performing reconnaissance by checking DNS
# Creating a list of subdomains. If subdomain exists,
# request its structure

import dns
import dns.resolver
import socket

def ReverseDNS(ip):
    try:
        result = socket.gethostbyaddr(ip)
    except:
        return []
    return [result[0]+result[1]]

def DNSrequest(domain):
    try: 
        result = dns.resolver.resolve(domain, 'A')
        if result: 
            print(domain)
            for answer in result:
                print(f'{answer}\nDomain Names: {ReverseDNS(answer.to_text())}')
    except (dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return 

def SubdomainSearch(domain, dictionary, nums):
    for word in dictionary:
        subdomain = word+'.'+domain
        DNSrequest(subdomain)
        if nums:
            for i in range(0,10):
                print(word+str(i)+'.'+domain)
                DNSrequest(word+str(i)+'.'+domain)

domain = 'google.com'
d = 'subdomains.txt'
dictionary = []

with open(d, 'r') as f:
    dictionary = f.read().splitlines()

SubdomainSearch(domain, dictionary, True)
