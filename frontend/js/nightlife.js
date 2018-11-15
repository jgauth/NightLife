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
    //var eventdict = {{g.event_dict|tojson}};


    // /api/event_all
    // javascript to get 

    //this is where I'm trying to get the js list
    //$.getJSON('./api/event/all', events, success);
    $.ajax({
    url: '/api/event/all',
    method: 'GET',
    dataType: 'json',
    success: function(data) {
      console.log(data)
      placepins(data)

    },
    error: function(data) {
      console.log(data)
    }
    }); 
    //var event_list = JSON.parse(events);

    

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


    //function for looping through and placing markers
    function placepins(event_list) {
      //loop that adds markers and info windows that appear upon click for each
      for (var i in event_list){
          //event_list is a list of events, currentdict represents the current event in the list so a marker can be set
          var current_event = event_list[i];
          //get relevant values for the marker
          var name = current_event["name"]
          var description = current_event["description"]
          
          var lat = current_event["lat"];
          var long = current_event["long"];
          var address = current_event["address"]
          
          console.log(lat, long);
          //creates new marker for this event
          var marker = new google.maps.Marker({
            position: {lat, long};
            map: map,
            info: description,
            title: name,
            //testing different marker appearance, in this case what google calls a "bar" marker, might be relevant for this project
            icon: iconBase + 'bars.png',
            //drop animation
            animation: google.maps.Animation.DROP
            
          });
          //makes infowindow appear upon click for each marker
          marker.addListener('click', function() {
            infowindow.setContent(this.info);
            infowindow.open(map, this);
            
          });
        }
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