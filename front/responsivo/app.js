$(document).ready(function() {
    $('#form-busca').submit(function(event) {
        console.log(event);
        event.preventDefault();
        let busca = $('#busca-txt').val();
        console.log(busca);
        $.ajax({
            url: `https://dummyapi.io/data/v1/user/${busca}`,
            success: function(data, status) {
                console.log(data);
                console.log(status);
                $('#search-result').text(data.firstName).show();
            },
            headers: {
                "app-id": "617b43e00f0fb30f765f1e12"
            },
            dataType: 'json'
        });
    });
});