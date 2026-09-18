import requests, json
from pprint import pprint
from src.data import Data

def request_url(IP: str, plugin:str) -> str:
    url = f"http://{IP}:61208/api/4/{plugin}"
    response = requests.get(url)
    return response.json()

def request_url_value(IP: str, plugin:str) -> str:
    url = f"http://{IP}:61208/api/4/{plugin}"
    response = requests.get(url)
    return json.loads(response.text)

def main():
    print("Hello from restapi-py!")
    hosts = ["192.168.1.42", "192.168.1.65", "192.168.1.139", "192.168.1.19", "192.168.1.106", "192.168.1.247"]
    plugins = ["cpu", "system", "sensors", "load", "mem", "network", "uptime"]
    data = ["system/hostname", "cpu/total", "mem/percent", "sensors/value"]

    request_data = []
    for host in hosts[:]:
        print(f"---------{host}---------")
        try:
            print(f"{request_url(host, "status")}")
        except requests.exceptions.ConnectionError:
            print(f"not available")
            print()
            continue
        temp_data = []
        for plugin in data:
            dictonary = request_url_value(host, plugin)
            temp_data.append(dictonary[plugin.split("/")[1]])

        request_data.append(Data(temp_data[0], temp_data[1], temp_data[2], temp_data[3][0]))
        print()

    for data in request_data:
        print(data)

if __name__ == "__main__":
    main()
