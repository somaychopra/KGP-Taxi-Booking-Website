var $DOM = $(document);
// setTimeout(function(){
//     window.location.href = '/user/home/';
//  }, 5000);
$DOM.on('click', '#login_submit', function() {
    
	console.log("Review made");
    data = {}
    data["rating"] = $(".rating").val();
    data["feedback_text"] = $(".feedback_text").val()
    // data["to"] = "ahm"
    data["car_type"] = $(".car_type").val()
    
	$.ajax({
		type: 'post',
        data: JSON.stringify(data),
		url: '/user/in_trip/review/',
		success: function(result) {
            if (result.success) {
                alertify.set('notifier', 'position', 'top-left');
                alertify.error(result.message);
                window.location.href = "/user/home/";
            }
            else {
                alertify.set('notifier', 'position', 'top-left');
                alertify.error(result.message);
            }
		}
	});
});

