#Created by Timothy Gamble
#tjgambs@gmail.com

from BeautifulSoup import BeautifulSoup as Soup
import cookielib
import mechanize
import getpass

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

def download_emails():
	setup_browser()
	response = br.open("https://login.depaul.edu/ldap/login?service=https%3a%2f%2fwapp.is.depaul.edu%2fDigicationSSO%2fSSO.aspx")
	
	br.select_form(nr=0)
	br.form['username'] = raw_input('Username: ')
	br.form['password'] = getpass.getpass('Password: ')
	br.submit()

	for count in range(0,3158):
		response = br.open("https://depaul.digication.com/user_list.digi?sid=592&cid=0&tid=0&pid=0&&results_per_page=20&user_courseid=0&sort=lastname&direction=&limit=20&page="+str(count))
		html = br.response().read()
		soup = Soup(html).find('tbody').findAll('a')
		for i in soup:
			temp = []
			if 'mailto:' in i['href']:
				temp.append(i['href'].lower()[7:])
			with open('../emails.txt','a') as output:
				for j in temp:
					output.write(j+'\n') 

if __name__ == '__main__':
	download_emails()
