# -*- coding: utf-8 -*-
import json
import isbnlib
import os
import glob

def format_data():
	with open('../books.json','w') as output:
		file_names = glob.glob("../course_books/*.json")
		dic = {}
		for f in file_names:	
			with open(f) as input:
				data = json.loads(input.read())
				for d in data:
					ret = []
					for i in range(len(d['isbns'])):
						number = isbnlib.to_isbn10(d['isbns'][i])
						if number:
							url ='http://www.amazon.com/gp/product/'+number+'/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN='+number+'&linkCode=as2&tag=mock09-20&linkId=EMBDL7BV7IXRB44G'
							ret.append([d['status'][i],url])
					dic[d['title']] = ret
		json.dump(dic,output)

def get_data():
	with open('../books.json','r') as output:
		data = json.loads(output.read())
		print data['20034']

if __name__ == '__main__':
	format_data()