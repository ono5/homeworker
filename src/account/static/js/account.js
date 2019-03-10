var error = document.getElementById('id_error');


var atsnow = new ATSnow({
	classname : 'sakura',
	count : 50,
	interval : 60,
	maxSize : error ? 50 : 10,
	minSize : 1,
	leftMargin : 10,
	rightMargin : 20,
	bottomMargin : 0,
	maxDistance : 10,
	minDistance : 1
});

atsnow.load();
