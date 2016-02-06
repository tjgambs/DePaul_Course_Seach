from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import isbnlib
import glob
import sys

driver = webdriver.PhantomJS()

def format_data(termname):
	file_names = glob.glob('../terms/' + termname + '/course_books/*.json')
	dic = {}
	good_urls = json.loads(open('../good_urls.json', 'r').read())
	bad_urls = json.loads(open('../bad_urls.json', 'r').read())
	for f in file_names:
		with open(f) as input:
			data = json.loads(input.read())
			for d in data:
				ret = []
				for i in range(len(d['isbns'])):
					number = isbnlib.to_isbn10(d['isbns'][i])
					name = ','.join(d['names'][i].split(',')[:-1]) + ', Isbn: ' + d['isbns'][i]
					if number:
						url ='http://www.amazon.com/gp/product/' + number + '/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=' + number + '&linkCode=as2&tag=mocksched-20&linkId=EMBDL7BV7IXRB44G'
						url_for_checking = 'http://www.amazon.com/gp/product/' + number + '/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=' + number + '&linkCode=as2&linkId=EMBDL7BV7IXRB44G'
						if url in good_urls:
							ret.append([d['status'][i],url,name])
						elif url in bad_urls:
							ret.append([d['status'][i],'',name])
						elif check_url(url_for_checking):
							ret.append([d['status'][i],'',name])
							bad_urls.append(url)
						else:
							ret.append([d['status'][i],url,name])
							good_urls.append(url)
					else:
						ret.append([d['status'][i],'',name])
				dic[d['title']] = ret
	with open('../terms/' + termname + '/books.json','w') as output:
		json.dump(dic,output)
	with open('../good_urls.json','w') as good:
		json.dump(good_urls,good)
	with open('../bad_urls.json','w') as bad:
		json.dump(bad_urls,bad)

def check_url(url):
	try:
		driver.get(url)
		return 'Looking for something?' in (driver.page_source)
	except:
		check_url(url)

if __name__ == '__main__':
	format_data(sys.argv[1])
	driver.close()