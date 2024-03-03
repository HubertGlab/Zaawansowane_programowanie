import requests
import argparse


def get_breweries(city=None):
    url = 'https://api.openbrewerydb.org/v1/breweries?page=1&per_page=20'
    if city:
        url = f'https://api.openbrewerydb.org/v1/breweries?by_city={city}&page=1&per_page=20'
    r = requests.get(url)
    data = r.json()
    lista = []
    for value in data:
        obj = Brewery(value)
        lista.append(obj)
    return lista


def print_breweries():
    parser = argparse.ArgumentParser()
    parser.add_argument("--city")
    args = parser.parse_args()
    breweries = get_breweries(args.city)
    for index, value in enumerate(breweries, start=1):
        print(f'Brewery {index} {value}')


class Brewery:
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.brewery_type = data.get('brewery_type')
        self.address_1 = data.get('address_1')
        self.address_2 = data.get('address_2')
        self.address_3 = data.get('address_3')
        self.city = data.get('city')
        self.state_province = data.get('state_province')
        self.postal_code = data.get('postal_code')
        self.country = data.get('country')
        self.longitude = data.get('longitude')
        self.latitude = data.get('latitude')
        self.phone = data.get('phone')
        self.website_url = data.get('website_url')
        self.state = data.get('state')
        self.street = data.get('street')

    def __str__(self):
        return (
            f'\nID: {self.id}\nName: {self.name}\nbrewery_type: {self.brewery_type}\naddress_1: {self.address_1}'
            f'\naddress_2: {self.address_2}\naddress_3: {self.address_3}\ncity: {self.city}'
            f'\nstate_province: {self.state_province}\npostal_code: {self.postal_code}\ncountry:{self.country}'
            f'\nlongitude: {self.longitude}\nlatitude: {self.latitude}\nphone: {self.phone}'
            f'\nwebsite_url: {self.website_url}\nstate: {self.state}\nstreet: {self.street}'
            f'\n')
