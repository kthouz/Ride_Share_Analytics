from uberpy import Uber
from uberapp_credentials import Uberapp_credentials
from lyftapp_credentials import Lyftapp_credentials


from geopy.geocoders import Nominatim
import requests, json

class UberObj():
    """
    generate uber service object around a location given its geo-coordinates
    """
    def __init__(self):
        # load credentials
        credentials = Uberapp_credentials()
        # create uber instance
        self.uber = Uber(credentials.cliend_id,credentials.server_token,credentials.client_secret)
        pass
    
    def get_products(self,lat,lon):
        """
        get uber products around a given location
        """
        products = self.uber.get_products(lat,lon)['products']
        return products
    
    def get_ride_cost(self,st_lat,st_lon,en_lat,en_lon):
        """
        get price estimate for
        st_lat: float, starting position latitude
        st_lon: float, starting position longitude
        en_lat: float, ending position latitude
        en_lon: float, ending position longitude
        """
        # request price estimates
        prices = self.uber.get_price_estimate(st_lat,st_lon,en_lat,en_lon)['prices']
        return prices

class LyftObj():
    """
    generate lyft service object
    """
    def __init__(self):
        """
        initialize connection to the api url and get access token
        """
        # load credentials from file
        credentials = Lyftapp_credentials()
        self.client_id = credentials.client_id
        self.client_secret = credentials.client_secret
        
        # obtain access token
        self.token = self.__generate_token__()
        
        # define variables to be used in the request parameters
        token_val = 'Bearer '+self.token
        self.headers = {'Authorization':token_val}
        
    def __generate_token__(self):
        """
        use client_id and client_secret to generate access token. 
        The generated access code will only last for 24 hours
        """
        url = 'https://api.lyft.com/oauth/token'
        
        # define request parameters
        payload = {"Content-Type": "application/json",
                   "grant_type": "client_credentials", 
                   "scope": "public"}
        # request data
        res = requests.post(url, 
                            data = payload,
                            auth = (self.client_id, self.client_secret))
        
        # extract the token from the response
        token = res.json()['access_token']
        return token

    def get_nearby_drivers(self,lat,lon):
        """
        get drivers nearby a given location
        lat: float, latitude
        lon: float, longitude
        """
        url = 'https://api.lyft.com/v1/drivers?lat='+str(lat)+'&lng='+str(lon)
        nearby_drivers = requests.get(url,headers=self.headers).json()['nearby_drivers']
        return nearby_drivers
    
    def get_ride_types(self,lat,lon):
        """
        get lyft products around a given location
        lat: float, latitude
        lon: float, longitude
        """
        url = 'https://api.lyft.com/v1/ridetypes?lat='+str(lat)+'&lng='+str(lon)
        ride_types = requests.get(url,headers=self.headers).json()['ride_types']
        return ride_types
    
    def get_ride_cost(self,st_lat,st_lon,en_lat,en_lon):
        """
        get cost estimates of a ride given starting and ending coordinates
        lat: float, latitude
        lon: float, longitude
        """
        url = 'https://api.lyft.com/v1/cost?start_lat='+str(st_lat)+'&start_lng='+str(st_lon)+'&end_lat='+str(en_lat)+'&end_lng='+str(en_lon)
        ride_cost = requests.get(url,headers=self.headers).json()['cost_estimates']
        return ride_cost
    
    def get_eta(self,lat,lon):
        """
        get the estimate time of arrival with respect to a given location
        lat: float, latitude
        lon: float, longitude
        """
        url = 'https://api.lyft.com/v1/eta?lat='+str(lat)+'&lng='+str(lon)
        eta = requests.get(url,headers=self.headers).json()['eta_estimates']
        return eta

class geoObj():
    """
    generate the geographic object
    """
    def __init__(self,street_address):
        """
        initialize an location object
        street_address: str
        """
        self.st_address = street_address
        self.geolocator = Nominatim()
        self.location = self.__get_location__()
        self.raw_data = self.__get_raw_data__()
    
    def __get_location__(self):
        return self.geolocator.geocode(self.st_address)
    
    def __get_raw_data__(self):
        """return raw data of the initiated location"""
        keys = ['lat','lon','class','type','display_name']
        raw= {}
        for k in keys:
            raw[k] = self.location.raw[k]
        return raw
    
    def get_lat_lon(self):
        """return latitude and longitude of the initiated location"""
        return [self.location.latitude,self.location.longitude]
    
    
