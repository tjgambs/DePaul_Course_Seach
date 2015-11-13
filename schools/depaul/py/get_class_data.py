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

	with open('../classes.json','w') as output:

		for ul in soup.findAll('ul',{'class':'columnlist medium'}):
			a = ul.findAll('a')
			for i in a:
				url = 'http://offices.depaul.edu/_layouts/DUC.SR.ClassSvc/DUClassSvc.ashx?action=getclasses'
				start = i['href'].rindex('?dtl=Y') + 6

				html = urllib.urlopen(i['href'])
				soup = Soup(html)
				course_description = soup.find('p',{'class':'nopadding-top'}).text

				print 'Downloaded ' + str(url+i['href'][start:])
				courses.append([i.text,course_description,str(url+i['href'][start:])])

		json.dump(courses, output)


def main():
    download_classes()

if __name__ == '__main__':
	main()