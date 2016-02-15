from BeautifulSoup import BeautifulSoup as Soup
import urllib

def take():
	arts_and_literature = 'http://www.depaul.edu/university-catalog/academic-handbooks/undergraduate/university-information/liberal-studies-program/liberal%20studies%20learning%20domains/Pages/arts-and-literature.aspx'
	philosophical_inquiry = 'http://www.depaul.edu/university-catalog/academic-handbooks/undergraduate/university-information/liberal-studies-program/liberal%20studies%20learning%20domains/Pages/philosophical-inquiry.aspx'
	religious_dimensions = 'http://www.depaul.edu/university-catalog/academic-handbooks/undergraduate/university-information/liberal-studies-program/liberal%20studies%20learning%20domains/Pages/religious-dimensions.aspx'
	scientific_inquiry = 'http://www.depaul.edu/university-catalog/academic-handbooks/undergraduate/university-information/liberal-studies-program/liberal%20studies%20learning%20domains/Pages/scientific-inquiry.aspx'
	social_cultural_and_behavioral_inquiry = 'http://www.depaul.edu/university-catalog/academic-handbooks/undergraduate/university-information/liberal-studies-program/liberal%20studies%20learning%20domains/Pages/self-society-and-the-modern-world.aspx'
	understanding_the_past = 'http://www.depaul.edu/university-catalog/academic-handbooks/undergraduate/university-information/liberal-studies-program/liberal%20studies%20learning%20domains/Pages/understanding-the-past.aspx'

	lsldArray = {'Arts and Literature': arts_and_literature,
				'Philosophical Inquiry': philosophical_inquiry,
				'Religious Dimensions': religious_dimensions,
				'Understanding the Past': understanding_the_past,
				'Scientific Inquiry': scientific_inquiry,
				'Social, Cultural, and Behavioral Inquiry': social_cultural_and_behavioral_inquiry}
	ret = {}
	for name, url in lsldArray.iteritems():
		html = urllib.urlopen(url).read()
		soup = Soup(html)
		classes = []
		for a in soup.findAll('a', {'class':'courseLink'}):
			classes.append(' '.join(a.text.split(' ')[:2]))
		ret[name]=classes
	return ret
