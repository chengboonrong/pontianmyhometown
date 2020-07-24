import json
import requests as re
import cv2
import skimage.io
import os

def get(name, photoRef, i):
	maxHeight = 484 #r['result']['photos'][0]['height']
	URL = f'https://maps.googleapis.com/maps/api/place/photo?maxheight={maxHeight}&photoreference={photoRef}&key={API_KEY}'
	result = re.get(URL).url # will get image url
	image = skimage.io.imread(result)
	image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
	image_name = f'./static/image/{CITY}/{TYPE}/' + "".join(name.split(" ")) + f'-{i}.jpg'
	cv2.imwrite(image_name, image_rgb)
	return image_name[1:]

API_KEY = 'AIzaSyDKqSLy4MMxiNwEXSPqpomf7m94-pSTzk4'
CITY = 'pekannanas'
TYPE = 'atm'

if not os.path.isdir(f'./static/image/{CITY}/{TYPE}'):
	os.mkdir(f'./static/image/{CITY}/{TYPE}')

with open(f'./data/{CITY}/{CITY}_{TYPE}.json', 'r') as file_:
	data = json.load(file_)
	places = [d for d in data]
	# print(len(places))
    
for p in places:
	print(f"{p['name']}: ")
	try: 
		photos = [photo for photo in p['photos']]
		for i, photo in enumerate(photos):
			print(i, photo['photo_reference'])
			p['photo'] = get(p['name'], photo['photo_reference'], i)
	
	except:
		p['photo'] = '#'
		# print('No Photo for this Place')
  

with open(f'./data/{CITY}/{CITY}_{TYPE}.json', 'w') as file_:
	json.dump(places, file_, indent=2)