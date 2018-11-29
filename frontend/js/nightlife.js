/*
 Primary static JS functionality to control event map
*/


// Google Maps pin icons and themes for events
let iconBase = '../images/icons/';
let baseIcon = '../images/icons/party.png'
let themes = new Set(["Toga", "Halloween", "Date Dash", "Formal"]);


function initMap() {
  /*
   Initializes map inside of div element, places pins using JSON data 
   */
  var eug = {lat: 44.0520691, lng: -123.0867536}; // Center map on campus 

  var currentLocation = new google.maps.InfoWindow; // Access user location

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 15,
    center: eug,

    // Styling the map to dark mode
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

  if (navigator.geolocation) {
    // Attempts to get user geo location and place a pin on the map with their location, using success and failure handlers
      navigator.geolocation.getCurrentPosition(function(position) {
        var pos = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };

        currentLocation.setPosition(pos);
        currentLocation.setContent('Location found.');
        currentLocation.open(map);
        map.setCenter(pos);
      }, function() {
        handleLocationError(true, currentLocation, map.getCenter());
      });
  } else {
      // Browser doesn't support Geolocation, error handler
      handleLocationError(false, currentLocation, map.getCenter());
  }
  function handleLocationError(browserHasGeolocation, currentLocation, pos) {
    currentLocation.setPosition(pos);
    currentLocation.setContent("Unable to find your current location");
    currentLocation.open(map);
  }

  $.ajax({
    // AJAX call to get all events from application API
    url: '/api/event/all',
    method: 'GET',
    dataType: 'json',
    success: function(data) {
      placepins(data['events'])

    },
    error: function(data) {
      console.log('unable to load events')
    }
  });

  function placepins(events) {
    /*
     Iterate over JSON dict and place map markers using geo location
     */
    var partyInfoWindow = new google.maps.InfoWindow;

    var contentInfo = [], marker, i;
    for (i=0; i<events.length; i++){
      event = events[i]

      // Re-formatting datetime strings
      let startTime = new Date(event.time_start).toLocaleString()
      let endTime = new Date(event.time_end).toLocaleString()


      // Creating an info window for each individual event, hashing it with in array
      contentInfo[i] = '<div class="partyMarker">'
      +'<h3 class="partyMarkerHeading">'+String(event.name)+'</h3>'
      +'<b>Host: </b>'+String(event.host)+'<br />'
      +'<b>Theme: </b>'+String(event.theme)+'<br />'
      +'<b>Start: </b>'+startTime+'<br />'
      +'<b>End: </b>'+endTime+'<br /><br />'
      +'<p>'+String(event.description)+'</p>'
      +'<form action="/api/event/add_rating" method="POST">'
      +'<p><b>Rate: </b><input id="partyRatingSlider" name="partyRatingSlider" type="range" min="1" max="5" value="5" class="slider">&nbsp;<span id="partyRatingSliderLabel">5</span></p>'
      +'<input type="hidden" name="eventId" value="'+event.id+'">'
      +'<button type="submit" class="btn btn-primary btn-sm">Submit Rating</button>'
      +'</form>'
      +'</div>';

      // If the user selects a pre-determined theme, use the icon for that theme, else give a generic icon
      if (themes.has(event.theme)) {
        eventIcon = iconBase + event.theme.replace(' ','-') + '.png';
      } else {
        console.log(typeof(event.theme))
        console.log(themes)
        console.log(event.theme,"NOT IN SET")
        eventIcon = baseIcon;
      }

      // Place the maps marker
      marker = new google.maps.Marker({
        position: {lat: event.lat, lng: event.lng},
        map: map,
        title: event.name,
        icon: eventIcon,
        animation: google.maps.Animation.DROP,
      });
    
      // Allow each marker to have an info window, attach a listener    
      google.maps.event.addListener(marker, 'click', (function(marker, i) {
          return function() {
              partyInfoWindow.setContent(contentInfo[i]);
              partyInfoWindow.open(map, marker);
          }
      })(marker, i));

      // Attach listener for rating slider
      google.maps.event.addListener(partyInfoWindow, 'domready', function() {
        $('#partyRatingSlider').on('input', function(){
          $('#partyRatingSliderLabel').text($(this).val());
        });
      });
    }
  }
};

$(document).ready(function(){
  // On DOM-load, load the map.
  $(initMap);
});