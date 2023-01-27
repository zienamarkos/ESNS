from scapy.all import *
x_ip = "10.0.2.11" # X-Terminal
x_port = 514 # Port number used by X-Terminal
srv_ip = "10.0.2.12" # The trusted server
srv_port = 1023 # Port number used by the trusted server

# Add 1 to the sequence number used in the spoofed SYN
seq_num = 0x1000 + 1

def spoof(pkt):
global seq_num # We will update this global variable in the function
old_ip = pkt[IP]
old_tcp = pkt[TCP]

# Print out debugging information
tcp_len = old_ip.len - old_ip.ihl*4 - old_tcp.dataofs*4 # TCP data length
print("{}:{} -> {}:{} Flags={} Len={}".format(old_ip.src, old_tcp.sport,
old_ip.dst, old_tcp.dport, old_tcp.flags, tcp_len))

# Construct the IP header of the response
ip = IP(src=srv_ip, dst=x_ip)

# Check whether it is a SYN+ACK packet or not;
# if it is, spoof an ACK packet
# ... Add code here ...
myFilter = ’tcp’ # You need to make the filter more specific
sniff(filter=myFilter, prn=spoof)