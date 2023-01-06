import pytest
import json
from unittest.mock import patch
from app.ip_manager import Ip_Manager

def test_init():
    ip_manager_object = Ip_Manager()
    pass

def test_get_host_ip():
    host_ip = '1.1.1.1.1'

    ip_manager_object = Ip_Manager()
    ip_manager_object._host_ip = host_ip

    assert host_ip == ip_manager_object.get_host_ip()

@patch("pyshark.LiveCapture")
def test_sniff_ips(mock_live_capture):
    ip_manager_object = Ip_Manager()

    ip_manager_object._sniff_ips()

    pass

# @patch("requests.models.json")
# @patch("requests.get")
# def test_get_location(mock_request, mock_json):
#     ip_address = "1.1.1.1"
#     expected_location = {
#         "ip": "1.1.1.1",
#         "city": "city_01",
#         "region": "region_01",
#         "country": "country_01"
#     }
#     mock_json.return_value = json.dumps(expected_location, indent = 4)
#     ip_manager_object = Ip_Manager()

#     assert expected_location == ip_manager_object.get_location(ip_address)