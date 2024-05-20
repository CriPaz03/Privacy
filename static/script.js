$(document).ready(function (){
    console.log("ciaqo")
    $.ajax({
        method: "GET",
        url: "/view-feedback/",
        success: function (response){
            console.log(typeof response["data"])

        }
    })
})