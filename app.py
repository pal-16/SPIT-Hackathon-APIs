import requests
res = requests.get('http://d4fc5ecf0ad9.ngrok.io/api/notify')
file = open('data.txt','a')
file.write('Done\n')
file.close()
