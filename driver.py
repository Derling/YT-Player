from selenium import webdriver

class Driver:
	'''
		Wrapper for selenium's web driver
	'''
	YOUTUBEPLAYBUTTON = "ytp-play-button"
	def start(self, url):
		self.driver = webdriver.Chrome()
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