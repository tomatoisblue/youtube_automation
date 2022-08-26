from tkinter import E
from selenium import webdriver as wd
import chromedriver_binary
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class YouTubeAutomation:
	def __init__(self, incognito = True, headless = False, detach = False):
		self.options = Options()
		# open in incognito
		if incognito:
			self.options.add_argument('--incognito')
		if headless:
			self.options.add_argument('headless')
		if detach:
			self.options.add_experimental_option('detach', True)

		self.set_options()
		self.wait = WebDriverWait(self.driver, 20*60)

	# set driver option
	def set_options(self):
		self.driver = wd.Chrome(options = self.options)

	def headless(self):
		self.options.add_argument('headless')
		self.set_options()

	def open(self, url):
		self.driver.get(url)

	def get_url_of_top_video(self):
		try:
			elem = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
			return elem.get_attribute('href')
		except:
			print("cannot get a url of top video")


	def ad_check(self):
		try:
			elem = self.driver.find_elements(By.XPATH, '//*[@id="ad-preview:15"]/span')
			# self.driver.find_elements(By.CLASS_NAME, 'ytp-ad-player-overlay')
		except:
			pass
		if len(elem) > 0:
			print("ad exists")
			return True
		else:
			print("ad NOT existed")
			return False


	def ad_skip(self):
		try:
			print("trying to skip ad...")
			elem_ad = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ytp-ad-skip-button")))
			elem_ad.click()
		except:
			print("cannot skip ad")

	def set_resolution(self):
		try:
			print("setting video resolution...")
			list = self.driver.find_elements(By.CLASS_NAME, "ytp-settings-button")
			list[0].click()
			# click quality button
			self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Quality')]"))).click()

			# set to 144p
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

	def play(self):
		try:
			self.driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[29]/div[2]/div[1]/button').click()
		except:
			print("cannot click play button")


	def minimize(self):
		try:
			self.driver.minimize_window()
		except:
			print("window NOT minimize")
		print("window minimized")

	def basic_background(self):
		if self.ad_check():
			self.ad_skip()
		self.play()
		self.set_resolution()
		self.close_chat()
		self.minimize()

	def ad_routine(self):
		while True:
			if self.ad_check():
				self.ad_skip()
			time.sleep(2)
			print("ad warden is in opration...")
