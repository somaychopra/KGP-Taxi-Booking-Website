var $DOM = $(document);
$DOM.on('click', '#add', function() {
    
	console.log("add clicked");
    data = {}
    data["number"] = $(".number").val();
    data["model"] = $(".model").val();
    data["number_seats"] = $(".number_seats").val();
	$.ajax({
		type: 'post',
        data: JSON.stringify(data),
		url: '/admin/add_car/add_car_req/',
		success: function(result) {
            if (result.success) {
                window.location.href = "/admin/add_car/";
            }
            else {
                alertify.set('notifier', 'position', 'top-left');
                alertify.error(result.message);
            }
		}
	});
});

