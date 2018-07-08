from selenium import webdriver, common

DRIVERNOTFOUNDERROR = common.exceptions.WebDriverException

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
			break
		except DRIVERNOTFOUNDERROR:
			continue
	return installed_driver

class Driver:
	'''
		Wrapper for selenium's web driver
	'''
	YOUTUBEPLAYBUTTON = "ytp-play-button"
	def start(self, url):
		# **TODO** raise error if driver is None and if get functions raises an error
		self.driver = getDriver()
		self.driver.get(url)
		self.running = True
		self.playing = True

	def quit(self):
		if hasattr(self, "driver") and self.running:
			self.driver.quit()
			self.running = False

	def pauseplay(self):
		if hasattr(self, "driver"):
			pause_elem = self.driver.find_element_by_class_name(self.YOUTUBEPLAYBUTTON)
			pause_elem.click()
			self.playing = not self.playing