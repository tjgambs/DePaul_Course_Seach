import json
import isbnlib
import glob
import urllib2

def format_data():
	with open('../books.json','w') as output:
		file_names = glob.glob("../course_books/*.json")
		dic = {}
		for f in file_names:
			print f	
			with open(f) as input:
				data = json.loads(input.read())
				for d in data:
					ret = []
					for i in range(len(d['isbns'])):
						number = isbnlib.to_isbn10(d['isbns'][i])
						name = ','.join(d['names'][i].split(',')[:-1])
						if not number: 
							number = ""
						url ='http://www.amazon.com/gp/product/'+number+'/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN='+number+'&linkCode=as2&tag=mock09-20&linkId=EMBDL7BV7IXRB44G'
						if not check_url(url):
							print url
							url = ""
						ret.append([d['status'][i],url,name])
					dic[d['title']] = ret
		json.dump(dic,output)

def check_url(url):
	try:
		request_headers = {"Accept-Language": "en-US,en;q=0.5",
							"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
							"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
							"Referer": "http://thewebsite.com",
							"Connection": "keep-alive"}
		request = urllib2.Request(url, headers=request_headers)
		return urllib2.urlopen(request).getcode() < 400 
	except urllib2.HTTPError, e:
		if e.code == 404: return False

if __name__ == '__main__':
	format_data()