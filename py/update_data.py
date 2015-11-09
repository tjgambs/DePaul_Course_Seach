#Created by Timothy Gamble
#tjgambs@gmail.com

from BeautifulSoup import BeautifulSoup as Soup
import urllib
import cookielib
import mechanize
import json
import csv

br = mechanize.Browser()
cj = cookielib.LWPCookieJar()


def setup_browser():
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


def download_classes():
	setup_browser()
	response = br.open("http://offices.depaul.edu/student-records/schedule-of-classes/Pages/default.aspx")
	
	br.select_form(nr=0)
	control = br.form.find_control('ctl00$ctl29$g_49ceed09_b59e_4457_94a1_a9ea1bd8a6c6$ctl00$ddTerm')
	control.value = ['0965'] #Winter Quarter
	br.submit()

	html = br.response().read()
	soup = Soup(html)

	courses = []

	with open('../other/classes.json','w') as output:

		for ul in soup.findAll('ul',{'class':'columnlist medium'}):
			a = ul.findAll('a')
			for i in a:
				url = 'http://offices.depaul.edu/_layouts/DUC.SR.ClassSvc/DUClassSvc.ashx?action=getclasses'
				start = i['href'].rindex('?dtl=Y') + 6

				html = urllib.urlopen(i['href'])
				soup = Soup(html)
				course_description = soup.find('p',{'class':'nopadding-top'}).text

				html = urllib.urlopen(url+i['href'][start:])
				data = json.loads(str(Soup(html)))

				print 'Downloaded ' + str(url+i['href'][start:])
				courses.append([i.text,course_description,data])

		json.dump(courses, output)
		format_classes()


def format_classes():
	headers = ['Overall Rating','Class Status','Credit Hours', 'Teacher First Name', 'Teacher Last Name', 'Class Start Time', 'Class End Time', 'Class Section', 'Class Number', 'Location', 'Days']

	with open('../other/classes.json','r') as input:
		class_data = json.loads(input.read())
		for i in range(len(class_data)):

			class_name = str(class_data[i][0])
			class_description = str(class_data[i][1])
			array_of_class_data = []

			for j in range(len(class_data[i][2])):
				days = [0,0,0,0,0,0,0]
				for key, value in class_data[i][2][j].iteritems():
					if key.strip().lower() == 'units_minimum':
						credit_hours = str(value)
					if key.strip().lower() == 'first_name':
						if len(value) == 0: 
							teacher_first_name = 'Staff'
						else:
							teacher_first_name = str(value)
					if key.strip().lower() == 'last_name':
						if len(value) == 0: 
							teacher_last_name = 'Staff'
						else:
							teacher_last_name = str(value)
					if key.strip().lower() == 'meeting_time_start':
						class_start_time = str(value).replace('1/1/1900 ','').replace(':00 ',' ')
					if key.strip().lower() == 'meeting_time_end':
						class_end_time = str(value).replace('1/1/1900 ','').replace(':00 ',' ')
					if key.strip().lower() == 'class_section':
						class_section = str(value)
					if key.strip().lower() == 'class_nbr':
						class_number = str(value)
					if key.strip().lower() == 'location_descr':
						class_location = str(value)
					if key.strip().lower() == 'enrl_stat':
						if(value.upper() == 'O'): class_status = 'Open'
						if(value.upper() == 'C'): class_status = 'Closed'
						if(value.upper() == 'W'): class_status = 'Waitlist'


					if key.strip().lower() == 'mon' and value.strip().lower() == 'y':
						days[0] = 'Monday'
					if key.strip().lower() == 'tues' and value.strip().lower() == 'y':
						days[1] = 'Tuesday'
					if key.strip().lower() == 'wed' and value.strip().lower() == 'y':
						days[2] = 'Wednesday'
					if key.strip().lower() == 'thurs' and value.strip().lower() == 'y':
						days[3] = 'Thursday'
					if key.strip().lower() == 'fri' and value.strip().lower() == 'y':
						days[4] = 'Friday'
					if key.strip().lower() == 'sat' and value.strip().lower() == 'y':
						days[5] = 'Saturday'
					if key.strip().lower() == 'sun' and value.strip().lower() == 'y':
						days[6] = 'Sunday'

				days = filter(lambda a: a != 0, days)
				days =', '.join(days)

				rmp_overall = overall_rating(teacher_first_name,teacher_last_name)

				array_of_class_data.append([rmp_overall,class_status,credit_hours,teacher_first_name,teacher_last_name,class_start_time,class_end_time,class_section,class_number,class_location,days])
			with open('../class_data/'+ class_name.replace('/','').replace(';','') +'.csv','w') as formatted_class:
				writer = csv.writer(formatted_class)
				writer.writerow([class_name])
				writer.writerow([class_description])
				writer.writerow(headers)

				for row in array_of_class_data:
					writer.writerow(row)


def overall_rating(first,last):
	reader = csv.DictReader(open('../other/teachers.csv'))
	for row in reader:
		if first.lower() == row['teacherfirstname_t'].lower() and last.lower() == row['teacherlastname_t'].lower():
			return row['averageratingscore_rf']
	return 'N/A'


def main():
    download_classes()
    format_classes()

if __name__ == '__main__':
	main()