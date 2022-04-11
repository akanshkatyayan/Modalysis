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

$("form[name=updateuser_form").submit(function(e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/updateuser",
        type: "PUT",
        data: data,
        dataType: "json",
        success: function(resp){
            window.location.href = "/dashboard/manageusers/";
            },
        error: function(resp){
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
            }

    });
    e.preventDefault();
});


$("form[name=getuser_form").submit(function(e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/getusers",
        type: "GET",
        data: data,
        dataType: "json",
        success: function(resp){
            console.log(resp);
            var users_data = resp
            var table = document.createElement("table");

                // CREATE HTML TABLE HEADER ROW USING THE EXTRACTED HEADERS ABOVE.

            var tr = table.insertRow(-1);                   // TABLE ROW.
            var col = ["Name", "Email Id"]
            for (var i = 0; i < col.length; i++) {
                var th = document.createElement("th");      // TABLE HEADER.
                th.innerHTML = col[i];
                tr.appendChild(th);
            }

            console.log("length:", Object.keys(users_data).length)

                // ADD JSON DATA TO THE TABLE AS ROWS.
            for (var i = 0; i < Object.keys(users_data).length; i++) {

                tr = table.insertRow(-1);

                for (var j = 0; j < col.length; j++) {
                    var tabCell = tr.insertCell(-1);
                    tabCell.innerHTML = users_data[i][col[j]];
                }
            }

                // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
            var divContainer = document.getElementById("showUserData");
            divContainer.innerHTML = "";
            divContainer.appendChild(table);

            //$data.text(resp);
            //window.location.href = "/dashboard/manageusers/";
            },
        error: function(resp){
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
            }

    });
    e.preventDefault();
});


$("form[name=summaryresult_form").submit(function(e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/dashboard/discord",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp){
            window.location.href = "/dashboard/summarizer/";
            },
        error: function(resp){
            console.log(resp);
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
            }

    });
    e.preventDefault();
});
