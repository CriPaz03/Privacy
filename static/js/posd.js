$(document).ready(function () {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    $("#searchPatterns").on("click", function () {
        $("#bodyPatterns").empty()
        let data = JSON.stringify({
            text: $("#searchP").val(),
            article: $("#article").val(),
            owasp: $("#owasp").val(),
        });
        $.ajax({
            url: "/search-patterns/",
            method: "POST",
            headers: {'X-CSRFToken':csrftoken},
            data:data,
            dataType: "json",
            success: function (response){
                let html = ""
                for(let i in response){
                    html += `<tr>
                    <th><input class="form-check-input table-check" type="checkbox" id="${i}"></th>
                    <td>${response[i]["patterns"]}</td>
                    <td>${response[i]["description"]}</td>
                    <td>${response[i]["strategies"]}</td>
                    </tr>`
                }
                $("#bodyPatterns").append(html)
                if(html!=="")
                    $("#buttons").removeClass("invisible")
                else
                    $("#buttons").removeClass("visible").addClass("invisible")
            }
        })
    })

    $("#sendNotify").on("click", function (){
        let check = $(".table-check:checked")
        console.log(check)

    })
})