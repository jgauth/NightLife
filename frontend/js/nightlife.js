let iconBase = '../images/icons/';
let baseIcon = '../images/icons/party.png'
let themes = new Set(["Toga", "Halloween", "Date Dash", "Formal"]);


function initMap() {
  var eug = {lat: 44.0520691, lng: -123.0867536};

  var currentLocation = new google.maps.InfoWindow;

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

  if (navigator.geolocation) {
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
      // Browser doesn't support Geolocation
      handleLocationError(false, currentLocation, map.getCenter());
  }
  function handleLocationError(browserHasGeolocation, currentLocation, pos) {
    currentLocation.setPosition(pos);
    currentLocation.setContent("Unable to find your currnet location");
    currentLocation.open(map);
  }

  $.ajax({
    url: '/api/event/all',
    method: 'GET',
    dataType: 'json',
    success: function(data) {
      console.log(data['events'])
      placepins(data['events'])

    },
    error: function(data) {
      console.log(data['events'])
    }
  });

  function placepins(events) {
    var partyInfoWindow = new google.maps.InfoWindow, contentInfo = [], marker, i;
    for (i=0; i<events.length; i++){
      event = events[i]

      let startTime = new Date(event.time_start).toLocaleString()
      let endTime = new Date(event.time_end).toLocaleString()

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

      if (themes.has(event.theme)) {
        eventIcon = iconBase + event.theme.replace(' ','-') + '.png';
      } else {
        console.log(typeof(event.theme))
        console.log(themes)
        console.log(event.theme,"NOT IN SET")
        eventIcon = baseIcon;
      }

      marker = new google.maps.Marker({
        position: {lat: event.lat, lng: event.lng},
        map: map,
        title: event.name,
        icon: eventIcon,
        animation: google.maps.Animation.DROP,
      });
    
      // Allow each marker to have an info window    
      google.maps.event.addListener(marker, 'click', (function(marker, i) {
          return function() {
              partyInfoWindow.setContent(contentInfo[i]);
              partyInfoWindow.open(map, marker);
          }
      })(marker, i));

      google.maps.event.addListener(partyInfoWindow, 'domready', function() {
        $('#partyRatingSlider').on('input', function(){
          $('#partyRatingSliderLabel').text($(this).val());
        });
      });
    }
  }
};

$(document).ready(function(){
  $(initMap);
});