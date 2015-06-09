#!/usr/bin/python
import cgi
import getData
import getjson
import htmlTop
import htmlTail


def getChoice():
    print("""
            <style>
            #buttonSubmit{
                margin:10px;
            }
            #choiceForm{
                text-align:center;
            }
            #caption{
                text-align:center;
            }
            @media screen and (min-width: 375px) and (max-width:450px){
           #choiceForm {
                text-align: center;
                display: table-caption;
                margin: 0px 10px 10px 300px;
            }
            #caption {
                text-align:left;
                font-size: 21px;
                margin-left: 200px;
            }
            }
            </style>
    """)
    print(""" 	

                <form method="POST" action="processname.cgi" id="choiceForm">
                    <input type="hidden" id="lat" name="lat" class="lat">
                    <input type="hidden" id="lng" name="lng" class="lng">
                    <input class="btn btn-info btn-lg" type="submit" id="buttonSubmit" name="food" class="buttonSubmit" value="Pizza"/>
                    <input class="btn btn-info btn-lg" type="submit" id="buttonSubmit" name="food" class="buttonSubmit" value="Burger"/>
                    <input class="btn btn-info btn-lg" type="submit" id="buttonSubmit" name="food" class="buttonSubmit" value="Ice Cream"/>
                    <input class="btn btn-info btn-lg" type="submit" id="buttonSubmit" name="food" class="buttonSubmit" value="Chocolate"/>
                    <input class="btn btn-info btn-lg" type="submit" id="buttonSubmit" name="food" class="buttonSubmit" value="Cake"/>
                    <input class="btn btn-info btn-lg" type="submit" id="buttonSubmit" name="food" class="buttonSubmit" value="Chicken Tikka"/>
                    <input class="btn btn-info btn-lg" type="submit" id="buttonSubmit" name="food" class="buttonSubmit" value="Sandwich"/>
                    <input class="btn btn-info btn-lg" type="submit" id="buttonSubmit" name="food" class="buttonSubmit" value="Vada Pav"/>
                    <input class="btn btn-info btn-lg" type="submit" id="buttonSubmit" name="food" class="buttonSubmit" value="Pani Puri"/>
                    <input class="btn btn-info btn-lg" type="submit" id="buttonSubmit" name="food" class="buttonSubmit" value="Juice"/>
                    <input class="btn btn-info btn-lg" type="submit" id="buttonSubmit" name="food" class="buttonSubmit" value="Chinese Cuisine"/>
            </form>
<script src='http://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js'></script>
<script>
$(document).ready(getLocation())
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
        alert("Geolocation is not supported by this browser.");
    }
}
function showPosition(position) {
    document.getElementById("lng").value=position.coords.longitude;
    document.getElementById("lat").value=position.coords.latitude;
}
</script>
		  """)



#main Program
if __name__== "__main__":
    try:
        htmlTop.htmlTop()
        print("<h2 id='caption'>What are you CRAVERRing?</h2>")
        result = getChoice()
        htmlTail.htmlTail()
    except:
        print("</li>")
        htmlTail.htmlTail()
        print("<h3 id='responceMessage' class='alert alert-danger'>oh Snap! I guess something went wrong, Try Again Later! Sorry :)</h2>")
