import requests as re
import io
from PIL import Image
from skimage import io
import cv2
import json

API_KEY = 'AIzaSyDKqSLy4MMxiNwEXSPqpomf7m94-pSTzk4'
LATLON = '1.49,103.39'
RADIUS = 22500 # Benut - Ayer Baloi - Pontian Kecil - Kukup
TYPE = 'pharmacy'
KEYWORD = ""
filename = f'./data/{TYPE}.txt'

def getPlaceDetails(r):
	places = []
	# name, business_status, price_level, type, rating, formatted_address, formatted_phone_number, opening_hours/weekday_text, website
	for place in r['results']:
		PLACE_ID = place['place_id']
		PLACE_DETAIL_URL = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={PLACE_ID}&fields=name,business_status,type,price_level,rating,formatted_address,formatted_phone_number,opening_hours/weekday_text,website&key={API_KEY}'
		r = re.get(PLACE_DETAIL_URL).json()
		places.append(r['result'])


	with open(filename, 'w') as f:
		json.dump(places, f, indent=2)

URL = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={LATLON}&radius={RADIUS}&type={TYPE}&keyword={KEYWORD}&key={API_KEY}"
# print(URL)
r = re.get(URL).json()

# for place in r['results']:
# 	print(place['name'])

getPlaceDetails(r)




# def getPhotos(r):
	# photoRef = r['results'][0]['photos'][0]['photo_reference']
	# maxWidth = r['results'][0]['photos'][0]['width']
	# URL = f'https://maps.googleapis.com/maps/api/place/photo?maxwidth={maxWidth}&photoreference={photoRef}&key={API_KEY}'
	# r = re.get(URL).url # will get image url
	# print(r)

	# image = io.imread(r)
	# cv2.imshow('im', cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
	# cv2.waitKey(0)



# def goNext(r):
	# if r['next_page_token']:
	# 	TOKEN = r['next_page_token']
	# 	# print(TOKEN)

	# try:
	# 	while True:
	# 		URL = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken={TOKEN}&key=AIzaSyDKqSLy4MMxiNwEXSPqpomf7m94-pSTzk4"
	# 		r = re.get(URL).json()

	# 		if r['next_page_token']:
	# 			TOKEN = r['next_page_token'] 
	# 			print(TOKEN)

	# 		else:
	# 			break


	# 		for place in r['results']:
	# 			print(place['name'])
	# except:
	# 	print('No pagetoken')