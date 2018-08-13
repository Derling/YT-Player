from time import sleep
from selenium import webdriver, common
from driver.errors import WEBPAGE_LOADING_ERROR, DRIVER_NOT_FOUND_ERROR
from driver.lib import get_element_msg, AUDIO_CONTROL

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
	def __init__(self, logger):
		self.logger = logger

	def start(self, url):
		# Starts the selenium web driver on a given url
		self.driver = getDriver()
		self.logger.info("opening selenium")
		self.driver.get(url)
		self.logger.info(f"playing {self.get_title()}")
		self.playing = True

	def quit(self):
		# Shut's down the selenium web driver
		self.logger.info("shutting down selenium")
		self.driver.quit()

	def click_element(self, element_class):
		# Clicks on an element based on the element's class
		self.logger.info(get_element_msg(element_class, self.playing))
		
		try:
			play_elem = self.driver.find_element_by_class_name(element_class)
			play_elem.click()
		except WEBPAGE_LOADING_ERROR:
			sleep(5)
			play_elem.click()

		if element_class == AUDIO_CONTROL:
			self.playing = not self.playing
		else:
			self.playing = True

	def get_title(self):
		# Return the tile of the url the web driver is on
		return self.driver.title[:-10] # There is a " - youtube" suffix on youtube videos
