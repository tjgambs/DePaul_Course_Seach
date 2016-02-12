function run() {
	readSelections();
	readCreditSelections();
	$('#help').mousedown(function(e) {
		var clicked = $(e.target);
		if (clicked.is('#help-container') || clicked.parents().is('#help-container')) {
			return;
		} else {
			el = document.getElementById("help");
			el.style.visibility = (el.style.visibility == "hidden") ? "visible" : "hidden";
		}
	});
	$('#overlay').mousedown(function(e) {
		var clicked = $(e.target);
		if (clicked.is('#advanced-container') || clicked.parents().is('#advanced-container')) {
			return;
		} else {
			el = document.getElementById("overlay");
			el.style.visibility = (el.style.visibility == "hidden") ? "visible" : "hidden";
		}
	});
	$.fn.select2.amd.require(['select2/compat/matcher'], function(oldMatcher) {
		$("select").select2({
			matcher: oldMatcher(matchStart)
		})
	});
	$(".credit-input").keyup(function(e) {
		if (e.keyCode == 13) {
			creditSearch();
		}
	});
	$(".number").keyup(function(e) {
		if (e.keyCode == 13) {
			submitForm();
		}
	});
	if ("onhashchange" in window) {
		saveSelections();
	}
}

function saveSelections() {
	var prefix = document.getElementsByClassName('prefix')[0].value;
	var number = document.getElementsByClassName('number')[0].value;
	writeCookie('depaul-university-standard-prefix', prefix);
	writeCookie('depaul-university-standard-number', number);
}

function saveCreditPrefix() {
	var prefix = document.getElementsByClassName('credit-prefix')[0].value;
	writeCookie('depaul-university-standard-prefix', prefix);
	writeCookie('depaul-university-standard-number', '');
}

function readCreditSelections() {
	var prefix = readCookie('depaul-university-standard-prefix');
	if (prefix) {
		document.getElementsByClassName('credit-prefix')[0].value = prefix;
	}
}

function readSelections() {
	var prefix = readCookie('depaul-university-standard-prefix');
	var number = readCookie('depaul-university-standard-number');
	if (prefix) {
		document.getElementsByClassName('prefix')[0].value = prefix;
	}
	if (number) {
		document.getElementsByClassName('number')[0].value = number;
	}
}

function writeCookie(name, value, days) {
	var date, expires;
	if (days) {
		date = new Date();
		date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
		expires = "; expires=" + date.toGMTString();
	} else {
		expires = "";
	}
	document.cookie = name + "=" + value + expires + "; path=/";
}

function readCookie(name) {
	var i, c, ca, nameEQ = name + "=";
	ca = document.cookie.split(';');
	for (i = 0; i < ca.length; i++) {
		c = ca[i];
		while (c.charAt(0) == ' ') {
			c = c.substring(1, c.length);
		}
		if (c.indexOf(nameEQ) == 0) {
			return c.substring(nameEQ.length, c.length);
		}
	}
	return '';
}

function creditSearch() {
	var prefix = document.getElementsByClassName('credit-prefix')[0].value;
	var credit = document.getElementsByClassName('credit-input')[0].value;
	if (isNaN(credit) == false) {
		var search = prefix.toLowerCase() + '-credits=' + credit;
		document.getElementById('tipue_search_input').value = '"' + search + '"';
		document.getElementById('field').submit();
		saveCreditPrefix();
	}
}

function updateCourseCartCount() {
	var cookies = document.cookie;
	var term = readCookie('depaul-university-term');
	if (!term) {
		writeCookie('depaul-university-term', 'winter-2016', 1);
		term = readCookie('depaul-university-term');
	}
	var count = 0;
	for (i of cookies.split(';')) {
		var cookie = i.split(',');
		if (cookie[0].indexOf('-add-') != -1) {
			if (cookie[0].indexOf(term) != -1) {
				count += 1;
			}
		}
	}
	document.getElementById('course-cart').innerHTML = 'Course Cart (' + count + ')';
}

function help() {
	el = document.getElementById("help");
	el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
}

function overlay() {
	el = document.getElementById("overlay");
	el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
}

function submitForm() {
	var prefix = document.getElementsByClassName('prefix')[0].value;
	var number = document.getElementsByClassName('number')[0].value;
	if (isNaN(number) == false) {
		search = prefix.toUpperCase() + '  ' + number;
		document.getElementById('tipue_search_input').value = '" ' + search + '"';
		document.getElementById('field').submit();
	}
	saveSelections();
}

function matchStart(term, text) {
	return text.toUpperCase().indexOf(term.toUpperCase()) == 0;
}