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
        let check = $(".table-check:checked")
    })

    $("#exemple").on("click", function () {
        let radio = $(".form-check-label")
        for (let i = 0; i < radio.length; i++) {
            let id = radio[i].id
            if ($("#exampleRadios" + id).is(":checked")) {
                $("#listExemple").html("")
                $.ajax({
                    method: "GET",
                    url: "/exemple-patterns/" + id,
                    success: function (response) {
                        if (response["success"] === true) {
                            for (let r in response["exemple"]) {
                                for (let b = 0; b < response["exemple"][r].length; b++) {
                                    $("#listExemple").append(`<li class="list-group-item">${response["exemple"][r][b]}</li>`)
                                }
                            }
                        }
                    }
                })
            }
        }
    })
})