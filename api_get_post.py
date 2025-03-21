import json
import requests

def Api_Get(adres):
    try:
        response = requests.get(adres)
        if response.status_code == requests.codes.ok:
            print(response.text)
            return response
        
        else:
            return response
    except Exception as ex:
        print(ex)
        return None


def Api_Post(adres, model):
    try:
        json_data = json.dumps(model)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post(adres, data=json_data, headers=headers)
        
        if response.status_code == requests.codes.ok:
            return response
        else:
            return response
    except Exception as ex:
        print(ex)
        return None

client = requests.Session()
 