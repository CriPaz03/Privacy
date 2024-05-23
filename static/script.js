$(document).ready(function (){
    $.ajax({
        method: "GET",
        url: "/view-feedback/",
        success: function (response){
            console.log(typeof response["data"])
        }
    })
})