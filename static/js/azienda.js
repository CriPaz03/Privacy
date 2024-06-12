$(document).ready(function (){
    $("#sArticle").on("click", function (){
        $.ajax({
            method: "GET",
            url: "/spiegazioneArticle/" +  $("#article").val() + "/",
            success: function (response){
                if(response["success"] === true){
                    $("#responseGpt").text(response["response"])
                }
            }
        })
    })

    $("#sendNotify").on("click", function () {
        let radio = $(".form-check-label")
        for (let i = 0; i < radio.length; i++) {
            let id = radio[i].id
            if ($("#exampleRadios" + id).is(":checked")) {
                $.ajax({
                    method: "GET",
                    url: "/send-notification/" + id,
                    success: function (response) {
                        if (response["success"] === true) {
                            alert("Sistema di notifiche attivo")
                        }else {
                            alert("ERRORE")
                        }
                    }
                })
            }
        }
    })
})