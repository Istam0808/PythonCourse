import json

import requests  # to install: pip install requests


def find_person_by_ip(ip_address):
    url = "http://ip-api.com/json/"
    response = requests.get(url, ip_address)
    data = json.loads(response.content)
    return data


# type ipconfig in cmd
my_ip_address = "192.168.0.111"

geolocation_data = find_person_by_ip(my_ip_address)
print(geolocation_data)
