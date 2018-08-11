from time import sleep
from selenium import webdriver, common
from driver.errors import WEBPAGE_LOADING_ERROR, DRIVER_NOT_FOUND_ERROR
from driver.lib import YOUTUBE_PLAY_BUTTON, YOUTUBE_NEXT_BUTTON

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
	raise DRIVER_NOT_FOUND_ERROR

class Driver:
	'''
		Wrapper for selenium's web driver
	'''
	def start(self, url):
		self.driver = getDriver()
		self.driver.get(url)

	def quit(self):
		self.driver.quit()
		self.running = False

	def pauseplay(self):
		try:
			play_elem = self.driver.find_element_by_class_name(YOUTUBE_PLAY_BUTTON)
			play_elem.click()
		except WEBPAGE_LOADING_ERROR:
			sleep(5)
			play_elem.click()


	def next(self):
		try:
			next_elem = self.driver.find_element_by_class_name(YOUTUBE_NEXT_BUTTON)
			next_elem.click()
		except WEBPAGE_LOADING_ERROR:
			sleep(5)
			next_elem.click() 
