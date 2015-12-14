from fabric.api import local
from fabric.context_managers import lcd
import take_book_data as Book
import time
from time import gmtime, strftime

def get_all_books():
	Book.login()
	Book.navigate_to_course_search()
	number_of_courses = Book.amount_of_subjects()
	Book.driver.close()
	first_run = int(number_of_courses) / 10 * 10
	second_run = int(number_of_courses) % 10
	for index in range(1,first_run,10):
		local('python take_book_data.py %s &' % str(index))
		time.sleep(5)
		local('python take_book_data.py %s &' % str(index+1))
		time.sleep(5)
		local('python take_book_data.py %s &' % str(index+2))
		time.sleep(5)
		local('python take_book_data.py %s &' % str(index+3))
		time.sleep(5)
		local('python take_book_data.py %s &' % str(index+4))
		time.sleep(5)
		local('python take_book_data.py %s &' % str(index+5))
		time.sleep(5)
		local('python take_book_data.py %s &' % str(index+6))
		time.sleep(5)
		local('python take_book_data.py %s &' % str(index+7))
		time.sleep(5)
		local('python take_book_data.py %s &' % str(index+8))
		time.sleep(5)
		local('python take_book_data.py %s &' % str(index+9))
		time.sleep(1000)
	for index in range(first_run + 1,second_run + first_run):
		if index < second_run + first_run - 1:
			local('python take_book_data.py %s &' % str(index))
			time.sleep(5)
		else:
			local('python take_book_data.py %s' % str(index))
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
		local('git checkout master')

def delete_courses_teachers():
	with lcd('../'):
		local('rm -r teachers')
		local('rm -r classes')
		local('mkdir teachers')
		local('mkdir classes')

def update():
	print 'Start:' + strftime("%Y-%m-%d %H:%M:%S")
	#local('python take_class_data.py')
	#delete_courses_teachers()
	#local('python make_course_pages.py &')
	#local('python make_teacher_pages.py &')
	#get_all_books()
	local('python make_amazon_links.py')
	update_website()
	print 'Finish:' + strftime("%Y-%m-%d %H:%M:%S")

