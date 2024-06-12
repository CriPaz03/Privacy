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
        sendNotification(radio)
    })
})