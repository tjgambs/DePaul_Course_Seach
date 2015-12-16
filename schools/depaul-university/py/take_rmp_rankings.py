import urllib
__URL__ = 'http://search.mtvnservices.com/typeahead/suggest/?solrformat=true&rows=10&callback=jQuery111003276446736417711_1446762506495&q=*%3A*+AND+schoolid_s%3A1389&defType=edismax&qf=teacherfullname_t%5E1000+autosuggest&bf=pow(total_number_of_ratings_i%2C2.1)&sort=&siteName=rmp&rows=1000000000&start=0&fl=pk_id+teacherfirstname_t+teacherlastname_t+averageratingscore_rf'
html = urllib.urlopen(__URL__).read()
with open('../backupRankings.html','w') as output:
	output.write(html)