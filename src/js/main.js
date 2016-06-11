$(document).ready(function(){
  $('#click').click(function() { 
	alert("Here");
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
    	return false;
  });
});
