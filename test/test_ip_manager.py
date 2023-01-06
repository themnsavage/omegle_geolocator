import pytest
import socket
from app.ip_manager import Ip_Manager

def test_init():
    ip_manager_object = Ip_Manager()
    pass

def test_get_host_ip():
    host_ip = '1.1.1.1.1'

    ip_manager_object = Ip_Manager()
    ip_manager_object._host_ip = host_ip

    assert host_ip == ip_manager_object.get_host_ip()