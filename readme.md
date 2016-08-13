# Ride Sharing Analyics

Analyze and compare ride sharing prices at given locations and times for surge between the two major ride sharing firms Uber and Lyft

## To do
1. Register apps to get client id and client secrets [- Done]
2. Authenticate apps to get access_tokens [- Done]
3. Prep data collection apis [- Done]
Three sources of data are to be used:

	a. uber: 

		- get the number of drivers nearby origin and destination
		- get the ride's cost and duration estimates 
		- get the surge rate if it exists

	b. lyft:

		- get the number of drivers nearby origin and destination
		- get the ride's cost and duration estimates 
		- get the surge rate if it exists

	c. yelp: Used to identify location neighbourhood

		- get places by categories (restaurants, school, hospital, church, finance services, ...)nearby location
		- Use classification model to identify the neighbourhood of the location
		
4. Prep the database: still need to choose between MongoDB and Sqlite
5. Collect data to the database
6. Analyze data
7. Build models:
	a. Neighbourhood classification
	b. Cost and surge estimation
8. Build front-end
