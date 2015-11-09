from BeautifulSoup import BeautifulSoup as Soup
import urllib
import csv
import json

URL = 'http://odata.cdm.depaul.edu/Cdm.svc/Faculties'
xml = urllib.urlopen(URL).read()
soup = Soup(xml)

for i in soup.findAll('m:properties'):
	filename = (i.find('d:firstname').text + ' ' + i.find('d:lastname').text).lower().replace(' ','-') + '.json'
	with open('../teacher_data/' + filename, 'w') as teacher:
		data = {}
		data['department'] = i.find('d:departmentdescription').text
		data['biography'] = i.find('d:biography').text.replace('&#xD;','')
		data['email'] = i.find('d:email').text
		data['phone'] = i.find('d:phone').text
		
		json.dump(data,teacher)




		
		

