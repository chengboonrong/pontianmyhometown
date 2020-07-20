import pandas as pd
import requests as re
import numpy as np

# set years and months here
years = [str(i) for i  in range(2020, 2021)] # Early 2010- End 2019

months = [ 
    '-01-01', 
    '-02-01', 
    '-03-01', 
    '-04-01',
    '-05-01',
    '-06-01',
    '-07-01',
    # '-08-01',
    # '-09-01',
    # '-10-01',
    # '-11-01',
    # '-12-01'
]

def createDataset(date, enddate, placeName):
    response = re.get('http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=fdb755ec2cd84e498f283433200807&q={}&format=json&date={}&enddate={}'.format(placeName, date, enddate)).json()['data']
    narray = []
   
    for j, each in enumerate(response['weather']):   
        date = each['date']
        windspeedKmph = 0
        precipMM = 0
        humidity = 0
        visibility = 0
        pressure = 0 
        cloudcover = 0
        
        for i in each['hourly']:
            
            windspeedKmph += int(i['windspeedKmph'])
            precipMM += float(i['precipMM'])
            humidity += int(i['humidity'])
            visibility += int(i['visibility'])            
            pressure += int(i['pressure'])    
            cloudcover += int(i['cloudcover'])   
            
        windspeedKmph = round(windspeedKmph/8, 2)
        humidity = round(humidity/8, 2)
        visibility = round(visibility/8, 2)
        pressure = round(pressure/8, 2)
        cloudcover = round(cloudcover/8, 1)
        
        narray.append(list([date, each['avgtempC'], humidity, windspeedKmph, precipMM, visibility, pressure, cloudcover]))
        
    df = pd.DataFrame(np.array(narray), columns=['date', 'avgtempC','humidity','windspeedKmph','precipMM','visibility','pressure','cloudcover'])
    
    return df

# change location/area here for the dateset
### Klang Valley - KL, PJ, SB, Klang, Puchong

placeName = 'Pontian'
df = pd.DataFrame()

for i in range(len(years)):
    for j in range(len(months)-1):
        df = df.append(createDataset(years[i]+months[j], years[i]+months[j+1], placeName))
    
        print('Month {}: done'.format(j+1))
    
    df = df.append(createDataset(years[i]+months[j+1], years[i]+months[j+1], placeName))
    print('Year {} : done'.format(years[i]))
    
df.to_csv('{}-1.csv'.format(placeName), index=False)