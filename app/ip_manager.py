import socket
import requests
import pyshark

class Ip_Manager:
    def __init__(self):
        hostname = socket.gethostname()
        self._host_ip = socket.gethostbyname(hostname)
    
    def start(self):
        while(True):
            list_of_ips = self._sniff_ips()
            for ip in list_of_ips:
                print(self._get_location(ip))
    
    def get_host_ip(self):
        return self._host_ip

    def _sniff_ips(self, interface_type = 'wlp3s0'):
        ips = []
        capture = pyshark.LiveCapture(interface= interface_type, bpf_filter= 'udp')

        for packet in capture.sniff_continuously(packet_count=5):
            if packet.ip.dst not in ips and packet.ip.dst != self._host_ip:
                ips.append(packet.ip.dst)

        return ips

    def _get_location(self, ip_address):
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        location_data = {
            "ip": ip_address,
            "city": response.get("city"),
            "region": response.get("region"),
            "country": response.get("country_name")
        }
        return location_data