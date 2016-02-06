from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
import json
import getpass
import sys

driver = webdriver.PhantomJS()

__URL__ = "https://campusconnect.depaul.edu/psp/CSPRD90/?cmd=login&languageCd=ENG"

def login(username,password):
	driver.get(__URL__)
	time.sleep(10)
	driver.find_element(By.XPATH,'//input[@name="userid"]').send_keys(username.upper())
	driver.find_element(By.XPATH,'//input[@name="pwd"]').send_keys(password)
	driver.find_element(By.XPATH,'//input[@name="Submit"]').click()

def navigate_to_course_search():
	new_url = '''https://campusconnect.depaul.edu/psp/CSPRD90/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.
				SSR_SSENRL_CART.GBL?FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE.HCCC_
				ENROLLMENT.HC_SSR_SSENRL_CART_GBL&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder'''
	driver.get(new_url)
	driver.switch_to_frame(driver.find_element(By.XPATH,'//iframe[@name="TargetContent"]'))
	time.sleep(10)
	driver.find_element(By.XPATH,'//td[@class="SSSTABINACTIVE"][1]').click()
	driver.switch_to_default_content()

def amount_of_subjects():
	driver.switch_to_frame(driver.find_element(By.XPATH,'//iframe[@name="TargetContent"]'))
	time.sleep(10)
	select = Select(driver.find_element(By.XPATH,'//div[@id="win0divSSR_CLSRCH_WRK_SUBJECT_SRCH$0"]/select'))
	options = select.options
	driver.switch_to_default_content()
	return len(options)

def select_term(index):
	driver.switch_to_frame(driver.find_element(By.XPATH,'//iframe[@name="TargetContent"]'))
	time.sleep(10)
	select = Select(driver.find_element(By.XPATH,'//div[@id="win0divCLASS_SRCH_WRK2_STRM$35$"]/select'))
	select.select_by_index(int(index))
	driver.switch_to_default_content()

def search_subject(index):
	driver.switch_to_frame(driver.find_element(By.XPATH,'//iframe[@name="TargetContent"]'))
	time.sleep(10)
	select = Select(driver.find_element(By.XPATH,'//div[@id="win0divSSR_CLSRCH_WRK_SUBJECT_SRCH$0"]/select'))
	select.select_by_index(index)
	driver.find_element(By.XPATH,'//a[@name="CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH"]').click()
	time.sleep(10)

	try:
		if driver.find_element(By.XPATH,'//span[@class="SSSMSGWARNINGTEXT"]'):
			return -1
	except:
		pass

	try:
		if(driver.find_element(By.XPATH,'//input[@id="#ICSave"]') != None):
			driver.find_element(By.XPATH,'//input[@id="#ICSave"]').click()
	except: 
		pass
	driver.switch_to_default_content()
	return 0

def select_course_career(index):
	driver.switch_to_frame(driver.find_element(By.XPATH,'//iframe[@name="TargetContent"]'))
	time.sleep(10)
	select = Select(driver.find_element(By.XPATH,'//div[@id="win0divCLASS_SRCH_WRK2_ACAD_CAREER"]/select'))
	select.select_by_index(index)
	driver.switch_to_default_content()

def amount_of_course_careers():
	driver.switch_to_frame(driver.find_element(By.XPATH,'//iframe[@name="TargetContent"]'))
	time.sleep(10)
	select = Select(driver.find_element(By.XPATH,'//div[@id="win0divCLASS_SRCH_WRK2_ACAD_CAREER"]/select'))
	options = select.options
	driver.switch_to_default_content()
	return len(options)

def take_all_data(code,termname):
	time.sleep(60)
	driver.switch_to_frame(driver.find_element(By.XPATH,'//iframe[@name="TargetContent"]'))
	time.sleep(10)
	end = int(driver.find_element(By.XPATH,'//td[@class="SSSGROUPBOX PSLEFTCORNER"]').text.split()[0])
	file_name = str(driver.find_element(By.XPATH,'//div[@id="win0divSSR_CLSRSLT_WRK_GROUPBOX2GP$0"]/table/tbody/tr/td/table/tbody/tr/td').text.split()[0])
	all_books = []
	for index in range(0,end):
		button = driver.find_element(By.XPATH,'//a[@name="MTG_CLASS_NBR$%s"]' % str(index))
		title = button.text
		button.click()
		time.sleep(10)
		isbns = []
		status = []
		names = []
		if(driver.find_elements(By.XPATH,'//div[contains(@id,"win0divDERIVED_SSR_TXB_SSR_TXBDTL_ISBN")]')):
			isbns = driver.find_elements(By.XPATH,'//div[contains(@id,"win0divDERIVED_SSR_TXB_SSR_TXBDTL_ISBN")]/span[contains(@id,"DERIVED_SSR_TXB_SSR_TXBDTL_ISBN")]')
			status = driver.find_elements(By.XPATH,'//div[contains(@id,"win0divDERIVED_SSR_TXB_SSR_TXB_STATDESCR")]/span[contains(@id,"DERIVED_SSR_TXB_SSR_TXB_STATDESCR")]')
			names = driver.find_elements(By.XPATH,'//div[contains(@id,"win0divDERIVED_SSR_TXB_SSR_TXBDTL_LONG")]/span[contains(@id,"DERIVED_SSR_TXB_SSR_TXBDTL_LONG")]')
		all_books.append(format_book_data(title,isbns,status,names))
		driver.find_element(By.XPATH,'//a[@id="CLASS_SRCH_WRK2_SSR_PB_BACK"]').click()
		time.sleep(10)
	with open('../terms/' + termname + '/course_books/'+file_name+str(code)+'.json','w') as output:
		json.dump(all_books,output)
	driver.switch_to_default_content()

def format_book_data(title,isbns,status,names):
	dic = {}
	if(len(isbns)!=0):
		isbns = [isbn.text for isbn in isbns]
		status = [stat.text for stat in status]
		names = [name.text for name in names]
	dic['title'] = title
	dic['isbns'] = isbns
	dic['status'] = status
	dic['names'] = names
	return dic

def iterate_over_one(index,term,termname,username,password):
	try:
		login(username,password)
		navigate_to_course_search()
		for i in range(1,amount_of_course_careers()):
			select_course_career(i)
			select_term(term)
			time.sleep(3)
			flag = search_subject(index)
			if flag == 0:
				take_all_data(i,termname)
			navigate_to_course_search()
	except:
		iterate_over_one(index,term,termname)

if __name__ == '__main__':
	iterate_over_one(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3],sys.argv[4].upper(),sys.argv[5])
	driver.close()
