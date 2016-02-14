var defaultTerm = 'spring-2016';

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

function matchStart(term, text) {
	return text.toUpperCase().indexOf(term.toUpperCase()) == 0;
}

function saveSelections() {
	var prefix = document.getElementsByClassName('prefix')[0].value;
	var number = document.getElementsByClassName('number')[0].value;
	writeToLocal('depaul-university-standard-prefix', prefix);
	writeToLocal('depaul-university-standard-number', number);
}

function saveCreditPrefix() {
	var prefix = document.getElementsByClassName('credit-prefix')[0].value;
	writeToLocal('depaul-university-standard-prefix', prefix);
	writeToLocal('depaul-university-standard-number', '');
}

function readCreditSelections() {
	var prefix = readFromLocal('depaul-university-standard-prefix');
	if (prefix) {
		document.getElementsByClassName('credit-prefix')[0].value = prefix;
	}
}

function readSelections() {
	var prefix = readFromLocal('depaul-university-standard-prefix');
	var number = readFromLocal('depaul-university-standard-number');
	if (prefix) {
		document.getElementsByClassName('prefix')[0].value = prefix;
	}
	if (number) {
		document.getElementsByClassName('number')[0].value = number;
	}
}

function writeToLocal(name, value) {
    localStorage.setItem(name.trim(), value);
}

function readFromLocal(name) {
    if (localStorage.getItem(name.trim()))
        return localStorage.getItem(name.trim());;
    return '';
}

function creditSearch() {
	var prefix = document.getElementsByClassName('credit-prefix')[0].value;
	var credit = document.getElementsByClassName('credit-input')[0].value;
	if (isNaN(credit) == false && credit.trim().length > 0) {
		var search = prefix.toLowerCase() + '-credits=' + credit.trim();
		document.getElementById('tipue_search_input').value = '"' + search + '"';
		document.getElementById('field').submit();
		saveCreditPrefix();
	}
}

function updateCourseCartCount() {
	if (!readFromLocal('depaul-university-term')) {
		writeToLocal('depaul-university-term',defaultTerm);
	}
    var term = readFromLocal('depaul-university-term');
    var count = 0;
    for (var i = 0; i < localStorage.length; i++) {
        if (localStorage.key(i).indexOf('-add-') != -1) {
            if (localStorage.key(i).indexOf(term) != -1) {
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