#!C:/Python/python.exe

import cgi
import getData
import getjson
import htmlTop
import htmlTail
import map_template
import printList
import getIp
import getLocation
#main Program
        
if __name__== "__main__":
	try:
		htmlTop.htmlTop()
		result=getData.getData_DiffFormat()		
		#current_location=getLocation.getLocation(getIp.getIP())
		result_LatLong=getjson.getJSON(result['food'],result['latitude'],result['longitude'])
		print("""
			<script>
			function goBack(){
				window.history.back();
			}
			</script>
			<style>
				#responceMessage{
					text-align:center;
				}
			</style>
		""")
		print("<button class='btn btn-danger btn-lg' onclick='goBack()' style='margin: -70px 15px;;width: 5%;height: 45px;border-radius: 23px; padding:10px;}'><span class='glyphicon glyphicon-hand-left' aria-hidden='true'></span></button>")
		map_template.map_template(result_LatLong,result['latitude'],result['longitude'])
		printList.printList(result_LatLong)
		#print("<h3 id='responceMessage' class='alert alert-success'>OoPs! I guess these are the only places that serve %s in your area</h2>")%result['food']
		htmlTail.htmlTail()
	except:
		print("</li>")
		htmlTail.htmlTail()
		print("<h3 id='responceMessage' class='alert alert-danger'>oh Snap! I guess something went wrong, Try Again Later! Sorry :)</h2>")
		#cgi.print_exception()
