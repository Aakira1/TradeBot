import json
import hmac
import hashlib
import requests
import time


class Profile:
    def __init__() -> "Profile":
        Profile.currency = ""
        Profile.start_ts = 0.00
        Profile.end_ts = 0.00
        Profile.page_size = 0
        Profile.page = 0
        Profile.status = ""
        Profile.private_endpoints = ""
    
    def set_cancel_disconnection():
        return



if __name__ == "__main__":
    #connect Json File
    with open("keys.json") as file:
        calls = json.load(file)
    
    API_URL = calls['API_URL']
    priv_endpoints = ["private"]