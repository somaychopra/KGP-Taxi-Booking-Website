var $DOM = $(document);
$DOM.on('click', '#add', function() {
    
	console.log("add clicked");
    data = {}
    data["driver_email"] = $(".driver_email").val();
    data["car_number"] = $(".car_number").val();
	$.ajax({
		type: 'post',
        data: JSON.stringify(data),
		url: '/admin/allocate/allocate_req/',
		success: function(result) {
            if (result.success) {
                window.location.href = "/admin/allocate/";
            }
            else {
                alertify.set('notifier', 'position', 'top-left');
                alertify.error(result.message);
            }
		}
	});
});

