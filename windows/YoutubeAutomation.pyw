from selenium import webdriver as wd
import chromedriver_binary
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class YouTube:
	def __init__(self, incognito = True, headless = False, detach = False, brave = False):
		self.options = Options()
		self.brave = False

		# open in incognito
		if incognito:
			self.options.add_argument('--incognito')
		# open with no gui
		if headless:
			self.options.add_argument('headless')
		# keep browser open
		if detach:
			self.options.add_experimental_option('detach', True)
		# open in brave
		if brave:
			# set path to your brave binary file
			self.options.binary_location = 'C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe'
			self.brave = True

		self.set_options()
		self.wait = WebDriverWait(self.driver, 20)

	# set driver option
	def set_options(self):
		self.driver = wd.Chrome(options = self.options)

	def open(self, url):
		self.driver.get(url)

	# when you are on channel page
	def get_url_of_top_video(self):
		try:
			elem = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
			return elem.get_attribute('href')
		except:
			print("cannot get a url of top video")


	def ad_check(self):
		try:
			self.driver.find_element(By.CSS_SELECTOR, 'div[id^="ad-text:"]')
		except:
			print("ad NOT exist")
			return False
		print("ad exists")
		return True


	def ad_skip(self):
		print("trying to skip ad...")
		try:
			elem_ad = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ytp-ad-skip-button")))
			elem_ad.click()
		except:
			print("somehow cannot skip ad")
		print("ad skipped")

	# set video resolution
	# default is 144p
	def set_resolution(self, res = "144p"):
		try:
			print("setting video resolution...")
			elem = self.driver.find_elements(By.CLASS_NAME, "ytp-settings-button")
			elem[0].click()
			# click quality button
			self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Quality')]"))).click()
			# set to 144p
			if res == "1080p60":
				self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(string(),'1080p60')]"))).click()
			elif res == "1080p":
				self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(string(),'1080p')]"))).click()
			elif res == "720p60":
				self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(string(),'720p60')]"))).click()
			elif res == "720p":
				self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(string(),'720p')]"))).click()
			elif res == "480p":
				self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(string(),'480p')]"))).click()
			elif res == "360p":
				self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(string(),'360p')]"))).click()
			elif res == "240p":
				self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(string(),'240p')]"))).click()
			else:
				self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(string(),'144p')]"))).click()

		except:
			print("cannot set resolution")

		print("resolution setting accomplished")


	def close_chat(self):
		try:
			self.driver.find_element(By.XPATH, '//*[@id="show-hide-button"]/ytd-toggle-button-renderer/a').click()
		except:
			print("cannot close chat")
		print("chat closed")

	def close_premium_banner(self):
		try:
			self.driver.find_elements(By.XPATH, '//*[@id="dismiss-button"]/a').click()
		except:
			print("cannot close youtube premium banner")

	def play(self):
		try:
			self.driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[29]/div[2]/div[1]/button').click()
		except:
			print("cannot click play button")


	def minimize(self):
		try:
			self.driver.minimize_window()
		except:
			print("window NOT minimized")
		print("window minimized")

	def basic_background(self):
		if not self.brave:
			cnt = 0
			while(cnt<2):
				if self.ad_check():
					self.ad_skip()
				time.sleep(2)
				cnt += 1
		self.play()
		self.set_resolution()
		self.close_chat()
		self.close_premium_banner()
		self.minimize()

	def ad_routine(self):
		if self.brave:
			print("you are on brave, so don't have to run ad_routine.")
			return
		while True:
			if self.ad_check():
				self.ad_skip()
			time.sleep(5)
			print("warden of ad is in operation...")
