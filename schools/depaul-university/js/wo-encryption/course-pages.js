function hasNumber(myString) 
{
	return (/\d/.test(myString));
}

function prereqCourses()
{
	var description = document.getElementById('description').innerHTML;
	if(description.toUpperCase().indexOf('REQUISITE') == -1) return;
	var splitDescr = description.substr(description.toUpperCase().indexOf('REQUISITE')+9).split('(').join('').split(')').join('').split('.').join('').split(':').join('').split(',').join('').split(' ');
	console.log(splitDescr)
	var courses = [];
	var flags = [];
	var tempPrefix = '';
	for(var i = 1; i < splitDescr.length; i++)
	{
		if(!isNaN(Number(splitDescr[i])))
		{
			var number = splitDescr[i];
			var prefix = splitDescr[i-1];
			if(prefix == 'or')
			{
				courses.push(tempPrefix + ' ' + number);
				flags.push(false);
			}
			else
			{
				tempPrefix = prefix;
				courses.push(prefix + ' ' + number);
				flags.push(true);
			}
		}
		else if(hasNumber(splitDescr[i]))
		{
			var number = splitDescr[i].substr(-3);
			var prefix = splitDescr[i].replace(number,'');
			if(prefix == 'or')
			{
				courses.push(tempPrefix + ' ' + number);
				flags.push(false);
			}
			else
			{
				tempPrefix = prefix;
				courses.push(prefix + ' ' + number);
				flags.push(true);
			}
		}
	}
	document.getElementById('description').innerHTML = addLinks(description,courses,flags);
}

function addLinks(description,courses,flags)
{
	for(var j = 0; j < courses.length; j++)
	{
		if(courses[j].split(' ')[1][0] == '0')
		{
			if(urlExists((courses[j].split(' ')[0] + '-' + courses[j].split(' ')[1].substr(1)).toLowerCase()))
			{
				if(courses[j] && !flags[j])
				{
					description = description.substr(0,description.indexOf('TE(S)')+4) + description.substr(description.indexOf('TE(S)')+4).split(courses[j].split(' ')[1]).join('<a style="text-decoration: none;"href="' + (courses[j].split(' ')[0] + '-' + courses[j].split(' ')[1]).toLowerCase() + '">' + courses[j].split(' ')[1] + '</a>');
				}
				else if(courses[j] && courses[j].length < 10)
				{
					description = description.substr(0,description.indexOf('TE(S)')+4) + description.substr(description.indexOf('TE(S)')+4).split(courses[j]).join('<a style="text-decoration: none;"href="' + (courses[j].split(' ')[0] + '-' + courses[j].split(' ')[1].substr(1)).toLowerCase() + '">' + courses[j] + '</a>');
					description = description.substr(0,description.indexOf('TE(S)')+4) + description.substr(description.indexOf('TE(S)')+4).split(courses[j].replace(' ','')).join('<a style="text-decoration: none;"href="' + (courses[j].split(' ')[0] + '-' + courses[j].split(' ')[1].substr(1)).toLowerCase() + '">' + courses[j].replace(' ','') + '</a>');
				}
			}
		}
		else
		{
			if(urlExists(courses[j].replace(' ','-').toLowerCase()))
			{
				if(courses[j] && !flags[j])
				{
					description = description.substr(0,description.indexOf('TE(S)')+4) + description.substr(description.indexOf('TE(S)')+4).split(courses[j].split(' ')[1]).join('<a style="text-decoration: none;"href="' + (courses[j].split(' ')[0] + '-' + courses[j].split(' ')[1]).toLowerCase() + '">' + courses[j].split(' ')[1] + '</a>');
				}
				else if(courses[j] && courses[j].length < 10)
				{
					description = description.substr(0,description.indexOf('TE(S)')+4) + description.substr(description.indexOf('TE(S)')+4).split(courses[j]).join('<a style="text-decoration: none;"href="' + courses[j].replace(' ','-').toLowerCase() + '">' + courses[j] + '</a>');
					description = description.substr(0,description.indexOf('TE(S)')+4) + description.substr(description.indexOf('TE(S)')+4).split(courses[j].replace(' ','')).join('<a style="text-decoration: none;"href="' + courses[j].replace(' ','-').toLowerCase() + '">' + courses[j].replace(' ','') + '</a>');
				}
			}
		}
	}
	return description;
}

function urlExists(url)
{
    var http = new XMLHttpRequest();
    http.open('HEAD', url, false);
    http.send();
    return http.status != 404;
}

function saveSelections()
{
	var prefix = document.getElementsByClassName('prefix')[0].value;
	var number = document.getElementsByClassName('number')[0].value;
	writeCookie('depaul-university-standard-prefix',prefix);
	writeCookie('depaul-university-standard-number',number);
}

function saveCreditPrefix()
{
	var prefix = document.getElementsByClassName('credit-prefix')[0].value;
	writeCookie('depaul-university-standard-prefix',prefix);
	writeCookie('depaul-university-standard-number','');
}

function readCreditSelections()
{
	var prefix = readCookie('depaul-university-standard-prefix');
	if(prefix)
	{
		document.getElementsByClassName('credit-prefix')[0].value = prefix;
	}
}

function readSelections()
{
	var prefix = readCookie('depaul-university-standard-prefix');
	var number = readCookie('depaul-university-standard-number');
	if(prefix)
	{
		document.getElementsByClassName('prefix')[0].value = prefix;
	}
	if(number)
	{
		document.getElementsByClassName('number')[0].value = number;
	}
}

function run()
{
	prereqCourses();
	readSelections();
	readCreditSelections();
	$.fn.select2.amd.require(['select2/compat/matcher'], function (oldMatcher) 
	{
		$("select").select2({
	    	matcher: oldMatcher(matchStart)
	    })
	});

	$(".number").keyup(function (e) 
	{
	    if (e.keyCode == 13) 
	    {
	        submitForm();
	    }
	});

	$(".credit-input").keyup(function (e) 
	{
	    if (e.keyCode == 13) 
	    {
	        creditSearch();
	    }
	});

	$('#overlay').mousedown(function(e) 
	{
		var clicked = $(e.target);
		if (clicked.is('#advanced-container') || clicked.parents().is('#advanced-container')) 
		{
			return;
    	} 
    	else 
    	{ 
    		el = document.getElementById("overlay");
			el.style.visibility = (el.style.visibility == "hidden") ? "visible" : "hidden";
    	}
	});

	$('#help').mousedown(function(e) 
	{
		var clicked = $(e.target);
		if (clicked.is('#help-container') || clicked.parents().is('#help-container')) 
		{
			return;
    	} 
    	else 
    	{ 
    		el = document.getElementById("help");
			el.style.visibility = (el.style.visibility == "hidden") ? "visible" : "hidden";
    	}
	});

	if ("onhashchange" in window) 
	{
    	saveSelections();
	}
}

function updateTable(url,shortUrl)
{
	$.ajax({
	    url:url,
	    type:'GET',
	    async: false,
	    success: function(response)
	    {
	    	var data = jQuery.parseJSON(response);
	    	var term = readCookie('depaul-university-term');
	    	var html = '<table id="myTable" class="tablesorter"><thead><tr>';
	    	var headers = ['Add','Overall Rating','Class Status','Credit Hours', 'Teacher First Name', 'Teacher Last Name', 'Class Start Time', 'Class End Time', 'Class Section', 'Class Number', 'Location', 'Days'];
	    	for (i of headers)
	    	{
				html += '<th>' + i + '</th>';
	    	}
			html += '</tr></thead><tbody>';
	    	for(i = 0; i < data.length; i++)
	    	{
		    	var classStatus = data[i].enrl_stat;
		    	var creditHours = data[i].units_minimum;
		    	var teacherFirstName = data[i].first_name;
		    	var teacherLastName = data[i].last_name;
		    	var classStartTime = data[i].meeting_time_start.replace('1/1/1900 ','').replace(':00 ',' ');
		    	var classEndTime = data[i].meeting_time_end.replace('1/1/1900 ','').replace(':00 ',' ');
		    	var classSection = data[i].class_section;
		    	var classNumber = data[i].class_nbr;
		    	if(data[i].facility_descrshort)
		    	{
		    		var campus = data[i].location_descr + ' - ' + data[i].facility_descrshort;
		    	}
		    	else
		    	{
		    		var campus = data[i].location_descr;
		    	}
		    	var days = [undefined,undefined,undefined,undefined,undefined,undefined];

		    	if(data[i].mon.toLowerCase() == 'y') days[0] = 'M';
		    	if(data[i].tues.toLowerCase() == 'y') days[1] = 'Tu';
		    	if(data[i].wed.toLowerCase() == 'y') days[2] = 'W';
		    	if(data[i].thurs.toLowerCase() == 'y') days[3] = 'Th';
		    	if(data[i].fri.toLowerCase() == 'y') days[4] = 'F';
		    	if(data[i].sat.toLowerCase() == 'y') days[5] = 'Sat';
		    	days = days.join('');

		    	if(days.length == 0) days = 'OnLine';
		    	if(teacherFirstName.length == 0) teacherFirstName = 'TBD';
		    	if(teacherLastName.length == 0) teacherLastName = 'TBD';
		    	if(days.toUpperCase() == 'ONLINE')
		    	{
			    	if(classStartTime.length == 0) classStartTime = 'OnLine';
			    	if(classEndTime.length == 0) classEndTime = 'OnLine';
			    }
			    else
			    {
			    	if(classStartTime.length == 0) classStartTime = 'TBD';
			    	if(classEndTime.length == 0) classEndTime = 'TBD';
			    }

		    	if(classStatus == 'C') classStatus = 'Closed';
		    	if(classStatus == 'O') classStatus = 'Open';
		    	if(classStatus == 'W') classStatus = 'Waitlist';
		    	
		    	html += '<tr>';
		    	if(readCookie('depaul-university-(' + term + ')-' + (teacherFirstName + '-' + teacherLastName).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-add-' + classNumber) == 0)
		    	{
					html += '<td><input class="' + (teacherFirstName + '-' + teacherLastName).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-add"' + 'id="' + [shortUrl,classStatus,creditHours,teacherFirstName,teacherLastName,classStartTime,classEndTime,classSection,classNumber,campus,days] + '" type="image" src="../../../../../add.png" width="20" onclick="addToCart(this)"/>';
		    	}
		    	else
		    	{
		    		html += '<td><input class="' + (teacherFirstName + '-' + teacherLastName).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-add"' + 'id="' + ['WRD 103',classStatus,creditHours,teacherFirstName,teacherLastName,classStartTime,classEndTime,classSection,classNumber,campus,days] + '" type="image" src="../../../../../minus.png" width="20" onclick="removeFromCart(this)"/>';
		    	}
		    	html += '<td class="'+(teacherFirstName+'-'+teacherLastName).toLowerCase().replace('\u00ED','i').split(' ').join('-')+'-overall">0.0</td>';
		    	if(classStatus == 'Closed')
		    	{
		    		html += '<td style="color:red;" class="' + (teacherFirstName + '-' + teacherLastName).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-status">' + classStatus+'</td>';
		    	}
		    	else
		    	{
		    		html += '<td style="color:green;" class="' + (teacherFirstName + '-' + teacherLastName).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-status">' + classStatus+'</td>';
		    	}
		    	html += '<td class="' + (teacherFirstName + '-' + teacherLastName).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-credits">' + creditHours + '</td>';
		    	html += '<td class="' + (teacherFirstName + '-' + teacherLastName).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-firstn">' + teacherFirstName + '</td>';
		    	html += '<td class="' + (teacherFirstName + '-' + teacherLastName).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-lastn">' + teacherLastName + '</td>';
		    	html += '<td class="' + (teacherFirstName + '-' + teacherLastName).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-start">' + classStartTime + '</td>';
		    	html += '<td class="' + (teacherFirstName + '-' + teacherLastName).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-end">' + classEndTime + '</td>';
		    	html += '<td class="' + (teacherFirstName + '-' + teacherLastName).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-section">' + classSection + '</td>';
		    	html += '<td class="' + (teacherFirstName + '-' + teacherLastName).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-number">' + classNumber + '</td>';
		    	html += '<td class="' + (teacherFirstName + '-' + teacherLastName).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-campus">' + campus + '</td>';
		    	html += '<td class="' + (teacherFirstName + '-' + teacherLastName).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-days">' + days + '</td>';
		    	html += '</tr>';

		    }
		    html += '</tbody></table>';
		    html += '<div class="center ital" style="padding-top: 1%;">Ratings credited to <a href="http://www.ratemyprofessors.com" target="_blank">Rate My Professors.</a> Courses credited to <a href="http://depaul.edu" target="_blank">DePaul University.</a></div>';
		    html += '<div class="center ital" style="padding-top: .5%;">Contact the <a href="mailto:mocksched@gmail.com?subject=MockSched">Developer</a></div>';
		    document.getElementById('body').innerHTML += html;
	    }
	});
}

function updateRanking()
{
	$.ajax({
		url:'https://crossorigin.me/http://search.mtvnservices.com/typeahead/suggest/?solrformat=true&rows=10&callback=jQuery111003276446736417711_1446762506495&q=*%3A*+AND+schoolid_s%3A1389&defType=edismax&qf=teacherfullname_t%5E1000+autosuggest&bf=pow(total_number_of_ratings_i%2C2.1)&sort=&siteName=rmp&rows=1000000000&start=0&fl=pk_id+teacherfirstname_t+teacherlastname_t+averageratingscore_rf',
		type:'GET',
		async: false,
		success: function(response)
	    {
	    	try
	    	{
		    	var begin = response.indexOf('"docs":') + 7;
		    	var end = response.length - 151;
		    	var data = jQuery.parseJSON(response.substr(begin,end));
		    	for (i of data)
		    	{
			    	var overall = i.averageratingscore_rf;
			    	var first_name = i.teacherfirstname_t.replace('\u00ED','i');
			    	var last_name = i.teacherlastname_t.replace('\u00ED','i');
			    	var list_overall = document.getElementsByClassName((first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-overall');
			    	var list_firstn = document.getElementsByClassName((first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-firstn');
			    	var list_lastn = document.getElementsByClassName((first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-lastn');
			    	var list_cookie = document.getElementsByClassName((first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-add');
			    	if(list_overall.length != 0)
			    	{
			    		for(var j = 0; j<list_overall.length; j++)
			    		{
			    			if(overall)
			    			{
			    				if (overall.length != 0 && overall != '0' && overall != '0.0')
			    				{
			    					if(list_overall[j].innerHTML.indexOf('<a style') == -1)
			    					{
					    				list_overall[j].innerHTML = '<a style="text-decoration:none;" href="../../../teachers/'+(first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-')+'">'+ overall + '</a>';
					    				list_firstn[j].innerHTML = '<a style="text-decoration:none;" href="../../../teachers/'+(first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-')+'">'+ first_name + '</a>';
					    				list_lastn[j].innerHTML = '<a style="text-decoration:none;" href="../../../teachers/'+(first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-')+'">'+ last_name + '</a>';
					    				list_cookie[j].id = overall+',' + list_cookie[j].id;
				    				}
			    				}
			    			}
			    		}
			    	}
		    	}
	    	}
	    	catch(e)
	    	{
	    		useBackup('http://mocksched.com/schools/depaul-university/backupRankings0.html');
	    	}
	    },
	    error: function()
	    {
		    useBackup('http://mocksched.com/schools/depaul-university/backupRankings0.html');
		}
	});
	$.ajax({
		url:'https://crossorigin.me/http://search.mtvnservices.com/typeahead/suggest/?solrformat=true&rows=10&callback=jQuery1110022448566812090576_1450841735528&q=*%3A*+AND+schoolid_s%3A5485&defType=edismax&qf=teacherfullname_t%5E1000+autosuggest&bf=pow(total_number_of_ratings_i%2C2.1)&sort=&siteName=rmp&rows=1000000000&start=0&fl=pk_id+teacherfirstname_t+teacherlastname_t+averageratingscore_rf',
		type:'GET',
		async: false,
		success: function(response)
	    {
	    	try
	    	{
		    	var begin = response.indexOf('"docs":') + 7;
		    	var end = response.length - 151;
		    	var data = jQuery.parseJSON(response.substr(begin,end));
		    	for (i of data)
		    	{
			    	var overall = i.averageratingscore_rf;
			    	var first_name = i.teacherfirstname_t.replace('\u00ED','i');
			    	var last_name = i.teacherlastname_t.replace('\u00ED','i');
			    	var list_overall = document.getElementsByClassName((first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-overall');
			    	var list_firstn = document.getElementsByClassName((first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-firstn');
			    	var list_lastn = document.getElementsByClassName((first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-lastn');
			    	var list_cookie = document.getElementsByClassName((first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-add');
			    	if(list_overall.length != 0)
			    	{
			    		for(var j = 0; j<list_overall.length; j++)
			    		{
			    			if(overall)
			    			{
			    				if (overall.length != 0 && overall != '0' && overall != '0.0')
			    				{
			    					if(list_overall[j].innerHTML.indexOf('<a style') == -1)
			    					{
					    				list_overall[j].innerHTML = '<a style="text-decoration:none;" href="../../../teachers/'+(first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-')+'">'+ overall + '</a>';
					    				list_firstn[j].innerHTML = '<a style="text-decoration:none;" href="../../../teachers/'+(first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-')+'">'+ first_name + '</a>';
					    				list_lastn[j].innerHTML = '<a style="text-decoration:none;" href="../../../teachers/'+(first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-')+'">'+ last_name + '</a>';
					    				list_cookie[j].id = overall+',' + list_cookie[j].id;
				    				}
			    				}
			    			}
			    		}
			    	}
		    	}
	    	}
	    	catch(e)
	    	{
	    		useBackup('http://mocksched.com/schools/depaul-university/backupRankings1.html');
	    	}
	    },
	    error: function()
	    {
		    useBackup('http://mocksched.com/schools/depaul-university/backupRankings1.html');
		}
	});	
}

function useBackup(url)
{
	$.ajax({
		url:url,
		type:'GET',
		async: false,
		success: function(response)
	    {
	    	var begin = response.indexOf('"docs":') + 7;
	    	var end = response.length - 151;
	    	var data = jQuery.parseJSON(response.substr(begin,end));
	    	for (i of data)
	    	{
		    	var overall = i.averageratingscore_rf;
		    	var first_name = i.teacherfirstname_t.replace('\u00ED','i');
		    	var last_name = i.teacherlastname_t.replace('\u00ED','i');
		    	var list_overall = document.getElementsByClassName((first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-overall');
		    	var list_firstn = document.getElementsByClassName((first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-firstn');
		    	var list_lastn = document.getElementsByClassName((first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-lastn');
		    	var list_cookie = document.getElementsByClassName((first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-add');
		    	if(list_overall.length != 0)
		    	{
		    		for(var j = 0; j<list_overall.length; j++)
		    		{
		    			if(overall)
		    			{
		    				if (overall.length != 0 && overall != '0' && overall != '0.0')
		    				{
		    					if(list_overall[j].innerHTML.indexOf('<a style') == -1)
		    					{
				    				list_overall[j].innerHTML = '<a style="text-decoration:none;" href="../../../teachers/'+(first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-')+'">'+ overall + '</a>';
				    				list_firstn[j].innerHTML = '<a style="text-decoration:none;" href="../../../teachers/'+(first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-')+'">'+ first_name + '</a>';
				    				list_lastn[j].innerHTML = '<a style="text-decoration:none;" href="../../../teachers/'+(first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-')+'">'+ last_name + '</a>';
				    				list_cookie[j].id = overall+',' + list_cookie[j].id;
			    				}
		    				}
		    			}
		    		}
		    	}
	    	}
	    }
	});
}

function creditSearch()
{
	var prefix = document.getElementsByClassName('credit-prefix')[0].value;
	var credit = document.getElementsByClassName('credit-input')[0].value;
	if(isNaN(credit) == false)
	{
		var search = prefix.toLowerCase() + '-credits=' + credit;
		document.getElementById('tipue_search_input').value = '"' + search + '"';
		document.getElementById('field').submit();
		saveCreditPrefix();
	}
}

function updateCourseCartCount()
{
	var term = window.location.href.split('/').slice(-3,-2)[0];
	if(readCookie('depaul-university-term') != term) writeCookie('depaul-university-term',term,1);
	var cookies = document.cookie;
	var count = 0;
	for (i of cookies.split(';'))
	{
		var cookie = i.split(',');
		if (cookie[0].indexOf('-add-') != -1)
		{
			if(cookie[0].indexOf(term) != -1)
			{
				count += 1;
			}
		}
	}
	document.getElementById('course-cart').innerHTML = 'Course Cart (' + count + ')';
}

function help() 
{
	el = document.getElementById("help");
	el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
}

function overlay() 
{
	el = document.getElementById("overlay");
	el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
}

function addToCart(contents)
{
	var index = 9;
	var term = readCookie('depaul-university-term');
	var value = contents.getAttribute('id');
	if(value.split(',').length < 12) index = 8;
	var className = contents.getAttribute('class').split(' ').join('-');
	var days = 1;
	writeCookie('depaul-university-(' + term + ')-' + className + '-' + value.split(',')[index],value,days);
	document.getElementById(value).src = "../../../../../minus.png";
	document.getElementById(value).onclick = function() {removeFromCart(contents);};
	updateCourseCartCount();
}

function removeFromCart(contents)
{
	var term = window.location.href.split('/').slice(-3,-2)[0];
	if(readCookie('depaul-university-term') != term) writeCookie('depaul-university-term',term,1);
	var index = 9;
	var value = contents.getAttribute('id');
	if(value.split(',').length < 12) index = 8;
	var className = contents.getAttribute('class').split(' ').join('-');
	document.getElementById(value).src = "../../../../../add.png";
	document.getElementById(value).onclick = function() {addToCart(contents)};
	delete_cookie('depaul-university-(' + term + ')-' + className + '-' + value.split(',')[index]);
	updateCourseCartCount();
}

function writeCookie(name,value,days) 
{
    var date, expires;
    if (days) 
    {
        date = new Date();
        date.setTime(date.getTime()+(days*24*60*60*1000));
        expires = "; expires=" + date.toGMTString();
    }
    else
    {
        expires = "";
    }
    document.cookie = name + "=" + value + expires + "; path=/";
}

function readCookie(name) 
{
	var i, c, ca, nameEQ = name + "=";
	ca = document.cookie.split(';');
	for(i=0;i < ca.length;i++) 
	{
   		c = ca[i];
    	while (c.charAt(0)==' ') 
    	{
        	c = c.substring(1,c.length);
    	}
        if (c.indexOf(nameEQ) == 0) 
        {
            return c.substring(nameEQ.length,c.length);
        }
	}
	return '';
}

function delete_cookie(name) 
{
	document.cookie = name + '=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}

function submitForm()
{
	var prefix = document.getElementsByClassName('prefix')[0].value;
	var number = document.getElementsByClassName('number')[0].value;
	if(isNaN(number) == false)
	{
		search = prefix.toUpperCase() + '  ' + number;
		document.getElementById('tipue_search_input').value = '"' + search + '"';
		document.getElementById('field').submit();
	}
	saveSelections();
}

function matchStart (term, text) 
{
	return text.toUpperCase().indexOf(term.toUpperCase()) == 0;
}