import requests

f = open('ip.txt','r')
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0',
}
try:
	while 1:
		ip = f.readline()
		content = requests.get('https://ipinfo.io/' + ip, headers=headers)
		output = content.text.encode('utf-8')
		print(output)
	f.close
except:
	print("an error occured")