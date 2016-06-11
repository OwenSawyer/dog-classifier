/*global $*/
class Main {
    constructor() {
        this.initialize();
    }
    initialize() {
        $.ajax({
            url: '/api/x',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(inputs),
            success: (data) => {
	        $('#output').text(data);
            }
        });
    }
}

$(() => {
    var main = new Main();
    $('#clear').click(() => {
        main.initialize();
    });
});
