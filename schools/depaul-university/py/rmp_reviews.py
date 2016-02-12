import urllib
import json

def pages_of_reviews(id):
	counter = 1
	url = 'http://www.ratemyprofessors.com/paginate/professors/ratings?tid=' + str(id) + '&page=' + str(counter)
	page = urllib.urlopen(url).read()

	data = json.loads(page)

	number_of_reviews = int(data['remaining'])
	return number_of_reviews/20+2

def get_all_reviews(id):
	try:
		reviews = []
		for i in range(1,pages_of_reviews(id)+1):
			url = 'http://www.ratemyprofessors.com/paginate/professors/ratings?tid=' + str(id) + '&page=' + str(i)
			page=urllib.urlopen(url).read()

			data = json.loads(page)
			reviews.append(data['ratings'])
		return reviews
	except:
		return 'dead'

def format_reviews(id):
	formatted_reviews = []
	reviews = get_all_reviews(id)
	if reviews == 'dead': return 'dead'
	class_name = ''
	grade_received = ''
	date = ''
	comments = ''
	easy = ''
	clarity = ''
	helpful = ''

	for i in reviews:
		for j in i:
			temp = {}
			temp['class_name'] = j['rClass']
			temp['grade_received'] = j['teacherGrade']
			temp['date'] = j['rDate']
			temp['comments'] = j['rComments']
			temp['easy'] = j['rEasy']
			temp['clarity'] = j['rClarity']
			temp['helpful'] = j['rHelpful']
			formatted_reviews.append(temp)

	return formatted_reviews