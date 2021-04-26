var $DOM = $(document);
$DOM.on('click', '#add1', function() {
// $DOM.on('click', '#login_submit', function() { 
	console.log("add clicked");
    data = {}
    data["route_id"] = $(".route_id").val();
    data["loc_start"] = $(".loc_start").val();
    data["loc_end"] = $(".loc_end").val();
    data["distance"] = $(".distance").val();
	$.ajax({
		type: 'post',
        data: JSON.stringify(data),
		url: '/admin/add_route/add_route_req/',
		success: function(result) {
            if (result.success) {
                window.location.href = "/admin/add_route/";
                //alertify.set('notifier', 'position', 'top-left');
                //alertify.error(data["loc_start"]);
            }
            else {
                alertify.set('notifier', 'position', 'top-left');
                alertify.error(result.message);
            }
		}
	});
});

