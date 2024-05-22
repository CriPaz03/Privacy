$(document).ready(function () {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    $("#searchPatterns").on("click", function () {
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
                console.log(response)
                for(let i in response){
                    html += `<tr>
                    <th>${i}</th>
                    <td>${response[i]["patterns"]}</td>
                    <td>${response[i]["description"]}</td>
                    <td>${response[i]["strategies"]}</td>
                    </tr>`
                }
                $("#bodyPatterns").append(html)

            }
        })
    })
})