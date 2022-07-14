import requests

def Resi(no_resi): 
    api_address='https://bot-kemenkes-dev.azurewebsites.net/api/checkairwaybillhc?airwaybill='
#   resi = input('masukan resi:')
    url = api_address + no_resi
    json_data = requests.get(url).json() 
    format_add = json_data['result']
    final = format_add['text'] 
    return final