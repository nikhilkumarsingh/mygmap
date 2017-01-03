'''
This is the main script of our python package
'''
# importing the requests library
import requests
 
# api-endpoint
URL = "http://maps.googleapis.com/maps/api/geocode/json"
 

# function to get formatted address of passed location
def get_address(location):
	# defining a params dict for the parameters to be sent to the API
	PARAMS = {'address':location}
	 
	# sending get request and saving the response as response object
	r = requests.get(url = URL, params = PARAMS)
	 
	# extracting data in json format
	data = r.json()
	 
	 
	# extracting formatted address 
	# of the first matching location
	formatted_address = data['results'][0]['formatted_address']
	 
	# returning the output
	return(formatted_address)

# function to get latitude-longitude of passed location
def get_coordinates(location):
	# defining a params dict for the parameters to be sent to the API
	PARAMS = {'address':location}
	 
	# sending get request and saving the response as response object
	r = requests.get(url = URL, params = PARAMS)
	 
	# extracting data in json format
	data = r.json()
	 
	 
	# extracting latitude, longitude
	# of the first matching location
	latitude = data['results'][0]['geometry']['location']['lat']
	longitude = data['results'][0]['geometry']['location']['lng']
	 
	# returning the output
	return(latitude, longitude)


