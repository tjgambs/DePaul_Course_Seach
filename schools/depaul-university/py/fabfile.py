from fabric.api import local
from fabric.context_managers import lcd
import take_book_data as Book
import time
from time import gmtime, strftime

def get_all_books(__TERM__,__TERMNAME__):
	Book.login()
	Book.navigate_to_course_search()
	number_of_courses = Book.amount_of_subjects()
	Book.driver.close()
	first_run = int(number_of_courses) / 10 * 10
	second_run = int(number_of_courses) % 10
	for index in range(1,first_run,10):
		local('python take_book_data.py {0} {1} {2} &'.format(index,__TERM__,__TERMNAME__))
		time.sleep(5)
		local('python take_book_data.py {0} {1} {2} &'.format(index + 1,__TERM__,__TERMNAME__))
		time.sleep(5)
		local('python take_book_data.py {0} {1} {2} &'.format(index + 2,__TERM__,__TERMNAME__))
		time.sleep(5)
		local('python take_book_data.py {0} {1} {2} &'.format(index + 3,__TERM__,__TERMNAME__))
		time.sleep(5)
		local('python take_book_data.py {0} {1} {2} &'.format(index + 4,__TERM__,__TERMNAME__))
		time.sleep(5)
		local('python take_book_data.py {0} {1} {2} &'.format(index + 5,__TERM__,__TERMNAME__))
		time.sleep(5)
		local('python take_book_data.py {0} {1} {2} &'.format(index + 6,__TERM__,__TERMNAME__))
		time.sleep(5)
		local('python take_book_data.py {0} {1} {2} &'.format(index + 7,__TERM__,__TERMNAME__))
		time.sleep(5)
		local('python take_book_data.py {0} {1} {2} &'.format(index + 8,__TERM__,__TERMNAME__))
		time.sleep(5)
		local('python take_book_data.py {0} {1} {2} &'.format(index + 9,__TERM__,__TERMNAME__))
		time.sleep(1000)
	for index in range(first_run + 1,second_run + first_run):
		if index < second_run + first_run - 1:
			local('python take_book_data.py {0} {1} {2} &'.format(index,__TERM__,__TERMNAME__))
			time.sleep(5)
		else:
			local('python take_book_data.py {0} {1} {2} &'.format(index,__TERM__,__TERMNAME__))
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

def update(__TERMNAME__,__TERMNUMBER__,__TERM__,flag):
	print 'Start: ' + strftime("%Y-%m-%d %H:%M:%S")
	if flag:
		local('git checkout gh-pages')
		local('python take_rmp_rankings.py &')
		local('python take_course_descriptions.py')
	local('python take_class_data.py {0} {1}'.format(__TERMNAME__,__TERMNUMBER__))
	local('python make_course_pages.py {0} &'.format(__TERMNAME__))
	if flag:
		local('python make_teacher_pages.py &')
	get_all_books(__TERM__,__TERMNAME__)
	local('python make_amazon_links.py {0}'.format(__TERMNAME__))
	update_website()
	local('rm *.pyc')
	print 'Finish: ' + strftime("%Y-%m-%d %H:%M:%S")

def update_all:
	update('winter-2016','0965',3,True)
	update('spring-2016','0970',4,False)
	update('summer-2016','0975',5,False)

