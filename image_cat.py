# BEACH
# FOREST
# MOUNTAIN
# RAINY
# OTHERS
import requests
api_key = 'acc_a4c207c8da68b75'
api_secret = '0f32606b462571f6e56ceb88a4eecbb7'

beach = ['beach','shore','sea','coast','body of water','waves','seaside','bay','marine','coastal']
mountain = ['mountain','mountains','glacier','peak','mount','climbing','summit','valley','everest','hike','trekking']
rainy = ['umbrella','rain','water']
forest = ['wild','savanna','safari','animal','animals','tree','wildlife','meadow','field','rural','farm','farming']

def image_category(image_url):
    response = requests.get(
        'https://api.imagga.com/v2/tags?image_url=%s' % image_url,
        auth=(api_key, api_secret))
    data =  response.json()['result']['tags']
    is_beach = False
    is_mountain = False
    is_forest = False
    is_rainy = False
    for d in data:
        dp = d['tag']['en']
        if is_beach==False and dp in beach:
            is_beach = True
        if is_mountain==False and dp in mountain:
            is_mountain = True
        if is_forest==False and dp in forest:
            is_forest = True
        if is_rainy==False and dp in rainy:
            is_rainy = True
    send_data = {
        'is_mountain':is_mountain,
        'is_beach':is_beach,
        'is_forest':is_forest,
        'is_rainy':is_rainy
    }
    return str(send_data)