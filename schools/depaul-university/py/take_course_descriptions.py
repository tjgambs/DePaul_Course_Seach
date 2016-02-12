#Created by Timothy Gamble
#tjgambs@gmail.com

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

driver = webdriver.Firefox()

__URL__ = "http://www.depaul.edu/university-catalog/course-descriptions/Pages/default.aspx?letter=A&subject=Accountancy"

def take():
	driver.get(__URL__)
	time.sleep(5)
	subjects = driver.find_elements(By.XPATH,'//div[@class="grid_6"]/span/ul[@id="subjectBank"]/li/a[contains(@class,"AZSubject")]')
	subject_urls = []
	data = {}
	for subject in subjects:
		subject_urls.append(subject.get_attribute('href'))
	for url in subject_urls:
		driver.get(url)
		time.sleep(5)
		courses = driver.find_elements(By.XPATH,'//div[@class="grid_14"]/span/ul[@class="course-list course-descrip"]/li')
		for course in courses:
			name = course.find_element_by_class_name('subject').text
			description = course.find_element_by_class_name('description').text
			prerequisites = course.find_element_by_class_name('prerequisites').text
			data[name] = [description,prerequisites]
	with open('../course_data.json','w') as output:
		json.dump(data,output)
	driver.close()

if __name__ == '__main__':
	take()
