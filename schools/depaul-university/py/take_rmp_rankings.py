#Created by Timothy Gamble
#tjgambs@gmail.com

import urllib

url0 = 'http://search.mtvnservices.com/typeahead/suggest/?solrformat=true&rows=10&callback=jQuery111003276446736417711_1446762506495&q=*%3A*+AND+schoolid_s%3A1389&defType=edismax&qf=teacherfullname_t%5E1000+autosuggest&bf=pow(total_number_of_ratings_i%2C2.1)&sort=&siteName=rmp&rows=1000000000&start=0&fl=pk_id+teacherfirstname_t+teacherlastname_t+averageratingscore_rf'
url1 = 'http://search.mtvnservices.com/typeahead/suggest/?solrformat=true&rows=10&callback=jQuery1110022448566812090576_1450841735528&q=*%3A*+AND+schoolid_s%3A5485&defType=edismax&qf=teacherfullname_t%5E1000+autosuggest&bf=pow(total_number_of_ratings_i%2C2.1)&sort=&siteName=rmp&rows=1000000000&start=0&fl=pk_id+teacherfirstname_t+teacherlastname_t+averageratingscore_rf'

def download_data(url,number):
	html = urllib.urlopen(url).read()
	with open('../backupRankings'+number+'.html','w') as output:
		output.write(html)

def main():
	try:
		download_data(url0,'0')
		download_data(url1,'1')
	except:
		pass

if __name__ == '__main__':
	main()