function run()
{
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
		    	var campus = data[i].location_descr;
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
		    	if(classStartTime.length == 0) classStartTime = 'TBD';
		    	if(classEndTime.length == 0) classEndTime = 'TBD';
		    	if(classStatus == 'C') classStatus = 'Closed';
		    	if(classStatus == 'O') classStatus = 'Open';
		    	if(classStatus == 'W') classStatus = 'Waitlist';
		    	
		    	html += '<tr>';
		    	if(readCookie((teacherFirstName + '-' + teacherLastName).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-add-' + classNumber) == 0)
		    	{
					html += '<td><input class="' + (teacherFirstName + '-' + teacherLastName).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-add"' + 'id="' + [shortUrl,classStatus,creditHours,teacherFirstName,teacherLastName,classStartTime,classEndTime,classSection,classNumber,campus,days] + '" type="image" src="../../../add.png" width="20" onclick="addToCart(this)"/>';
		    	}
		    	else
		    	{
		    		html += '<td><input class="' + (teacherFirstName + '-' + teacherLastName).toLowerCase().replace('\u00ED','i').split(' ').join('-') + '-add"' + 'id="' + ['WRD 103',classStatus,creditHours,teacherFirstName,teacherLastName,classStartTime,classEndTime,classSection,classNumber,campus,days] + '" type="image" src="../../../minus.png" width="20" onclick="removeFromCart(this)"/>';
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
					    				list_overall[j].innerHTML = '<a style="text-decoration:none;" href="../teachers/'+(first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-')+'">'+ overall + '</a>';
					    				list_firstn[j].innerHTML = '<a style="text-decoration:none;" href="../teachers/'+(first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-')+'">'+ first_name + '</a>';
					    				list_lastn[j].innerHTML = '<a style="text-decoration:none;" href="../teachers/'+(first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-')+'">'+ last_name + '</a>';
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
	    		useBackup();
	    	}
	    },
	    error: function()
	    {
		    useBackup();
		}
	});
}

function useBackup()
{
	$.ajax({
		url:'http://mocksched.com/schools/depaul-university/backupRankings.html',
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
				    				list_overall[j].innerHTML = '<a style="text-decoration:none;" href="../teachers/'+(first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-')+'">'+ overall + '</a>';
				    				list_firstn[j].innerHTML = '<a style="text-decoration:none;" href="../teachers/'+(first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-')+'">'+ first_name + '</a>';
				    				list_lastn[j].innerHTML = '<a style="text-decoration:none;" href="../teachers/'+(first_name + '-' + last_name).toLowerCase().replace('\u00ED','i').split(' ').join('-')+'">'+ last_name + '</a>';
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
	var search = prefix.toLowerCase() + '-credits=' + credit;
	document.getElementById('tipue_search_input').value = '"' + search + '"';
	document.getElementById('field').submit();
}

function updateCourseCartCount()
{
	var cookies = document.cookie;
	var count = 0;
	for (i of cookies.split(';'))
	{
		var cookie = i.split(',');
		if (cookie[0].indexOf('-add-') != -1)
		{
			count += 1;
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
	var value = contents.getAttribute('id');
	if(value.split(',').length < 12) index = 8;
	var className = contents.getAttribute('class').split(' ').join('-');
	var days = 1;
	writeCookie(className + '-' + value.split(',')[index],value,days);
	document.getElementById(value).src = "../../../minus.png";
	document.getElementById(value).onclick = function() {removeFromCart(contents);};
	updateCourseCartCount();
}

function removeFromCart(contents)
{
	var index = 9;
	var value = contents.getAttribute('id');
	if(value.split(',').length < 12) index = 8;
	var className = contents.getAttribute('class').split(' ').join('-');
	document.getElementById(value).src = "../../../add.png";
	document.getElementById(value).onclick = function() {addToCart(contents)};
	delete_cookie(className + '-' + value.split(',')[index]);
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
}

function matchStart (term, text) 
{
	return text.toUpperCase().indexOf(term.toUpperCase()) == 0;
}