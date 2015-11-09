#Created by Timothy Gamble
#tjgambs@gmail.com

import os
import csv 

def create_webpage(filename):
	with open(filename,'r') as class_data:
		reader = csv.reader(class_data)
		info = list(reader)

		title = info[0][0]
		course_description = info[1][0]
		tags = []

		html = '<html><head><title>'+title+'</title>'
		html += '''<link rel="shortcut icon" href="../other/icon.png"><link rel="stylesheet" href="../css/stylesheet.css" type="text/css" media="print, projection, screen" />
					<script type="text/javascript" src="../js/jquery-1.11.3.min.js"></script><script type="text/javascript" src="../js/jquery.tablesorter.min.js"></script>
					</head><script type="text/javascript">$(document).ready(function(){$("#myTable").tablesorter({sortInitialOrder: 'desc'});  }); </script>'''

		html += '<h1>'+title+'</h1><body>'+course_description+'<h2>Available Classes</h2><table id="myTable" class="tablesorter">'
		html+='<thead><tr>'

		for i in info[2]:
			tags.append(i)
			html+='<th>' + i + '</th>'
		html+=' </tr></thead><tbody>'

		for i in info[3:]:

			for k in range(len(i)):
				if len(i[k]) == 0: 
					i[k] = '&nbsp;'


			if(i[0] != '0.0' and os.path.exists('../teachers/' + i[3].replace(' ','-').lower()+'-'+i[4].replace(' ','-').lower() + '.html')):
				html+='<tr>'

				tags.append(i[0])
				html+='<td>' + '<a href = "../teachers/' + i[3].replace(' ','-').lower()+'-'+i[4].replace(' ','-').lower() + '.html">' + i[0] + '</a></td>'

				tags.append(i[1])
				html+='<td>' + i[1] + '</td>'

				tags.append(i[2])
				html+='<td>' + i[2] + '</td>'

				tags.append(i[3])
				html+='<td>' + '<a href = "../teachers/' + i[3].replace(' ','-').lower()+'-'+i[4].replace(' ','-').lower() + '.html">' + i[3] + '</a></td>'

				tags.append(i[4])
				html+='<td>' + '<a href = "../teachers/' + i[3].replace(' ','-').lower()+'-'+i[4].replace(' ','-').lower() + '.html">' + i[4] + '</a></td>'

				for j in i[5:]:
					tags.append(j)
					html+='<td>' + j + '</td>'
			else:
				for j in i:
					tags.append(j)
					html+='<td>' + j + '</td>'

			html+=' </tr>'
        
		html+='</tbody></table></body></html>'

		with open('../classes/'+title.replace(' ','-').replace('/','').replace(';','')+'.html','w') as output:
			output.write(html)

		tags = list(set(tags))
		tags = filter(None, tags)
		return [title, course_description,tags,('classes/'+title.replace(' ','-').replace('/','').replace(';','')+'.html')]


def create_all_webpages():
	files = []
	for file in os.listdir("../class_data"):
		if file.endswith("csv"): 
			files.append(file)
	to_be_indexed = []

	for i in files:
		to_be_indexed.append(create_webpage('../class_data/'+i))

	send_to_be_indexed(to_be_indexed)


def send_to_be_indexed(items):

	with open('../tipuesearch/tipuesearch_content.js','w') as output:
		output.write('var tipuesearch = {"pages": [\n')
		for i in items:
			title = '""'
			text = '""'
			tags ='""'
			url = '""'

			if i[0]:
				title = '"{0}"'.format(i[0].replace("\"",'').replace("\r\n",'').replace("\n",''))
			if i[1]:
				text = '"{0}"'.format(i[1].replace("\"",'').replace("\r\n",'').replace("\n",''))
			if i[2]:
				tags = ', '.join('{0}'.format(j) for j in set(i[2]))
				tags = '"{0}"'.format(tags.replace("\"",'').replace("\r\n",'').replace("\n",''))
			if i[3]:
				url = '"{0}"'.format(i[3].replace("\"","\'"))

			output.write('{"title":'+ title +',"text":'+ text +',"tags":'+ tags +',"url": '+url+'},\n')
		output.write(']};')


def main():
	create_all_webpages()
	

if __name__ == '__main__':
	main()
