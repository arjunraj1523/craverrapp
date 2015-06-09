
L.mapbox.accessToken = 'pk.eyJ1IjoiYXJqcmFqMTUyMyIsImEiOiIxNDIyMGYwMTIwNTc0MmRkZmM3M2Q2YjgyM2NkM2U0YSJ9.POQ9sb7vnZFNywt9YRdgXA';
var map = L.mapbox.map('map', 'arjraj1523.a2d90ca6')
    .setView([18.4995719,73.84404540000001], 16);


L.mapbox.featureLayer({
    // this feature is in the GeoJSON format: see geojson.org
    // for the full specification
    type: 'Feature',
    geometry: {
        type: 'Point',
        // coordinates here are in longitude, latitude order because
        // x, y is the standard for GeoJSON and many formats
        coordinates: [
          73.84404540000001,18.4995719 
        ]
    },
    properties: {
        title: 'Peregrine Espresso',
        description: '1718 14th St NW, Washington, DC',
        // one can customize markers by adding simplestyle properties
        // https://www.mapbox.com/guides/an-open-platform/#simplestyle
        'marker-size': 'large',
        'marker-color': '#BE9A6B',
        'marker-symbol': 'building'
    }
}).addTo(map);
