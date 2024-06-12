$(document).ready(function () {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    $("#addFeedback").on("click", function () {

        let data = {
            'username': $("#id_username").val(),
            'message': $("#id_message").val(),
        }

        $.ajax({
            url: "/add-feedback/",
            method: "POST",
            headers: {'X-CSRFToken': csrftoken},
            data: data,
            dataType: "json",
            success: function (response) {
                if(response["success"] === true){
                    alert("Feedback aggiunto con successo")
                    window.location.reload()
                }
                else
                    alert("Feedback non andato a buon fine")
            }
        })
    })
})