import json
import isbnlib
import glob
import urllib2
import json

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
						default = {'Publisher': '', 'Language': '', 'Title': '', 'Authors': [''], 'ISBN-13':'', 'Year':''}
						name = ','.join(d['names'][0].split(',')[:-1])
						if not number: 
							number = ""
						url ='http://www.amazon.com/gp/product/'+number+'/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN='+number+'&linkCode=as2&tag=mock09-20&linkId=EMBDL7BV7IXRB44G'
						ret.append([d['status'][i],url,name])
					dic[d['title']] = ret
		json.dump(dic,output)

if __name__ == '__main__':
	format_data()