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
    var i;
    for (i=0; i<events.length; i++){
      event = events[i]

      var marker = new google.maps.Marker({
        position: {lat: event.lat, lng: event.lng},
        map: map,
        info: event.description,
        title: event.name,
        animation: google.maps.Animation.DROP
      });

      var window = new google.maps.InfoWindow;
      marker.addListener('click', function() {
        window.setContent(this.info);
        window.open(map, this);
      });
      }
    }
  };

$(document).ready(function(){
  $(initMap);
});