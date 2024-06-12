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
            headers: {'X-CSRFToken': csrftoken},
            data: data,
            dataType: "json",
            success: function (response) {
                let html = ""
                for (let i in response) {
                    html += `<tr>
                    <th><input class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios${i}" value="option1" checked><label class="form-check-label" for="exampleRadios${i}" id="${i}"></label></th>
                    <td>${response[i]["patterns"]}</td>
                    <td>${response[i]["description"]}</td>
                    <td>${response[i]["strategies"]}</td>
                    </tr>`
                }
                $("#bodyPatterns").append(html)
                if (html !== "")
                    $("#buttons").removeClass("invisible")
                else
                    $("#buttons").removeClass("visible").addClass("invisible")
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

    $("#exemple").on("click", function () {
        callApi("/exemple-patterns/", "#listExemple", "exemple")
    })
    $("#design").on("click", function () {
        callApi("/privacy-by-design/", "#listDesign", "privacy")
    })
})

function callApi(urls, list, responseSucc){
    let radio = $(".form-check-label")
        for (let i = 0; i < radio.length; i++) {
            let id = radio[i].id
            if ($("#exampleRadios" + id).is(":checked")) {
                $(list).html("")
                $.ajax({
                    method: "GET",
                    url: urls + id,
                    success: function (response) {
                        if (response["success"] === true) {
                            for (let r in response[responseSucc]) {
                                for (let b = 0; b < response[responseSucc][r].length; b++) {
                                    $(list).append(`<li class="list-group-item">${response[responseSucc][r][b]}</li>`)
                                }
                            }
                        }
                    }
                })
            }
        }
}