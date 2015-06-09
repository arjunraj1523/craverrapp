import urllib
import json
def getLocation(ip_addr):
	url = 'http://freegeoip.net/json/%s'%str(ip_addr)
	f = urllib.urlopen(url)
	json_string = f.read()
	location = json.loads(json_string)
	current_longitude = location['longitude']
	current_latitude = location['latitude']
	return current_longitude,current_latitude
