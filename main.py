import requests
import datetime

USERNAME = ''
TOKEN = ''
GRAPHID = ''

header = {
    'X-USER-TOKEN' : TOKEN
}

url_endpoint = 'https://pixe.la/v1/users'
graphcreate_url_endpoint = f"{url_endpoint}/{USERNAME}/graphs"

def create_user():
    user_params = {
        'token' : TOKEN,
        'username' : USERNAME,
        'agreeTermsOfService' : 'yes', 
        'notMinor' : 'yes'
    }
    response = requests.post(url=url_endpoint, json=user_params)
    print(response.text)
    
def create_graph():
    graph_config = {
        'id' : GRAPHID,
        'name' : 'Treadmill Walking',
        'unit' : 'Minutes',
        'type' : 'float',
        'color' : 'sora'
    }
    response = requests.post(url=graphcreate_url_endpoint, json=graph_config, headers=header)
    print(response.text)
    
def create_pixel(day, month, year, quantity):
    updated_date = datetime.datetime(year=year, month=month, day=day).strftime('%Y%m%d')
    pixel_data = {
        'date' : updated_date,
        'quantity' : quantity,   
    }
    
    url = f"{graphcreate_url_endpoint}/{GRAPHID}"
    response = requests.post(url=url, json=pixel_data, headers=header)
    print(response.text)

def update_pixel(day, month, year, quantity):
    updated_date = datetime.datetime(year=year, month=month, day=day).strftime('%Y%m%d')
    pixel_data = {
        'quantity' : quantity,   
    }
    
    url = f"{graphcreate_url_endpoint}/{GRAPHID}/{updated_date}"
    response = requests.put(url=url, json=pixel_data, headers=header)
    print(response.text)

def delete_pixel(day, month, year):
    updated_date = datetime.datetime(year=year, month=month, day=day).strftime('%Y%m%d')
    
    url = f"{graphcreate_url_endpoint}/{GRAPHID}/{updated_date}"
    response = requests.put(url=url, headers=header)
    print(response.text)