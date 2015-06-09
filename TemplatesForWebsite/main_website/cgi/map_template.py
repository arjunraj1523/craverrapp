def map_template(listdata,current_location_lat,current_location_lng):
    print('<div style="margin-top:30%">')
    print('</div>')
    print("""<script src='https://api.tiles.mapbox.com/mapbox.js/v2.1.9/mapbox.js'></script>
				<link href='https://api.tiles.mapbox.com/mapbox.js/v2.1.9/mapbox.css' rel='stylesheet' />
				<style>
  body { margin:0; padding:0; }
  #map {
  position:absolute !important;
  top: 0;
  bottom: 0;
  width: 100%;
  height:500px;
  margin: 175px 19px 30px;
}
				</style>
				<div class="row">
                
				<div id='map'></div>
				</div>
				<script>L.mapbox.accessToken = 'pk.eyJ1IjoiYXJqcmFqMTUyMyIsImEiOiIxNDIyMGYwMTIwNTc0MmRkZmM3M2Q2YjgyM2NkM2U0YSJ9.POQ9sb7vnZFNywt9YRdgXA';
var map = L.mapbox.map('map', 'arjraj1523.a2d90ca6')
    .setView(["""),current_location_lat,(""","""),current_location_lng,("""], 13);""")

    print("""
L.mapbox.featureLayer({
    // this feature is in the GeoJSON format: see geojson.org
    // for the full specification
    type: 'Feature',
    geometry: {
        type: 'Point',
        // coordinates here are in longitude, latitude order because
        // x, y is the standard for GeoJSON and many formats
        coordinates: [
          """),listdata[2][1],(""","""),listdata[2][0],(""" 
        ]
    },
    properties: {
        title: 'Point-1',
        description: 'Distance from You:"""),listdata[1][0],("""Km',
        'marker-size': 'large',
        'marker-color': '#BE9A6B',
        'marker-symbol': 'restaurant'
    }
}).addTo(map);
L.mapbox.featureLayer({
    // this feature is in the GeoJSON format: see geojson.org
    // for the full specification
    type: 'Feature',
    geometry: {
        type: 'Point',
        // coordinates here are in longitude, latitude order because
        // x, y is the standard for GeoJSON and many formats
        coordinates: [
          """),listdata[2][3],(""","""),listdata[2][2],(""" 
        ]
    },
    properties: {
        title: 'Point-2',
        description: 'Distance from You:"""),listdata[1][1],("""Km',
        'marker-size': 'large',
        'marker-color': '#BE9A6B',
        'marker-symbol': 'restaurant'
    }
}).addTo(map);
L.mapbox.featureLayer({
    // this feature is in the GeoJSON format: see geojson.org
    // for the full specification
    type: 'Feature',
    geometry: {
        type: 'Point',
        // coordinates here are in longitude, latitude order because
        // x, y is the standard for GeoJSON and many formats
        coordinates: [
          """),listdata[2][5],(""","""),listdata[2][4],(""" 
        ]
    },
    properties: {
        title: 'Point-3',
        description: 'Distance from You:"""),listdata[1][2],("""Km',
        'marker-size': 'large',
        'marker-color': '#BE9A6B',
        'marker-symbol': 'restaurant'
    }
}).addTo(map);

L.mapbox.featureLayer({
    // this feature is in the GeoJSON format: see geojson.org
    // for the full specification
    type: 'Feature',
    geometry: {
        type: 'Point',
        // coordinates here are in longitude, latitude order because
        // x, y is the standard for GeoJSON and many formats
        coordinates: [
          """),listdata[2][7],(""","""),listdata[2][6],(""" 
        ]
    },
    properties: {
        title: 'Point-4',
        description: 'Distance from You:"""),listdata[1][3],("""Km',
        'marker-size': 'large',
        'marker-color': '#BE9A6B',
        'marker-symbol': 'restaurant'
    }
}).addTo(map);

L.mapbox.featureLayer({
    // this feature is in the GeoJSON format: see geojson.org
    // for the full specification
    type: 'Feature',
    geometry: {
        type: 'Point',
        // coordinates here are in longitude, latitude order because
        // x, y is the standard for GeoJSON and many formats
        coordinates: [
          """),listdata[2][9],(""","""),listdata[2][8],(""" 
        ]
    },
    properties: {
        title: 'Point-5',
        description: 'Distance from You:"""),listdata[1][4],("""Km',
        'marker-size': 'large',
        'marker-color': '#BE9A6B',
        'marker-symbol': 'restaurant'
    }
}).addTo(map);


L.mapbox.featureLayer({
    // this feature is in the GeoJSON format: see geojson.org
    // for the full specification
    type: 'Feature',
    geometry: {
        type: 'Point',
        // coordinates here are in longitude, latitude order because
        // x, y is the standard for GeoJSON and many formats
        coordinates: [
          """),current_location_lng,(""","""),current_location_lat,(""" 
        ]
    },
    properties: {
        title: 'Current Location',
        // one can customize markers by adding simplestyle properties
        // https://www.mapbox.com/guides/an-open-platform/#simplestyle
        'marker-size': 'large',
        'marker-color': '#BE9A6B',
        'marker-symbol': 'building'
    }
}).addTo(map);
</script> """)
