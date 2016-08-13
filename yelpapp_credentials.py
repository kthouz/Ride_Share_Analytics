import pandas as pd
class Yelpapp_credentials():
	def __init__(self):
		credentials = pd.read_csv('Yelp/credentials.csv')
		self.consumer_key = credentials.consumer_key[0]
		self.consumer_secret = credentials.consumer_secret[0]
		self.access_token = credentials.token[0]
		self.access_token_secret = credentials.token_secret[0]