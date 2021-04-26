var $DOM = $(document);
setTimeout(function(){
    window.location.href = '/driver/home/';
 }, 5000);

$DOM.on('click', '#update_location', function() {
    
	console.log("login clicked");
    data = {}
    data["location_id"] = $(".location_id").val();

	$.ajax({
		type: 'post',
        data: JSON.stringify(data),
		url: 'set/location/',
		success: function(result) {
            if (result.success) {
                window.location.href = "/driver/home/";
            }
            else {
                alertify.set('notifier', 'position', 'top-left');
                alertify.error(result.message);
            }
		}
	});
});

$DOM.on('click', '#start_trip', function() {
    
	console.log("login clicked");
    data = {}
    // data["location_id"] = $(".location_id").val();

	$.ajax({
		type: 'post',
        data: JSON.stringify(data),
		url: 'start/',
		success: function(result) {
            if (result.success) {
                window.location.href = "/driver/home/";
            }
            else {
                alertify.set('notifier', 'position', 'top-left');
                alertify.error(result.message);
            }
		}
	});
});


var $DOM = $(document);
$DOM.on('click', '#end_trip', function() {
    
	console.log("login clicked");
    data = {}
    // data["location_id"] = $(".location_id").val();

	$.ajax({
		type: 'post',
        data: JSON.stringify(data),
		url: 'end/',
		success: function(result) {
            if (result.success) {
                window.location.href = "/driver/home/";
            }
            else {
                alertify.set('notifier', 'position', 'top-left');
                alertify.error(result.message);
            }
		}
	});
});
