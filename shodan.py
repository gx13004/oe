import shodan
import requests

api = "8uSQFKS27GkGch2GLtmeh00477nWuYx6"
search = "telnet"

try:
	for x in range(10000):
		page = str(x)
		content = requests.get('https://api.shodan.io/shodan/host/search?key=' + api + '&query=' + search +'%20&page=' + page)
		print "%s" % content.text
except:
	print("An exception occurred")
