import json

def create_page(full_name,description,course_url):
	html = '<!DOCTYPE html><html><head><title>'
	html += full_name
	html +='''</title>
					<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
					<script src="http://code.jquery.com/ui/1.9.2/jquery-ui.js"></script>
					<link rel="stylesheet" href="../../../css/stylesheet.css" type="text/css" media="print, projection, screen" />
					<script type="text/javascript" src="../../../js/jquery.tablesorter.min.js"></script>
					<link href="http://fonts.googleapis.com/css?family=Open+Sans:300,400|Merriweather:300,300italic" rel="stylesheet">
					<script>
						(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
						(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
						m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
						})(window,document,'script','http://www.google-analytics.com/analytics.js','ga');
						ga('create', 'UA-70030211-1', 'auto');
						ga('send', 'pageview');
					 </script>
				</head>
				<body id="body">
				<div class="right" class="inner"><h3><a href="../../../course-cart.html" style="text-decoration:none; color:#000">Course Cart</a></h3></div>
				<h1>'''

	html += full_name
	html +='</h1><h2>'
	html += description

	html += '</h2></body><script>'
	html += 'url = "https://crossorigin.me/{0}",'.format(course_url)
	html +='''$.ajax({
	    url:url,
	    type:'GET',
	    async: false,

	    success: function(response)
	    {
	    	data = jQuery.parseJSON(response);
	    	html = '<table id="myTable" class="tablesorter"><thead><tr>';

	    	headers = ['Add','Overall Rating','Class Status','Credit Hours', 'Teacher First Name', 'Teacher Last Name', 'Class Start Time', 'Class End Time', 'Class Section', 'Class Number', 'Location', 'Days'];

	    	for (i of headers)
	    	{
				html += '<th>' + i + '</th>';
	    	}
			html += ' </tr></thead><tbody>';
	    	for(i=0; i<data.length; i++)
	    	{
		    	classStatus = data[i].enrl_stat;
		    	creditHours = data[i].units_minimum;
		    	teacherFirstName = data[i].first_name;
		    	teacherLastName = data[i].last_name;
		    	classStartTime = data[i].meeting_time_start.replace('1/1/1900 ','').replace(':00 ',' ');
		    	classEndTime = data[i].meeting_time_end.replace('1/1/1900 ','').replace(':00 ',' ');
		    	classSection = data[i].class_section;
		    	classNumber = data[i].class_nbr;
		    	campus = data[i].location_descr;
		    	
		    	days = [undefined,undefined,undefined,undefined,undefined,undefined];
		    	if (data[i].mon.toLowerCase() == 'y') days[0] = 'M';
		    	if (data[i].tues.toLowerCase() == 'y') days[1] = 'Tu';
		    	if (data[i].wed.toLowerCase() == 'y') days[2] = 'W';
		    	if (data[i].thurs.toLowerCase() == 'y') days[3] = 'Th';
		    	if (data[i].fri.toLowerCase() == 'y') days[4] = 'F';
		    	if (data[i].sat.toLowerCase() == 'y') days[5] = 'Sat';
		    	days = days.join('');

		    	if (days.length == 0) days = '&nbsp;';
		    	if(teacherFirstName.length == 0) teacherFirstName = 'TBD';
		    	if(teacherLastName.length == 0) teacherLastName = 'TBD';
		    	if(classStartTime.length == 0) classStartTime = 'TBD';
		    	if(classEndTime.length == 0) classEndTime = 'TBD';
		    	if(classStatus == 'C') classStatus = 'Closed';
		    	if(classStatus == 'O') classStatus = 'Open';
		    	if(classStatus == 'W') classStatus = 'Waitlist';
		    	
		    	html += '<tr>'
		    	if(readCookie(teacherFirstName.toLowerCase()+'-'+teacherLastName.toLowerCase()+'-add'+[classStatus,creditHours,teacherFirstName,teacherLastName,classStartTime,classEndTime,classSection,classNumber,campus,days])==0)  
		    	{
		    		html += '<td><input class="'+teacherFirstName.toLowerCase()+'-'+teacherLastName.toLowerCase()+'-add"'+'id="'+[classStatus,creditHours,teacherFirstName,teacherLastName,classStartTime,classEndTime,classSection,classNumber,campus,days]+'" type="image" src="../../../add.png" width="20" onclick="addToCart(this)"/>'
		    	}
		    	else
		    	{
		    		html += '<td><input class="'+teacherFirstName.toLowerCase()+'-'+teacherLastName.toLowerCase()+'-add"'+'id="'+[classStatus,creditHours,teacherFirstName,teacherLastName,classStartTime,classEndTime,classSection,classNumber,campus,days]+'" type="image" src="../../../minus.png" width="20" onclick="removeFromCart(this)"/>'
		    	}
		    	html += '<td class="'+teacherFirstName.toLowerCase()+'-'+teacherLastName.toLowerCase()+'-overall">0.0</td>'
		    	html += '<td class="'+teacherFirstName.toLowerCase()+'-'+teacherLastName.toLowerCase()+'-status">'+classStatus+'</td>'
		    	html += '<td class="'+teacherFirstName.toLowerCase()+'-'+teacherLastName.toLowerCase()+'-credits">'+creditHours+'</td>'
		    	html += '<td class="'+teacherFirstName.toLowerCase()+'-'+teacherLastName.toLowerCase()+'-firstn">'+teacherFirstName+'</td>'
		    	html += '<td class="'+teacherFirstName.toLowerCase()+'-'+teacherLastName.toLowerCase()+'-lastn">'+teacherLastName+'</td>'
		    	html += '<td class="'+teacherFirstName.toLowerCase()+'-'+teacherLastName.toLowerCase()+'-start">'+classStartTime+'</td>'
		    	html += '<td class="'+teacherFirstName.toLowerCase()+'-'+teacherLastName.toLowerCase()+'-end">'+classEndTime+'</td>'
		    	html += '<td class="'+teacherFirstName.toLowerCase()+'-'+teacherLastName.toLowerCase()+'-section">'+classSection+'</td>'
		    	html += '<td class="'+teacherFirstName.toLowerCase()+'-'+teacherLastName.toLowerCase()+'-number">'+classNumber+'</td>'
		    	html += '<td class="'+teacherFirstName.toLowerCase()+'-'+teacherLastName.toLowerCase()+'-campus">'+campus+'</td>'
		    	html += '<td class="'+teacherFirstName.toLowerCase()+'-'+teacherLastName.toLowerCase()+'-days">'+days+'</td>'
		    	html += '</tr>';

		    }
		    html += '</tbody></table>';
		    html += '<div class="center ital" style="padding-top: 1%;">This data is live.</a></div>';
		    html += '<div class="center ital" style="padding-top: .5%;">Contact the <a href="mailto:tjgambs@gmail.com?subject=MockSched">Developer</a></div>';
		    
		    document.getElementById('body').innerHTML += html;
	    }
	});

	$.ajax({
		url:'https://crossorigin.me/http://search.mtvnservices.com/typeahead/suggest/?solrformat=true&rows=10&callback=jQuery111003276446736417711_1446762506495&q=*%3A*+AND+schoolid_s%3A1389&defType=edismax&qf=teacherfullname_t%5E1000+autosuggest&bf=pow(total_number_of_ratings_i%2C2.1)&sort=&siteName=rmp&rows=1000000000&start=0&fl=teacherfirstname_t+teacherlastname_t+averageratingscore_rf',
		type:'GET',
		async: false,
		
		success: function(response)
	    {
	    	begin = response.indexOf('"docs":') + 7;
	    	end = response.length - 150;
	    	data = jQuery.parseJSON(response.substr(begin,end));

	    	for (i of data)
	    	{
	    		overall = i.averageratingscore_rf;
	    		first_name = i.teacherfirstname_t;
	    		last_name = i.teacherlastname_t;
	    		var list_overall = document.getElementsByClassName(first_name.toLowerCase() + '-' + last_name.toLowerCase() + '-overall')
	    		var list_firstn = document.getElementsByClassName(first_name.toLowerCase() + '-' + last_name.toLowerCase() + '-firstn')
	    		var list_lastn = document.getElementsByClassName(first_name.toLowerCase() + '-' + last_name.toLowerCase() + '-lastn')
	    		var list_cookie = document.getElementsByClassName(first_name.toLowerCase() + '-' + last_name.toLowerCase() + '-add')
	    		if(list_overall.length != 0)
	    		{
	    			for(var i = 0; i<list_overall.length; i++)
	    			{
	    				list_overall[i].innerHTML = '<a style="text-decoration:none;" href="../teachers/'+first_name.toLowerCase()+'-'+last_name.toLowerCase()+'.html">'+ overall + '</a>'
	    				list_firstn[i].innerHTML = '<a style="text-decoration:none;" href="../teachers/'+first_name.toLowerCase()+'-'+last_name.toLowerCase()+'.html">'+ first_name + '</a>'
	    				list_lastn[i].innerHTML = '<a style="text-decoration:none;" href="../teachers/'+first_name.toLowerCase()+'-'+last_name.toLowerCase()+'.html">'+ last_name + '</a>'
	    				list_cookie[i].id = overall+',' + list_cookie[i].id
	    			}
	    		}
	    	}
	    }
	});

  	$("#myTable").tablesorter({sortInitialOrder: 'desc'});

	function addToCart(contents)
	{
		value = contents.getAttribute('id')
		className = contents.getAttribute('class')
		days = 1

		writeCookie(className+value,value,days)
		document.getElementById(value).src = "../../../minus.png"
		document.getElementById(value).onclick = function() {removeFromCart(contents);};
		
	}

	function removeFromCart(contents)
	{
		value = contents.getAttribute('id')
		className = contents.getAttribute('class')
		document.getElementById(value).src = "../../../add.png"
		document.getElementById(value).onclick = function() {addToCart(contents)};
		delete_cookie(className+value)
		
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
  		document.cookie = name +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
	}


</script>
</html>'''

	webpage_name = ('classes/'+'-'.join(full_name.split()[:2]).replace(';','').lower()+'.html')
	with open('../'+webpage_name,'w') as output:
			output.write(html)
	return [full_name,description,'schools/depaul/classes/'+'-'.join(full_name.split()[:2]).replace(';','').lower()+'.html']

def create_all():
	with open('../classes.json','r') as input:
		data = json.loads(input.read())
		to_be_indexed = []
		for i in data: 
			to_be_indexed.append(create_page(i[0],i[1],i[2]))
		send_to_be_indexed(to_be_indexed)

def send_to_be_indexed(items):
	with open('../tipuesearch/tipuesearch_content.js','w') as output:
		output.write('var tipuesearch = {"pages": [\n')
		for i in items:
			title = '""'
			text = '""'
			tags ='""'
			url = '""'

			if i[0]:
				title = clean_index(i[0])
			if i[1]:
				text = clean_index(i[1])
			if i[2]:
				url = clean_index(i[2])

			output.write('{"title":'+ title +',"text":'+ text +',"tags":'+ tags +',"url": '+url+'},\n')
		output.write(']};')

def clean_index(item):
	return '"{0}"'.format(item.replace("\"",'').replace("\r\n",'').replace("\n",''))

if __name__ == '__main__':
	create_all()

