$(document).ready(function (){
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    $("#sendSegnalazioni").on("click", function (){
        let data = {
            'username': $("#id_username").val(),
            'message': $("#id_message").val(),}

        $.ajax({
            method: "POST",
            data: data,
            headers: {'X-CSRFToken': csrftoken},
            url: "/valida-segnalazione/",
            success: function (response){
                if(response["success"] === true){
                    alert("Segnalazione inviata con successo")
                } else {
                    alert("Erroreeeeee")
                }
            }
        })
    })
})