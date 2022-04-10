$("form[name=signup_form").submit(function(e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/signup",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp){
            window.location.href = "/dashboard/";
            },
        error: function(resp){
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
            }

    });
    e.preventDefault();
});



$("form[name=login_form").submit(function(e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/login",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp){
            window.location.href = "/dashboard/";
            },
        error: function(resp){
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
            }

    });
    e.preventDefault();
});

$("form[name=updatepassword_form").submit(function(e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/updatepassword/",
        type: "PUT",
        data: data,
        dataType: "json",
        success: function(resp){
            window.location.href = "/dashboard/";
            },
        error: function(resp){
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
            }

    });
    e.preventDefault();
});


$("form[name=uploadmodel_form").submit(function(e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/dashboard/uploadmlmodel/",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp){
            window.location.href = "/dashboard/";
            },
        error: function(resp){
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
            }

    });
    e.preventDefault();
});

$("form[name=createuser_form").submit(function(e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/createuser",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp){
            console.log(resp);
            window.location.href = "/dashboard/manageusers/";
            },
        error: function(resp){
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
            }

    });
    e.preventDefault();
});


$("form[name=deleteuser_form").submit(function(e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/deleteuser",
        type: "DELETE",
        data: data,
        dataType: "json",
        success: function(resp){
            console.log(resp);
            window.location.href = "/dashboard/manageusers/";
            },
        error: function(resp){
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
            }

    });
    e.preventDefault();
});

