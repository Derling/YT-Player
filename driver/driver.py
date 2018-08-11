from selenium import webdriver, common

DRIVER_NOT_FOUND_ERROR = common.exceptions.WebDriverException

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
	YOUTUBEPLAYBUTTON = "ytp-play-button"
	def start(self, url):
		self.driver = getDriver()
		self.driver.get(url)
		self.running = True
		self.playing = True

	def quit(self):
		self.driver.quit()
		self.running = False

	def pauseplay(self):
		pause_elem = self.driver.find_element_by_class_name(self.YOUTUBEPLAYBUTTON)
		pause_elem.click()
		self.playing = not self.playing
