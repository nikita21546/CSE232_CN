import matplotlib.pyplot as plt
from scapy.all import *

def cwnd_calc(time_stamp, s_no):
    cwnd_win = [float('nan')]
    for i in range(1, len(s_no)):
        cwnd = (s_no[i] - s_no[i-1]) / (time_stamp[i] - time_stamp[i-1]) if (time_stamp[i] - time_stamp[i-1]) > 0 else float('nan')
        cwnd_win.append(cwnd)
    return cwnd_win

def time_seq(pcap_file):
    s_no = []
    time_stamp = []
    packets = rdpcap(pcap_file)
    for packet in packets:
        if 'TCP' in packet and 'IP' in packet:
            s_no.append(packet[TCP].seq)
            time_stamp.append(packet.time)
    return time_stamp, s_no

    
pcap_file = 'filename.pcap' 
time, s_no = time_seq(pcap_file)
cwnd = cwnd_calc(time, s_no)
plt.plot(time, cwnd)
plt.xlabel('Time (seconds)')
plt.ylabel('Congestion Window Size')
plt.title('CWND over time')
plt.show()
