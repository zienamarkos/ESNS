from scapy.all import *


ip=IP(src="10.0.2.12", dst="10.0.2.11")
tcp=TCP(sport=9090, dport=514, flags="SA", Seq=3920611527)


pkt=ip/tcp
ls(pkt)
send(pkt,verbose=0)