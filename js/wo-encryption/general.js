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
	$(".number").keyup(function(e) {
		if (e.keyCode == 13) {
			submitForm();
		}
	});
	$(".credit-input").keyup(function(e) {
		if (e.keyCode == 13) {
			creditSearch();
		}
	});

	if ("onhashchange" in window) {
		saveSelections();
	}
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

function updateTermSearch(flag) {
	var term = document.getElementsByClassName('term')[0].value;
	if (document.getElementsByClassName('term-content')[0]) {
		$('.term-content').remove();
	}
	if (document.getElementsByClassName('tipue-search')[0]) {
		$('.tipue-search').remove();
	}
	if (flag) {
		writeToLocal('depaul-university-term', term);
	}
	var content = document.createElement('script');
	var code = document.createElement('script');
	content.className = 'term-content';
	code.className = 'tipue-search';
	content.src = 'terms/' + term + '/tipuesearch/tipuesearch_content.js';
	code.src = '../../js/tipuesearch.min.js';
	$("head").append(content);
	$("head").append(code);
	updateCourseCartCount();
}

function updateTermIndex() {
	var term = document.getElementsByClassName('term')[0].value;
	writeToLocal('depaul-university-term', term);
	updateCourseCartCount();
}

function matchStart(term, text) {
	return text.toUpperCase().indexOf(term.toUpperCase()) == 0
}

function submitForm() {
	var prefix = document.getElementsByClassName('prefix')[0].value;
	var number = document.getElementsByClassName('number')[0].value;
	if (isNaN(number) == false) {
		var search = prefix.toUpperCase() + '  ' + number;
		document.getElementById('tipue_search_input').value = '" ' + search + '"';
		document.getElementById('field').submit();
	}
	saveSelections();
}

function overlay() {
	el = document.getElementById("overlay");
	el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
}

function help() {
	el = document.getElementById("help");
	el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
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

function learningDomainSearch() {
	var domain = document.getElementsByClassName('learning-domain-prefix')[0].value;
	var search = 'lsld=' + domain;
	document.getElementById('tipue_search_input').value = '"' + search + '"';
	document.getElementById('field').submit();
}

function updateCourseCartCount() {
    var term = document.getElementsByClassName('term')[0].value;
    var count = 0;
    for (var i = 0; i < localStorage.length; i++) {
        if (localStorage.key(i) && localStorage.key(i).indexOf('-add-') != -1) {
            if (localStorage.key(i).indexOf(term) != -1) {
                count += 1;
            }
        }
    }
    document.getElementById('course-cart').innerHTML = 'Course Cart (' + count + ')';
}

function writeToLocal(name, value) {
    localStorage.setItem(name.trim(), value);
}

function readFromLocal(name) {
    if (localStorage.getItem(name.trim()))
        return localStorage.getItem(name.trim());;
    return '';
}

function deleteFromLocal(name) {
    localStorage.removeItem(name.split('=')[0].trim());
}