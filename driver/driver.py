from time import sleep
from selenium import webdriver, common
from driver.errors import WEBPAGE_LOADING_ERROR, DRIVER_NOT_FOUND_ERROR

def getDriver():
	# Most popular web browsers
	drivers = [
		webdriver.Chrome,
		webdriver.Firefox,
		webdriver.Edge,
		webdriver.Safari
	]
	installed_driver = None
	for driver in drivers:
		try:
			installed_driver = driver()
			return installed_driver
		except DRIVER_NOT_FOUND_ERROR:
			pass
	raise DRIVER_NOT_FOUND_ERROR("Could not find any web driver in PATH")

class Driver:
	'''
		Wrapper for selenium's web driver
	'''
	def start(self, url):
		self.driver = getDriver()
		self.driver.get(url)

	def quit(self):
		self.driver.quit()

	def click_element(self, element):
		try:
			play_elem = self.driver.find_element_by_class_name(element)
			play_elem.click()
		except WEBPAGE_LOADING_ERROR:
			sleep(5)
			play_elem.click() 
