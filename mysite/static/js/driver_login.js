var $DOM = $(document);
$DOM.on('click', '#login_submit', function() {
    
	console.log("login clicked");
    data = {}
    data["email"] = $(".email").val();
    data["password"] = $(".password").val()

	$.ajax({
		type: 'post',
        data: JSON.stringify(data),
		url: 'login_req/',
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

