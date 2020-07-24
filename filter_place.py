import json

CITY = 'pekannanas'
TYPE = 'bank'
KEYWORD = 'food'

with open(f'./data/{CITY}/{CITY}_{TYPE}.json', 'r') as file_:
	data = json.load(file_)
	places = [d for d in data['results']]
	namelist = [d['name'] for d in places]
 
print(len(places))

try:
	with open(f'./data/{CITY}/{CITY}_{TYPE}_{KEYWORD}.json', 'r') as file_:
		data = json.load(file_)
		key_places = [d for d in data['results']]

	for kp in key_places:
		if kp['name'] not in namelist:
			print(kp['name'])
			places.append(kp)
			
	print(len(places))
 
except:
    print('Continue ..')

finally:
	with open(f'./data/{CITY}/{CITY}_{TYPE}.json', 'w') as file_:
		json.dump(places, file_, indent=2)