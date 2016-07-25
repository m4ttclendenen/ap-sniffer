from scapy.all import *
from access_point_detection_classes_module import *

def enable_monitor_mode(iface):
    subprocess.call('ifconfig ' + iface + ' down', shell=True)
    subprocess.call('iwconfig ' + iface + ' mode Monitor', shell=True)
    subprocess.call('ifconfig ' + iface + ' up', shell=True)

def enable_managed_mode(iface):
    subprocess.call('ifconfig ' + iface + ' down', shell=True)
    subprocess.call('iwconfig ' + iface + ' mode Managed', shell=True)
    subprocess.call('ifconfig ' + iface + ' up', shell=True)
    subprocess.call('nmcli d connect ' + iface, shell=True)







# def packet_handler(packet) :
#
#     if packet.haslayer(Dot11) :
#         if packet.subtype == 8 :
#             if packet.haslayer(Dot11Elt) :
#                 p = packet[Dot11Elt]
#                 while isinstance(p, Dot11Elt) :
#                     if p.ID == 1 :
#                         list_ascii = [ord(i) for i in p.info]
#                         print list_ascii
#                         s = "".join([chr(c) for c in list_ascii])
#                         print s
#                     p = p.payload

def main() :

    # enable_monitor_mode('wlan0')
    conf.iface = 'wlan0'
    # p = RadioTap()/Dot11(type=0,subtype=4,addr1='ff:ff:ff:ff:ff:ff',addr2 ='bc:77:37:ad:5c:a5',addr3='ff:ff:ff:ff:ff:ff')/Dot11ProbeReq()/Dot11Elt(ID=0,info='')/Dot11Elt(ID=1,info='\x02\x04\x0b\x16')/Dot11Elt(ID=3,info='\x02')/Dot11Elt(ID=50,info='\x0c\x12\x18\x24\x30\x48\x60\x6c')
    # sendp(p, iface = 'wlan0', count = 1, inter = .3)

    H = Handler()

    packet_capture = sniff(count = 50)

    H.process_packet_capture(packet_capture)

    for w in h.WAP_list :
        print w.bssid
        print w.essid
        print w.channel
        print '++++++++++++++++++++++++'




    # enable_managed_mode('wlan0')

if __name__ == "__main__" :
    main()
