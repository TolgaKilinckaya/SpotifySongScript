from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
isim = input("Şarkı: ")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
class Spotify():
    def pencere():
        driver.get("http://www.spotify.com")
        assert "Spotify" in driver.title
        driver.maximize_window()

    def entrance():
        giris = driver.find_element(By.CSS_SELECTOR, "button.jsmWVV")
        giris.click()
        time.sleep(3)
        username = driver.find_element(By.ID, "login-username")
        username.send_keys("your mail adress")
        password = driver.find_element(By.ID, "login-password")
        password.send_keys("your password")
        tikla = driver.find_element(By.ID, "login-button")
        tikla.click()
        time.sleep(3)

    def search():
        elem = driver.find_element(By.LINK_TEXT, "Ara")
        elem.click()
        time.sleep(2)
        elem2 = driver.find_element(By.CSS_SELECTOR, "input.QO9loc33XC50mMRUCIvf")
        elem2.clear()
        elem2.send_keys(isim)
        elem2.send_keys(Keys.RETURN)
        time.sleep(2)
    def sarki():
        song = driver.find_element(By.CSS_SELECTOR, "div.h4HgbO_Uu1JYg5UGANeQ")
        song.click()
        song2 = driver.find_element(By.CSS_SELECTOR, "button.Qs11Fsr_XqTVFDFWWRkQ")
        song2.click()


Spotify.pencere()
Spotify.entrance()
Spotify.search()
Spotify.sarki()
