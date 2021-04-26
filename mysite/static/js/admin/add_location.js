var $DOM = $(document);
$DOM.on('click', '#add', function() {
    
	console.log("add clicked");
    data = {}
    data["location_id"] = $(".location_id").val();
    data["location_name"] = $(".location_name").val();
    data["is_outstation"] = $(".is_outstation").val();
	$.ajax({
		type: 'post',
        data: JSON.stringify(data),
		url: '/admin/add_location/add_location_req/',
		success: function(result) {
            if (result.success) {
                window.location.href = "/admin/add_location/";
            }
            else {
                alertify.set('notifier', 'position', 'top-left');
                alertify.error(result.message);
            }
		}
	});
});

