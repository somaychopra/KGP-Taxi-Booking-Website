var $DOM = $(document);
$DOM.on('click', '#signup_submit', function() {
    
	console.log("signup clicked");
    data = {}
    data["email"] = $(".email").val();
    data["name"] = $(".name").val()
    data["gender"] = $(".gender").val()
    data["age"] = $(".age").val()
    data["password"] = $(".password").val()
    data["phone_number"] = $(".phone_number").val();

	$.ajax({
		type: 'post',
        data: JSON.stringify(data),
		url: 'signup_req/',
		success: function(result) {
            if (result.success) {
                window.location.href = "/driver/login/";
            }
            else {
                alertify.set('notifier', 'position', 'top-left');
                alertify.error(result.message);
            }
		}
	});
});
