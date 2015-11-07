# -*- coding: UTF-8 -*-

#Created by Timothy Gamble
#tjgambs@gmail.com

from BeautifulSoup import BeautifulSoup as Soup
import urllib
import json
import csv
import os
import unidecode

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

	with open('teachers.csv', 'wb') as output_file:
	    dict_writer = csv.DictWriter(output_file, keys)
	    dict_writer.writeheader()
	    dict_writer.writerows(data)


def pages_of_reviews(id):
	counter = 1
	url = 'http://www.ratemyprofessors.com/paginate/professors/ratings?tid=' + str(id) + '&page=' + str(counter)
	page = urllib.urlopen(url).read()
	
	data = json.loads(page)
	number_of_reviews = int(data['remaining'])
	return number_of_reviews/20+2

def get_all_reviews(id):
	reviews = []
	for i in range(1,pages_of_reviews(id)+1):
		url = 'http://www.ratemyprofessors.com/paginate/professors/ratings?tid=' + str(id) + '&page=' + str(i)
		page=urllib.urlopen(url).read()

		data = json.loads(page)
		reviews.append(data['ratings'])
	
	return reviews

def format_reviews(id):
	formatted_reviews = []
	reviews = get_all_reviews(id)

	class_name = ''
	grade_received = ''
	date = ''
	comments = ''
	easy = ''
	clarity = ''
	helpful = ''

	for i in reviews:
		for j in i:
			temp = {}
			temp['class_name'] = j['rClass']
			temp['grade_received'] = j['teacherGrade']
			temp['date'] = j['rDate']
			temp['comments'] = j['rComments']
			temp['easy'] = j['rEasy']
			temp['clarity'] = j['rClarity']
			temp['helpful'] = j['rHelpful']
			formatted_reviews.append(temp)

	return formatted_reviews

def create_teacher_webpage(id,name,values):

	reviews = format_reviews(id)
	if name == None: return
	name = name.encode('utf-8').replace('í','i')

	picture_name = name.replace(' ','-').lower()
	if not os.path.exists('teacher_pictures/' + picture_name):
		picture_name = 'default'

	with open('teachers/' + name.replace(' ','-').replace('/','').lower() + '.html','w') as output:
		html = '<!DOCTYPE html><html><head><title>' + name + ' - ' + values[0] + '</title><link rel="shortcut icon" href="../icon.png">'
		
		html +=	'''<link rel="stylesheet" type="text/css" href="../stylesheet.css"></head><style type="text/css">img.alignleft{ float: left; 
					margin: 0 1em 1em 0;}.alignleft{ float: left; }#left{width: 200px;height: 100px;float: left;padding-bottom:30px;padding-top: 20px;}
					#right{height: 100px;margin-left: 200px; padding-bottom: 30px;padding-top: 20px;}</style><h1>'''
		
		html += name + '<hr></h1><div><h2>'

		html += 'Overall Quality: ' + values[0] + '<br><br>'
		html += 'Helpfulness: ' + values[1] + '<br>'
		html += 'Clarity: ' + values[2] + '<br>'
		html += 'Easiness: ' + values[3]

		html += '</h2></div><h1>Student Reviews</h1><hr>'

		for i in reviews:
			html += '<div id="container"><div id="left">'

			html += 'Date: ' + str(i['date']) + '<br>'
			html += 'Class Name: ' + str(i['class_name']) + '<br>'
			html += 'Helpfulness: ' + str(i['helpful']) + '<br>'
			html += 'Clarity: ' + str(i['clarity']) + '<br>'
			html += 'Easiness: ' + str(i['easy']) + '<br>'
			html += 'Grade Received: ' + str(i['grade_received'])

			html += '</div><div id="right"><div>'

			html += i['comments']

			html += '</div></div></div>'

		html += '</body></html>'

		output.write(html.encode("utf-8", "ignore"))

def create_all_teacher_webpages():
	data = gather_data()
	for i in data:
		rating = '0'
		helpful = '0'
		clarity = '0'
		easy = '0'
		name = None

		try: name = i['teacherfirstname_t'] + ' ' + i['teacherlastname_t']
		except: pass
		try: rating = str(i['averageratingscore_rf'])
		except: pass
		try: helpful = str(i['averagehelpfulscore_rf'])
		except: pass
		try: clarity = str(i['averageclarityscore_rf'])
		except: pass
		try: easy = str(i['averageeasyscore_rf'])
		except: pass

		create_teacher_webpage(str(i['pk_id']),name,[rating,helpful,clarity,easy])


def main():
    export_to_csv()
    create_all_teacher_webpages()


if __name__ == '__main__':
	main()
	
