import pandas as pd

class Lyftapp_credentials():
    def __init__(self):
        """
        This generate an object containing uber application credentials
        """
        credentials = pd.read_csv('Lyft/credentials.csv')
        self.client_id = credentials['CLIENT_ID'].values[0]
        self.server_token = credentials['SERVER_TOKEN'].values[0]
        self.client_secret = credentials['CLIENT_SECRET'].values[0]