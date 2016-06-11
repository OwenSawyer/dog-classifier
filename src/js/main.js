/*global $*/
class Main {
    constructor() {
        this.initialize();
    }
    initialize() {
        $.ajax({
            url: '/api/mnist',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(inputs),
            success: (data) => {
	        $('#output').text(data);
            },
	    error: (err) => {
	        alert("err");
	    }
        });
    }
}

$(document).ready(function(){
  $('#click').click(function() { 
    var main = new Main();
    main.initialize();
    return false;
  });
});
