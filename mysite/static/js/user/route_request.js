var $DOM = $(document);
// setTimeout(function(){
//     window.location.href = '/user/home/';
//  }, 5000);
$DOM.on('click', '#login_submit', function() {
    
	console.log("Route requested");
    data = {}
    data["from"] = $(".from").val();
    data["to"] = $(".to").val()
    // data["to"] = "ahm"
    data["car_type"] = $(".car_type").val()
    
	$.ajax({
		type: 'post',
        data: JSON.stringify(data),
		url: '/user/home/route_req/',
		success: function(result) {
            if (result.success) {
                window.location.href = "route_accept/";
            }
            else {
                alertify.set('notifier', 'position', 'top-left');
                alertify.error(result.message);
            }
		}
	});
});

