function initMap() {
    var eug = {lat: 44.0520691, lng: -123.0867536};

    var infoWindow = new google.maps.InfoWindow;

    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 15,
      center: eug,

      styles: [
        {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
        {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
        {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]},
        {
          featureType: 'administrative.locality',
          elementType: 'labels.text.fill',
          stylers: [{color: '#d59563'}]
        },
        {
          featureType: 'poi',
          elementType: 'labels.text.fill',
          stylers: [{color: '#d59563'}]
        },
        {
          featureType: 'poi.park',
          elementType: 'geometry',
          stylers: [{color: '#263c3f'}]
        },
        {
          featureType: 'poi.park',
          elementType: 'labels.text.fill',
          stylers: [{color: '#6b9a76'}]
        },
        {
          featureType: 'road',
          elementType: 'geometry',
          stylers: [{color: '#38414e'}]
        },
        {
          featureType: 'road',
          elementType: 'geometry.stroke',
          stylers: [{color: '#212a37'}]
        },
        {
          featureType: 'road',
          elementType: 'labels.text.fill',
          stylers: [{color: '#9ca5b3'}]
        },
        {
          featureType: 'road.highway',
          elementType: 'geometry',
          stylers: [{color: '#746855'}]
        },
        {
          featureType: 'road.highway',
          elementType: 'geometry.stroke',
          stylers: [{color: '#1f2835'}]
        },
        {
          featureType: 'road.highway',
          elementType: 'labels.text.fill',
          stylers: [{color: '#f3d19c'}]
        },
        {
          featureType: 'transit',
          elementType: 'geometry',
          stylers: [{color: '#2f3948'}]
        },
        {
          featureType: 'transit.station',
          elementType: 'labels.text.fill',
          stylers: [{color: '#d59563'}]
        },
        {
          featureType: 'water',
          elementType: 'geometry',
          stylers: [{color: '#17263c'}]
        },
        {
          featureType: 'water',
          elementType: 'labels.text.fill',
          stylers: [{color: '#515c6d'}]
        },
        {
          featureType: 'water',
          elementType: 'labels.text.stroke',
          stylers: [{color: '#17263c'}]
        }
      ]
    });

    //dict with locations/events
    var eventdict = {{g.event_dict|tojson}};

    //loop that adds markers and info windows that appear upon click for each
        for (var i in eventtdict){
          //eventdict is a list of dicts, currentdict represents the current dict in the list so a marker can be set
          var currentdict = eventdict[i];
          //get relevant values for the marker
          var name = currentdict["name"]
          var description = currentdict["description"]
          
          var lat = currentdict["lat"];
          var long = currentdict["long"];
          var address = currentdict["address"]
          
          console.log(lat, long);
          //creates new marker for this event
          var marker = new google.maps.Marker({
            //position: poss,
            map: map,
            info: description
            
          });
          //makes infowindow appear upon click for any marker
          marker.addListener('click', function() {
            infowindow.setContent(this.info);
            infowindow.open(map, this);
            
          });
        }

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
          var pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
          };

          infoWindow.setPosition(pos);
          infoWindow.setContent('Location found.');
          infoWindow.open(map);
          map.setCenter(pos);
        }, function() {
          handleLocationError(true, infoWindow, map.getCenter());
        });
    } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
    }

    function handleLocationError(browserHasGeolocation, infoWindow, pos) {
      infoWindow.setPosition(pos);
      infoWindow.setContent("Oops, we can't find you!");
      infoWindow.open(map);
    }

    //For changing marker appearance, just a test for now
    var iconBase = 'images/icons/';

    var marker = new google.maps.Marker({
      position: eug,
      map: map,
      title: 'Hello World!',
      info: "This is Eugene Party Central",
      //testing different marker appearance, in this case what google calls a "bar" marker, might be relevant for this project
      icon: iconBase + 'bars.png',
      //drop animation
      animation: google.maps.Animation.DROP

    });

    marker.addListener('click', function() {
        infowindow.setContent(this.info);
        infowindow.open(map, this);
        
     });
};

$(document).ready(function(){
    $(initMap);
});