# -*- coding: UTF-8 -*-

#Created by Timothy Gamble
#mocksched@gmail.com

from BeautifulSoup import BeautifulSoup as Soup
import urllib
import json
import csv
import os
import unidecode
import rmp_reviews

#The id number of your school can be found in the ratemyprofessor link. For example
#the link of a universities page might look like this: 
#		http://www.ratemyprofessors.com/campusRatings.jsp?sid=1389
#The universities id number would be 1389, the number following 'sid='.
school_id_number = '1389'

#Please specify how many teachers you want in your data set. You can have all of 
#them if you enter in 'all' or you can enter in a number with in quotations.
#	Either this: how_many_teachers = '10'
#	or this: how_many_teachers = 'all'
how_many_teachers = 'all' 

#Write true next to the items you want to have and false to the items you do not want.
teacher_id 			= True
teacher_first_name 		= True
teacher_last_name 		= True
number_of_ratings 		= True
overall_rating 			= True
helpfulness_rating 		= True
clarity_rating 			= True
easiness_rating 		= True

#Creates a url with the predefined url parameters.
def generate_url():
	url ='http://search.mtvnservices.com/typeahead/suggest/?solrformat=true&rows=10&callback=jQuery111003276446736417711_1446762506495&q=*%3A*+AND+schoolid_s%3A' + school_id_number + '&defType=edismax&qf=teacherfullname_t%5E1000+autosuggest&bf=pow(total_number_of_ratings_i%2C2.1)&sort=&siteName=rmp&rows='	
	
	#Adds the amount of teachers wanted to a url paramater
	if(how_many_teachers.lower() == 'all'):
		url += total_teachers() + '&start=0&fl='
	else:
		url += how_many_teachers + '&start=0&fl='

	#Adds the url parameters as specified above
	if(teacher_id):
		url += 'pk_id+'
	if(teacher_first_name):
		url += 'teacherfirstname_t+'
	if(teacher_last_name):
		url += 'teacherlastname_t+'
	if(number_of_ratings):
		url += 'total_number_of_ratings_i+'
	if(overall_rating):
		url += 'averageratingscore_rf+'
	if(helpfulness_rating):
		url += 'averagehelpfulscore_rf+'
	if(clarity_rating):
		url += 'averageclarityscore_rf+'
	if(easiness_rating):
		url += 'averageeasyscore_rf+'
	if(url[-1] == '+'): 
		url = url[:-1]
	return url

#Takes the url generated and takes all of the data to be formatted.
def gather_data():
	url = generate_url()
	#Formats the data to be used in a list
	page_content = urllib.urlopen(url).read()
	begin = page_content.index('"docs":')+7

	#Characters with accents screwing everything up
	page = page_content[begin:-5].replace('í','i') 
	data = json.loads(page)

	#Creates a url for each professor, this is where all of the student reviews can be found
	for key in data:
		key['teacher_profile'] = 'http://www.ratemyprofessors.com/ShowRatings.jsp?tid='+ str(key['pk_id'])
		key['univerity_id'] = str(school_id_number)
	
	return data

#Totals all of the teachers that are associated with the specified university
def total_teachers():
	url = 'http://search.mtvnservices.com/typeahead/suggest/?callback=jQuery11100050687990384176373_1446754108140&q=*:*+AND+schoolid_s:' + school_id_number + '&siteName=rmp'
	page_content = urllib.urlopen(url).read()

	begin = page_content.index('"numFound":')+11
	end = page_content.index(',"start":')

	return page_content[begin:end]

#Takes all of the data and stores it in a csv called teachers.csv
def export_to_csv():
	data = gather_data()
	keys = data[0].keys()

	with open('../teachers.csv', 'wb') as output_file:
	    dict_writer = csv.DictWriter(output_file, keys)
	    dict_writer.writeheader()
	    dict_writer.writerows(data)

def create_teacher_webpage(id,name,values):
	reviews = rmp_reviews.format_reviews(id)
	name = name.encode('utf-8').replace('í','i')
	print name

	with open('../teachers/' + name.replace(' ','-').replace('/','').lower() + '.html','w') as output:
		html = '<!DOCTYPE html><html><head><title>' + name + ' - ' + values[0] + '</title>'
		html +=	'''<link rel="stylesheet" type="text/css" href="../../../css/stylesheet.css"><link href="http://fonts.googleapis.com/css?family=Open+Sans:300,400|Merriweather:300,300italic" rel="stylesheet"><link rel="stylesheet" id="tipue3" type="text/css" href="../../default/tipuesearch/tipuesearch.css"><link rel="shortcut icon" href="../../../icon.png"></head><style type="text/css">img.alignleft{ float: left; 
					margin: 0 1em 1em 0;}.alignleft{ float: left; }#left{width: 200px;height: 150px;float: left;padding-bottom:30px;padding-top: 20px;}
					#right{height: 150px;margin-left: 200px; padding-bottom: 30px;padding-top: 20px;}</style><body><div><span><h3><a href="../../../course-cart.html" style="text-decoration:none; float:right; color:#333;">Course Cart</a></h3></span><span>
					<h1 style="float:left; padding: 0px; padding-right:2%;">MockSched</a></h1><form action="../../../search.html">
					<input type="text" name="q" id="tipue_search_input" autocomplete="off" required placeholder="Enter a Course Name or General Keyword" style="width:40%;"></form></span><div><br /><br /><h1>'''
		html += name + '<hr></h1><div><h2>'

		#Adds the professors overall rankings
		html += 'Overall Quality: ' + values[0] + '<br><br>'
		html += 'Helpfulness: ' + values[1] + '<br>'
		html += 'Clarity: ' + values[2] + '<br>'
		html += 'Easiness: ' + values[3]
		html += '</h2></div><h1>Student Reviews</h1><hr>'

		#Adds the student reviews to the webpage
		for i in reviews:
			html += '<div id="container" class="review"><div id="left">'
			
			html += 'Date: ' + str(i['date']) + '<br>'
			html += 'Class Name: ' + str(i['class_name']) + '<br>'
			html += 'Helpfulness: ' + str(i['helpful']) + '<br>'
			html += 'Clarity: ' + str(i['clarity']) + '<br>'
			html += 'Easiness: ' + str(i['easy']) + '<br>'
			html += 'Grade Received: ' + str(i['grade_received'])

			html += '</div><div id="right"><div>'
			html += i['comments']
			html += '</div></div></div>'
		html += '</div>'
		html += '<div class="center ital" style="padding-top: 1%;">Ratings and reviews credited to <a href="http://www.ratemyprofessors.com" target="_blank">Rate My Professors</a></div>'
		html += '<div class="center ital" style="padding-top: .5%;">Contact the <a href="mailto:mocksched@gmail.com?subject=MockSched">Developer</a></div>';
		html += '</body>'
		html += '</html>'

		output.write(html.encode("utf-8", "ignore"))


def create_all_teacher_webpages():
	data = gather_data()
	for i in data:
		try: 
			name = i['teacherfirstname_t'] + ' ' + i['teacherlastname_t']
		except: 
			name = None
		try: 
			rating = str(i['averageratingscore_rf'])
		except: 
			rating = '0'
		try: 
			helpful = str(i['averagehelpfulscore_rf'])
		except: 
			helpful = '0'
		try: 
			clarity = str(i['averageclarityscore_rf'])
		except: 
			clarity = '0'
		try: 
			easy = str(i['averageeasyscore_rf'])
		except: 
			easy = '0'

		if name != None:
			create_teacher_webpage(str(i['pk_id']),name,[rating,helpful,clarity,easy])

def main():
    export_to_csv()
    create_all_teacher_webpages()

if __name__ == '__main__':
	main()