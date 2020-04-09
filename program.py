import requests

# get api and urls
dark_api = "" # input your api key here
dark_url = "https://api.darksky.net/forecast/"
gmaps_api = "" # input your api key here
gmaps_url = "https://maps.googleapis.com/maps/api/geocode/json?address="

# ask user to input address
address_input = input("Enter address: ")
address_mod = address_input.replace(" ", "+")

# combine google maps url with address and api key
gmaps_full_url = gmaps_url + address_mod + "&key=" + gmaps_api

# get json data from url for geocoding
response = requests.get(gmaps_full_url)
json_data = response.json() # this is a dict data structure
json_list = json_data.get('results')

# get coordinates of the location
lat = json_list[0].get('geometry').get('location').get('lat')
long = json_list[0].get('geometry').get('location').get('lng')
coords = str(lat) + "," + str(long) # convert from float to string

# combine dark sky url with coords and api key
complete_url = dark_url + dark_api + "/" + coords

# get json data form url for weather information
response = requests.get(complete_url)
json_data = response.json()
curr = json_data['currently']
temp = str(curr['temperature'])

# print information!
print("The temperature of the coordinates you have inputted is " + temp)
