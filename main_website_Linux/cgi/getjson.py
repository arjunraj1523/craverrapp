#return JSON List
import json
import urllib, json
import htmlTop, htmlTail

def getJSON(foodItem,current_location_lat,current_location_lng):
	lis_latlong = []
	lis_name = []
	lis_distance = []
	lis_all = []
	lat = float(current_location_lat)
	lang = float(current_location_lng)	
	url = "https://api.foursquare.com/v2/venues/search?ll=%f,%f&limit=3&query=%s&radius=2000&oauth_token=QBYJF4RXJRYJNYEHWQDHAX54D04ORLKEVKPDTFTSYIUJZXPW&v=20150603" %(lat,lang,foodItem)
	response = urllib.urlopen(url);
	data1 = json.loads(response.read())	
	data2 = data1['response'] 
	number_data=len(data2['venues'])
	for x in range(0,number_data):
		name = data2['venues'][x]['name']
		lis_name +=[name] 
		distance = float(data2['venues'][x]['location']['distance'])/1000
		lis_distance +=[distance] 
		lis_latlong+=[data2['venues'][x]['location']['lat']]
		lis_latlong+=[data2['venues'][x]['location']['lng']]
	lis_all += [lis_name]+[lis_distance]+[lis_latlong]
	print('</ol>')
	return lis_name,lis_distance,lis_latlong

	
