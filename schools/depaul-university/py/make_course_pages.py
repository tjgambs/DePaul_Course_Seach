import json

def create_page(full_name,description,course_url):
	short_url = ' '.join(full_name.split()[:2]).replace(';','')
	html = '<!DOCTYPE html><html><head><title>'
	html += full_name.replace(';','')
	html +='''</title>
	<meta charset="UTF-8">
	<script src="../../../js/jquery.min.js"></script>
	<script src="../../../js/select2.full.js"></script>

    <link href="../../../css/select2.css" rel="stylesheet"/>
	<link rel="stylesheet" href="../../../css/stylesheet.css" type="text/css" media="print, projection, screen" />
	<script type="text/javascript" src="../../../js/jquery.tablesorter.min.js"></script>
	<link href="http://fonts.googleapis.com/css?family=Open+Sans:300,400|Merriweather:300,300italic" rel="stylesheet">
	<link rel="shortcut icon" href="../../../icon.png">
    <link rel="stylesheet" id="tipue3" type="text/css" href="../../../css/tipuesearch.css">
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
<div>
	<span><h3><a href="../course-cart.html" style="text-decoration:none; float:right; color:#333;">Course Cart</a></h3></span>
	<span>
		<h1 style="float:left; padding: 0px; padding-right:2%;"><a href="../search.html" style="text-decoration:none; color:#333;">MockSched</a></h1>
		<div style="display: inline-block; padding-right:10px">
			<select class="prefix">
				<option value="ACC">ACC - Accountancy</option>
				<option value="A&amp;S">A&amp;S - Administration &amp; Supervision</option>
				<option value="ABD">ABD - African&amp;Black Diaspora Studies</option>
				<option value="AHT">AHT - Allied Health Technology</option>
				<option value="ASL">ASL - American Sign Language</option>
				<option value="AMS">AMS - American Studies</option>
				<option value="ANI">ANI - Animation</option>
				<option value="ANT">ANT - Anthropology</option>
				<option value="APB">APB - Applied Brass</option>
				<option value="APK">APK - Applied Keyboard</option>
				<option value="APM">APM - Applied Music</option>
				<option value="APP">APP - Applied Percussion</option>
				<option value="AP">AP - Applied Professional Studies</option>
				<option value="APS">APS - Applied Strings</option>
				<option value="AT">AT - Applied Technology</option>
				<option value="APV">APV - Applied Voice</option>
				<option value="APW">APW - Applied Woodwinds</option>
				<option value="ARB">ARB - Arabic</option>
				<option value="ART">ART - Art</option>
				<option value="HAA">HAA - Art And Architecture, History Of</option>
				<option value="AI">AI - Arts And Ideas</option>
				<option value="BBE">BBE - Bilingual-Bicultural Education</option>
				<option value="BIO">BIO - Biological Sciences</option>
				<option value="BLW">BLW - Business Law</option>
				<option value="CTH">CTH - Catholic Studies</option>
				<option value="CTU">CTU - Catholic Theological Union</option>
				<option value="CHE">CHE - Chemistry</option>
				<option value="CHN">CHN - Chinese</option>
				<option value="CMN">CMN - Communication</option>
				<option value="CMNS">CMNS - Communication Studies</option>
				<option value="CSS">CSS - Community Service Studies</option>
				<option value="CPL">CPL - Comparative Literature</option>
				<option value="COM">COM - Composition</option>
				<option value="GPH">GPH - Computer Graphics &amp; Motion Technology</option>
				<option value="CSC">CSC - Computer Science</option>
				<option value="CNS">CNS - Computer, Information And Network Security</option>
				<option value="CCA">CCA - Core Curriculum Arts And Ideas</option>
				<option value="CCH">CCH - Core Curriculum Human Community</option>
				<option value="CCS">CCS - Core Curriculum Scientific World</option>
				<option value="CSL">CSL - Counseling</option>
				<option value="CES">CES - Critical Ethnic Studies</option>
				<option value="CS">CS - Curriculum Studies</option>
				<option value="DA">DA - Decision Analytics</option>
				<option value="DES">DES - Design</option>
				<option value="DC">DC - Digital Cinema</option>
				<option value="DHS">DHS - Digital Humanities</option>
				<option value="DMA">DMA - Digital Media Arts</option>
				<option value="ECE">ECE - Early Childhood Education</option>
				<option value="ECT">ECT - E-Commerce Technology</option>
				<option value="ECO">ECO - Economics</option>
				<option value="EA">EA - Educating Adults</option>
				<option value="EDU">EDU - Education - General</option>
				<option value="EE">EE - Elementary Education</option>
				<option value="ENG">ENG - English</option>
				<option value="ELA">ELA - English Language Academy</option>
				<option value="ENV">ENV - Environmental Science</option>
				<option value="EXP">EXP - Experience Design</option>
				<option value="FIN">FIN - Finance</option>
				<option value="FA">FA - Focus Area</option>
				<option value="FCH">FCH - French</option>
				<option value="GAM">GAM - Game Development</option>
				<option value="GEO">GEO - Geography</option>
				<option value="GER">GER - German</option>
				<option value="AAS">AAS - Global Asian Studies</option>
				<option value="GSB">GSB - Graduate School Of Business</option>
				<option value="GD">GD - Graphic Design</option>
				<option value="GRK">GRK - Greek</option>
				<option value="HTHC">HTHC - Health Communication</option>
				<option value="HIT">HIT - Health Information Technology</option>
				<option value="HLTH">HLTH - Health Science</option>
				<option value="HST">HST - History</option>
				<option value="HON">HON - Honors</option>
				<option value="HSP">HSP - Hospitality Leadership</option>
				<option value="HCD">HCD - Human Centered Design</option>
				<option value="HC">HC - Human Community</option>
				<option value="HCI">HCI - Human-Computer Interaction</option>
				<option value="ICE">ICE - Illinois Institute Of Technology</option>
				<option value="ILL">ILL - Illustration</option>
				<option value="IS">IS - Information Systems</option>
				<option value="IT">IT - Information Technology</option>
				<option value="IPD">IPD - Institute For Professional Development</option>
				<option value="IN">IN - Integrative Learning</option>
				<option value="ISM">ISM - Interactive And Social Media</option>
				<option value="IM">IM - Interactive Media</option>
				<option value="INTC">INTC - Intercultural Communication</option>
				<option value="ICS">ICS - Interdisciplinary Commerce Studies</option>
				<option value="IDS">IDS - Interdisciplinary Studies</option>
				<option value="ISP">ISP - Interdisciplinary Studies Program</option>
				<option value="IB">IB - International Business</option>
				<option value="INT">INT - International Studies</option>
				<option value="IRE">IRE - Irish Studies</option>
				<option value="IWS">IWS - Islamic World Studies</option>
				<option value="ITA">ITA - Italian</option>
				<option value="JPN">JPN - Japanese</option>
				<option value="JZZ">JZZ - Jazz Studies</option>
				<option value="JOUR">JOUR - Journalism</option>
				<option value="LE">LE - Labor Education</option>
				<option value="LAT">LAT - Latin</option>
				<option value="LST">LST - LatinAmerican &amp; Latino Studies</option>
				<option value="LAW">LAW - Law</option>
				<option value="LGQ">LGQ - Lesbian, Gay, Bisexual, Transgender, Queer Studies</option>
				<option value="LLS">LLS - Liberal Learning Seminars</option>
				<option value="LSE">LSE - Liberal Studies In Education</option>
				<option value="LSP">LSP - Liberal Studies Program</option>
				<option value="LL">LL - Lifelong Learning</option>
				<option value="LSI">LSI - Literacy &amp; Specialized Instruction</option>
				<option value="MGT">MGT - Management</option>
				<option value="MIS">MIS - Management Information Systems</option>
				<option value="MKT">MKT - Marketing</option>
				<option value="MPH">MPH - Master Of Public Health</option>
				<option value="MSW">MSW - Masters In Social Work</option>
				<option value="MLS">MLS - Masters Of Liberal Studies</option>
				<option value="MAT">MAT - Mathematical Sciences</option>
				<option value="MMT">MMT - Mathematics For Middle School Teaching</option>
				<option value="MCS">MCS - Media Studies</option>
				<option value="MGE">MGE - Middle Grades Education</option>
				<option value="MSC">MSC - Military Science</option>
				<option value="MOL">MOL - Modern Languages</option>
				<option value="MED">MED - Music Education</option>
				<option value="MEN">MEN - Music Ensemble</option>
				<option value="MUS">MUS - Musicianship</option>
				<option value="NMS">NMS - New Media Studies</option>
				<option value="NSG">NSG - Nursing</option>
				<option value="ORGC">ORGC - Organizational Communication</option>
				<option value="PAX">PAX - Peace, Justice And Conflict Studies</option>
				<option value="PRF">PRF - Performance</option>
				<option value="PAM">PAM - Performing Arts Management</option>
				<option value="PHL">PHL - Philosophy</option>
				<option value="PE">PE - Physical Education</option>
				<option value="PHY">PHY - Physics</option>
				<option value="POL">POL - Polish</option>
				<option value="PSC">PSC - Political Science</option>
				<option value="POR">POR - Portuguese</option>
				<option value="PM">PM - Project Management</option>
				<option value="PSY">PSY - Psychology</option>
				<option value="PPS">PPS - Public Policy Studies</option>
				<option value="PRAD">PRAD - Public Relations And Advertising</option>
				<option value="MPS">MPS - Public Services</option>
				<option value="RE">RE - Real Estate</option>
				<option value="FMS">FMS - Refugee And Forced Migration Studies</option>
				<option value="RELC">RELC - Relational Communication</option>
				<option value="REL">REL - Religious Studies</option>
				<option value="RUS">RUS - Russian</option>
				<option value="STEM">STEM - Science, Technology, Engineering And Math</option>
				<option value="SW">SW - Scientific World</option>
				<option value="SEC">SEC - Secondary Education</option>
				<option value="DCM">DCM - SNL Degree Completion Major</option>
				<option value="SNC">SNC - SNL Liberal Studies</option>
				<option value="SCG">SCG - Social &amp; Cultural Studies Ed Human Dev Grad</option>
				<option value="SCU">SCU - Social/Cultural Studies Education/Human Dev Ugrd</option>
				<option value="SOC">SOC - Sociology</option>
				<option value="SE">SE - Software Engineering</option>
				<option value="REC">REC - Sound Recording Technology</option>
				<option value="SPN">SPN - Spanish</option>
				<option value="SEV">SEV - Strategy Execution Valuation</option>
				<option value="SAP">SAP - Study Abroad Program</option>
				<option value="SUD">SUD - Sustainable Urban Development</option>
				<option value="TCH">TCH - TEACH Program</option>
				<option value="T&amp;L">T&amp;L - Teaching And Learning</option>
				<option value="TDC">TDC - Telecommunications</option>
				<option value="TV">TV - Television Production</option>
				<option value="THE">THE - Theatre Studies</option>
				<option value="TEC">TEC - Theatre Technology</option>
				<option value="UIP">UIP - University Internship Program</option>
				<option value="VFX">VFX - Visual Effects</option>
				<option value="WGS">WGS - Women's And Gender Studies</option>
				<option value="WLE">WLE - World Language Education</option>
				<option value="MWR">MWR - Writing</option>
				<option value="WRD">WRD - Writing Rhetoric And Discourse</option>
			</select>
		</div>
		<div style="display: inline-block; padding-right:10px">
			<input type="text" class="number inputbox" placeholder="NUMBER">
		</div>
		<div style="display: inline-block;">
			<div style="style=padding: 5%;">
				<form onsubmit="submitForm()" action="../search.html" id="field">
					<input class="inputbox" type="hidden" name="q" id="tipue_search_input" autocomplete="off" required value="">
					<input class="inputbox" type="submit" value="SEARCH">
				</form>
			</div>
		</div>
	</span>
<div>
<br />
<hr>
<button class="generate" style="top:-20px; align: center;">ADVANCED SEARCH</button>
<h1>'''

	html += full_name.replace(';','')
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

		    	if (days.length == 0) days = 'OnLine';
		    	if(teacherFirstName.length == 0) teacherFirstName = 'TBD';
		    	if(teacherLastName.length == 0) teacherLastName = 'TBD';
		    	if(classStartTime.length == 0) classStartTime = 'TBD';
		    	if(classEndTime.length == 0) classEndTime = 'TBD';
		    	if(classStatus == 'C') classStatus = 'Closed';
		    	if(classStatus == 'O') classStatus = 'Open';
		    	if(classStatus == 'W') classStatus = 'Waitlist';
		    	
		    	html += '<tr>'
		    	if(readCookie(teacherFirstName.toLowerCase()+'-'+teacherLastName.toLowerCase()+'-add-'+classNumber)==0)
		    	{'''
	html += '''html += '<td><input class="'+teacherFirstName.toLowerCase()+'-'+teacherLastName.toLowerCase()+'-add"'+'id="'+["'''+short_url+'''",classStatus,creditHours,teacherFirstName,teacherLastName,classStartTime,classEndTime,classSection,classNumber,campus,days]+'" type="image" src="../../../add.png" width="20" onclick="addToCart(this)"/>'
		    	}
		    	else
		    	{
		    		html += '<td><input class="'+teacherFirstName.toLowerCase()+'-'+teacherLastName.toLowerCase()+'-add"'+'id="'+['WRD 103',classStatus,creditHours,teacherFirstName,teacherLastName,classStartTime,classEndTime,classSection,classNumber,campus,days]+'" type="image" src="../../../minus.png" width="20" onclick="removeFromCart(this)"/>'
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
		    html += '<div class="center ital" style="padding-top: 1%;">Ratings credited to <a href="http://www.ratemyprofessors.com" target="_blank">Rate My Professors.</a> Courses credited to <a href="http://depaul.edu" target="_blank">DePaul University.</a></div>'

		    html += '<div class="center ital" style="padding-top: .5%;">Contact the <a href="mailto:mocksched@gmail.com?subject=MockSched">Developer</a></div>';
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
	    	end = response.length - 151;
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
	
	function addToCart(contents)
	{
		index = 9
		value = contents.getAttribute('id')
		if(value.split(',').length<12) index=8
		className = contents.getAttribute('class')
		days = 1
		writeCookie(className+'-'+value.split(',')[index],value,days)
		document.getElementById(value).src = "../../../minus.png"
		document.getElementById(value).onclick = function() {removeFromCart(contents);};
		
	}

	function removeFromCart(contents)
	{
		index = 9
		value = contents.getAttribute('id')
		if(value.split(',').length<12) index=8
		className = contents.getAttribute('class')
		document.getElementById(value).src = "../../../add.png"
		document.getElementById(value).onclick = function() {addToCart(contents)};
		delete_cookie(className+'-'+value.split(',')[index])
		
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
	function submitForm()
	{
		var prefix = document.getElementsByClassName('prefix')[0].value
		var number = document.getElementsByClassName('number')[0].value
		if(isNaN(number) == false)
		{
			search = prefix.toUpperCase() + ' ' + number
			document.getElementById('tipue_search_input').value = '"'+search+'"'
			document.getElementById('field').submit()
		}
	}
	function matchStart (term, text) 
	{
		if (text.toUpperCase().indexOf(term.toUpperCase()) == 0) 
		{
	    	return true;
	    }
    	return false;
	}
 
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
	        submitForm()
	    }
	});

	$( document ).ready(function() {
    	$(".prefix").select2();
		$("#myTable").tablesorter({sortInitialOrder: 'desc'});
	});
</script>
</html>'''
	webpage_name = ('classes/'+'-'.join(full_name.split()[:2]).replace(';','').lower()+'.html')
	with open('../'+webpage_name,'w') as output:
			output.write(html)
	return [full_name.replace(';',''),description,'classes/'+'-'.join(full_name.split()[:2]).replace(';','').lower()+'.html']

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

