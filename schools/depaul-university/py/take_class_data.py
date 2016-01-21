#Created by Timothy Gamble
#tjgambs@gmail.com

from BeautifulSoup import BeautifulSoup as Soup
import urllib
import cookielib
import mechanize
import json
import sys

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

def download_classes(termname,termnumber):
	setup_browser()
	response = br.open("http://offices.depaul.edu/student-records/schedule-of-classes/Pages/default.aspx")
	
	br.select_form(nr=0)
	control = br.form.find_control('ctl00$ctl30$g_49ceed09_b59e_4457_94a1_a9ea1bd8a6c6$ctl00$ddTerm')
	control.value = [termnumber]
	br.submit()

	html = br.response().read()
	soup = Soup(html)

	courses = []
	data = json.loads(open('../course_data.json', 'r').read())

	for ul in soup.findAll('ul',{'class':'columnlist medium'}):
		a = ul.findAll('a')
		for i in a:
			url = 'http://offices.depaul.edu/_layouts/DUC.SR.ClassSvc/DUClassSvc.ashx?action=getclasses'
			start = i['href'].rindex('?dtl=Y') + 6
			try:
				course_data = data[' '.join(i.text.split(' ')[:2]).replace(';','')]
				course_description = course_data[0]
				course_prerequisites = course_data[1]
				complete_description = ''
				if 'PREREQUISITE' not in course_description.upper():
					if len(course_description) != 0:
						complete_description += course_description
					if len(course_prerequisites) != 0:
						if 'corequisite' in course_prerequisites and 'prerequisite' in course_prerequisites:
							complete_description += ' REQUISITE(S): ' + course_prerequisites
						elif 'corequisite' in course_prerequisites:
							complete_description += ' COREQUISITE(S): ' + course_prerequisites
						else:
							complete_description += ' PREREQUISITE(S): ' + course_prerequisites
				else:
					complete_description = course_description
			except:
				html = urllib.urlopen(i['href'])
				soup = Soup(html)
				course_description = soup.find('p',{'class':'nopadding-top'}).text
			courses.append([i.text.replace(';',''),complete_description,str(url+i['href'][start:])])
			
	with open('../terms/' + termname + '/classes.json','w') as output:
		json.dump(courses, output)

if __name__ == '__main__':
	download_classes(sys.argv[1],sys.argv[2])