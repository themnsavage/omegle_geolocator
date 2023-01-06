import socket

class Ip_Manager:
    def __init__(self):
        hostname = socket.gethostname()
        self._host_ip = socket.gethostbyname(hostname)
        
    
    def get_host_ip(self):
        return self._host_ip