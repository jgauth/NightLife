$(document).ready(function(){
    $.ajax({
        /*
        AJAX call to populate top parties table. Takes JSON payload from api endpoint and populates table data with events.
        */
        url: '/api/event/all',
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            events = data['events']
            for (var i=0; i<events.length; i++){
                event = events[i];
                if (event.rating == 0) {
                    rating = 'No Ratings';
                } else {
                    rating = event.rating.toFixed(2);
            }
            
            row = '<tr>'
                + '<td>'+rating+'</td>'
                + '<td>'+event.name+'</td>'
                + '<td>'+event.theme+'</td>'
                + '<td>'+event.description+'</td>'
                + '<td>'+new Date(event.time_start).toLocaleString()+'-'+new Date(event.time_end).toLocaleString()+'</td>'
                + '</tr>';
            
            $('tbody#partyReviews').append(row);
            }

        },
        error: function(data) {
            console.log("Failed to load events");
        }
    });
});