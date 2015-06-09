#Return data from Form

import cgi

def getData_DiffFormat():
	formData = cgi.FieldStorage()
	firstName = formData.getvalue('food')
	lat = formData.getvalue('lat')
	lng = formData.getvalue('lng')
	resultSet = {'food':firstName,'latitude':lat,'longitude':lng}
	return resultSet