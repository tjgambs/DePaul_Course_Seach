import json
import isbnlib
import glob
import bottlenose
from BeautifulSoup import BeautifulSoup

def format_data():
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
					name = ','.join(d['names'][i].split(',')[:-1]) + ', Isbn: ' + d['isbns'][i]
					try:
						url ='http://www.amazon.com/gp/product/'+number+'/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN='+number+'&linkCode=as2&tag=mocksched-20&linkId=EMBDL7BV7IXRB44G'
						url_for_checking = 'http://www.webproxy.net/view?q=http://www.amazon.com/gp/product/'+number+'/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN='+number+'&linkCode=as2&linkId=EMBDL7BV7IXRB44G'
						if not check_url(number):
							ret.append([d['status'][i],'',name])
						else:
							ret.append([d['status'][i],url,name])
					except:
						ret.append([d['status'][i],'',name])
				dic[d['title']] = ret
	with open('../books.json','w') as output:
		json.dump(dic,output)

def check_url(number):
	amazon = bottlenose.Amazon('AKIAIJC6MAEHF3QC67NA', '2omychx9HcFOu3hc4+T1qT/BiykvSF9pyIEZmyUF', 'mocksched-20')
	response = amazon.ItemLookup(ItemId=number, SearchIndex='Books', IdType='ISBN')
	if 'is not a valid value for ItemId. Please change this value and retry your request' in response:
		return False
	else:
		return True

if __name__ == '__main__':
	format_data()