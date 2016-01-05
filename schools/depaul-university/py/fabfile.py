from fabric.api import local
from fabric.context_managers import lcd
import take_book_data as Book
import time
from time import gmtime, strftime
import getpass

def get_all_books(__TERM__,__TERMNAME__,__USERNAME__,__PASSWORD__):
	Book.login(__USERNAME__,__PASSWORD__)
	Book.navigate_to_course_search()
	number_of_courses = Book.amount_of_subjects()
	Book.driver.close()
	first_run = int(number_of_courses) / 10 * 10
	second_run = int(number_of_courses) % 10
	for index in range(1,first_run,10):
		local('python take_book_data.py {0} {1} {2} {3} {4} &'.format(index,__TERM__,__TERMNAME__,__USERNAME__,__PASSWORD__))
		time.sleep(5)
		local('python take_book_data.py {0} {1} {2} {3} {4} &'.format(index + 1,__TERM__,__TERMNAME__,__USERNAME__,__PASSWORD__))
		time.sleep(5)
		local('python take_book_data.py {0} {1} {2} {3} {4} &'.format(index + 2,__TERM__,__TERMNAME__,__USERNAME__,__PASSWORD__))
		time.sleep(5)
		local('python take_book_data.py {0} {1} {2} {3} {4} &'.format(index + 3,__TERM__,__TERMNAME__,__USERNAME__,__PASSWORD__))
		time.sleep(5)
		local('python take_book_data.py {0} {1} {2} {3} {4} &'.format(index + 4,__TERM__,__TERMNAME__,__USERNAME__,__PASSWORD__))
		time.sleep(5)
		local('python take_book_data.py {0} {1} {2} {3} {4} &'.format(index + 5,__TERM__,__TERMNAME__,__USERNAME__,__PASSWORD__))
		time.sleep(5)
		local('python take_book_data.py {0} {1} {2} {3} {4} &'.format(index + 6,__TERM__,__TERMNAME__,__USERNAME__,__PASSWORD__))
		time.sleep(5)
		local('python take_book_data.py {0} {1} {2} {3} {4} &'.format(index + 7,__TERM__,__TERMNAME__,__USERNAME__,__PASSWORD__))
		time.sleep(5)
		local('python take_book_data.py {0} {1} {2} {3} {4} &'.format(index + 8,__TERM__,__TERMNAME__,__USERNAME__,__PASSWORD__))
		time.sleep(5)
		local('python take_book_data.py {0} {1} {2} {3} {4} &'.format(index + 9,__TERM__,__TERMNAME__,__USERNAME__,__PASSWORD__))
		time.sleep(1000)
	for index in range(first_run + 1,second_run + first_run):
		if index < second_run + first_run - 1:
			local('python take_book_data.py {0} {1} {2} {3} {4} &'.format(index,__TERM__,__TERMNAME__,__USERNAME__,__PASSWORD__))
			time.sleep(5)
		else:
			local('python take_book_data.py {0} {1} {2} {3} {4}'.format(index,__TERM__,__TERMNAME__,__USERNAME__,__PASSWORD__))
			break

def update_website():
	with lcd('../../../'):
		local('git checkout gh-pages')
		local('git add .')
		local('git commit -a -m "General update to data"')
		local('git push')
		local('git checkout master')
		local('git rebase gh-pages')
		local('git push')
		local('git checkout gh-pages')

def remove_teachers():
	with lcd('../'):
		local('rm -r teachers')
		local('mkdir teachers')

def remove_classes(__TERMNAME__):
	with lcd('../terms/' + __TERMNAME__):
		local('rm -r classes')
		local('mkdir classes')

def update(__USERNAME__,__PASSWORD__,__TERMNAME__,__TERMNUMBER__,__TERM__,flag):
	if flag:
		local('git checkout gh-pages')
		local('python take_rmp_rankings.py &')
		local('python take_course_descriptions.py')
	local('python take_class_data.py {0} {1}'.format(__TERMNAME__,__TERMNUMBER__))
	remove_classes(__TERMNAME__)
	local('python make_course_pages.py {0} &'.format(__TERMNAME__))
	if flag:
		remove_teachers()
		local('python make_teacher_pages.py &')
	get_all_books(__TERM__,__TERMNAME__,__USERNAME__,__PASSWORD__)
	local('python make_amazon_links.py {0}'.format(__TERMNAME__))

def update_all():
	print 'Start: ' + strftime("%Y-%m-%d %H:%M:%S")
	username = raw_input('CampusConnect Username: ')
	password = getpass.getpass('CampusConnect Password: ')
	update(username,password,'winter-2016','0965',3,True)
	#update(username,password,'spring-2016','0970',4,False)
	#update(username,password,'summer-2016','0975',5,False)
	update_website()
	local('rm *.pyc')
	print 'Finish: ' + strftime("%Y-%m-%d %H:%M:%S")

