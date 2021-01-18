import shodan
import requests

api = "8uSQFKS27GkGch2GLtmeh00477nWuYx6"
search = "ssh"
port = 22
country = "RU"

try:
	for x in range(200):
		page = str(x)
		url = 'https://api.shodan.io/shodan/host/search?key=' + api + '&query=' + search + '+port%3A"' + str(port) + '"' + '+country%3A"' + country + '"' +'%20&page=' + page
		content = requests.get(url)
		print "%s" % content.text
except:
	print("An exception occurred")
