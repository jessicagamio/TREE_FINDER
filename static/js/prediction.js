
    function initMap(){
        const sfBayCoords={lat: 37.7809825, lng:-122.444124};

        const map = new google.maps.Map(document.getElementById('map'),{
                center: sfBayCoords,
                zoom:15
        });


        const markers = {{ markers|tojson }};

        for (let mark of markers){
            let [ lat, lng ] = mark;
            // console.log(lat,lng);
            let marker = new google.maps.Marker(
                { 
                    position: {
                        lat: lat,
                        lng: lng
                    },
                    map: map
                }
            );
        }

         if (navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude
            };
            // console.log(pos);
            let user_marker= new google.maps.Marker(
                {position:pos,map:map});
        })
    }

}



     function processHug(evt){
    
        function hugCoord(){

            navigator.geolocation.getCurrentPosition(function(position) {
                var pos = {
                  lat: position.coords.latitude,
                  lng: position.coords.longitude }; })
        }

        const userSession = $('#logout-button').data('session');
        evt.preventDefault();
        
        if (userSession){ 

            const hugs = document.getElementById('treehugs');

            function changeToRed(){
                hugs.class="btn btn-danger";
                $('#treehugs').html("Hugged");
            }

            const hugInfo = {
                'tree_species':$('#treehugs').data('sciName'),
                'user_id': $('#logout-button').data('session')     
            };
           
            $.post('/hugs',hugInfo,changeToRed);
        }

    }

    $('#treehugs').on('click', processHug);
