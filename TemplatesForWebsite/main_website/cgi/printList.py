def printList(listdata):
        print("""
            <style>
            .placesNearYou{
                margin-top:100px;
                text-align:center;
            }
            @media only screen and (min-device-width: 320px) and (max-device-width: 480px) and (-webkit-min-device-pixel-ratio: 2){
                .placesNearYou{
                    margin-top:200px;
                    }
            }

            </style>
        """)
        print("<div class='row'>")
        print("<div class='placesNearYou'>")
        print("<h2>Places Near You!</h2>")
        print("<ol style='list-style:none;margin-left: -60px;'>")
        if (len(listdata[0])>0):
            for x in range(0,len(listdata[0])):
                    print("<li>")
                    print("<b>")
                    print listdata[0][x]
                    print("</b>")
                    print("<ul>")
                    print("<li style='list-style:none;'>")
                    print "Distance from You:",listdata[1][x],"Kilometers"
                    print("</li>")
                    print("</ul>")
                    print("</li>")
        print("</ol>")
        print("</div>")
        print("</div>")
