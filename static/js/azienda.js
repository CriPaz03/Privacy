$(document).ready(function (){
    $("#sArticle").on("click", function (){
        $.ajax({
            method: "GET",
            url: "/spiegazioneArticle/" +  $("#article").val() + "/",
            success: function (response){
                if(response["success"] === true){
                    $("#modalSpiegazione").show()
                    $("#modalSpiegazione #bodySpiegazione").text(response["response"])
                    $(".close").on("click", function (){
                        $("#modalSpiegazione").hide()
                    })
                }
            }
        })
    })

    $("#sendNotify").on("click", function () {
        let radio = $(".form-check-label")
        sendNotification(radio)
    })
})