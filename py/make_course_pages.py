#Created by Timothy Gamble
#tjgambs@gmail.com

from BeautifulSoup import BeautifulSoup as Soup
import os
import csv

def create_webpage(filename):
	with open(filename,'r') as class_data:
		reader = csv.reader(class_data)
		info = list(reader)

		title = info[0][0]
		course_description = info[1][0]
		tags = []

		html = '<html><head><title>' + title + '</title>'
		html += '''<link rel="shortcut icon" href="../other/icon.png"><link rel="stylesheet" href="../css/stylesheet.css" type="text/css" media="print, projection, screen" />
					<script type="text/javascript" src="../js/jquery-1.11.3.min.js"></script><script type="text/javascript" src="../js/jquery.tablesorter.min.js"></script>
					</head><script type="text/javascript">$(document).ready(function(){$("#myTable").tablesorter({sortInitialOrder: 'desc'});  }); </script>'''
		html += '<h1>' + title + '</h1><body>' + course_description + '<h2>Available Classes</h2><table id="myTable" class="tablesorter">'
		html += '<thead><tr>'

		#Adds the headers to the table
		for i in info[2]:
			html += '<th>' + i + '</th>'
		html += ' </tr></thead><tbody>'

		#Replace all open spaces with &nbsp; so Safari loads the border
		for i in info[3:]:
			for k in range(len(i)):
				if len(i[k]) == 0: 
					i[k] = '&nbsp;'

			teacher_file = (i[3]+'-'+i[4]).replace(' ','-').lower()

			if(i[0] != '0.0' and os.path.exists('../teachers/' + teacher_file + '.html')):
				html+='<tr>'
				html+='<td>' + '<a href = "../teachers/' + teacher_file + '.html">' + i[0] + '</a></td>'
				html+='<td>' + i[1] + '</td>'
				html+='<td>' + i[2] + '</td>'
				html+='<td>' + '<a href = "../teachers/' + teacher_file + '.html">' + i[3] + '</a></td>'
				html+='<td>' + '<a href = "../teachers/' + teacher_file + '.html">' + i[4] + '</a></td>'

				for j in i[5:]:
					html+='<td>' + j + '</td>'
			else:
				for j in i:
					html += '<td>' + j + '</td>'
			#Adds the first name of the teacher to keywords
			tags.append(i[3])
			#Adds the last name of the teacher to keywords
			tags.append(i[4])

			html += '</tr>'
		html += '</tbody></table></body></html>'

		#Creates a name that only contains the first two words (i.e. wrd-103.html or eco-105.html)
		webpage_name = ('classes/'+'-'.join(title.split()[:2]).replace(';','').lower()+'.html')

		with open('../'+webpage_name,'w') as output:
			output.write(html)

		return [title, course_description,tags,webpage_name]

def create_all_webpages():
	files = []
	for file in os.listdir("../class_data"):
		if file.endswith("csv"): 
			files.append(file)
	to_be_indexed = []

	for i in files:
		to_be_indexed.append(create_webpage('../class_data/'+i))
		create_webpage('../class_data/'+i)

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
				title = clean_index(i[0])
			if i[1]:
				text = clean_index(i[1])
			if i[2]:
				tags = ', '.join('{0}'.format(j) for j in set(i[2]))
				tags = clean_index(tags)
			if i[3]:
				url = clean_index(i[3])

			output.write('{"title":'+ title +',"text":'+ text +',"tags":'+ tags +',"url": '+url+'},\n')
		output.write(']};')

def clean_index(item):
	return '"{0}"'.format(item.replace("\"",'').replace("\r\n",'').replace("\n",''))

def main():
	create_all_webpages()
	
if __name__ == '__main__':
	main()