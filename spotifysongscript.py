from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
isim = input("Artist: ")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
class Spotify():
    def window():
        driver.get("http://www.spotify.com.tr")
        assert "Spotify" in driver.title
        driver.maximize_window()

    def entrance():
        enter = driver.find_element(By.CSS_SELECTOR, "button.jsmWVV")
        enter.click()
        time.sleep(3)
        username = driver.find_element(By.ID, "login-username")
        username.send_keys("...")
        password = driver.find_element(By.ID, "login-password")
        password.send_keys("...")
        clik = driver.find_element(By.ID, "login-button")
        clik.click()
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
        
    def song():
        song2 = driver.find_element(By.CSS_SELECTOR, "div.h4HgbO_Uu1JYg5UGANeQ")
        song2.click()
        song3 = driver.find_element(By.CSS_SELECTOR, "button.Qs11Fsr_XqTVFDFWWRkQ")
        song3.click()
        
    def info():
        song_name = driver.find_element(By.CSS_SELECTOR, "div.t_yrXoUO3qGsJS4Y6iXX")
        print(song_name.text)
        artist_name = driver.find_element(By.CSS_SELECTOR, "span.rq2VQ5mb9SDAFWbBIUIn")
        print(artist_name.text)
        song_time = driver.find_element(By.CSS_SELECTOR, "div.Btg2qHSuepFGBG6X0yEN")
        print(song_time.text)
        
    def lyrics():
        lyrics_button = driver.find_element(By.CSS_SELECTOR, "button.Xmv2oAnTB85QE4sqbK00")
        lyrics_button.click()
        time.sleep(2)
        lyrics_text = driver.find_element(By.CSS_SELECTOR, "div.class.data-testid.fullscreen-lyric")
        print(lyrics_text.text)
        
    def suggestion():
        artist_name = driver.find_element(By.CSS_SELECTOR, "span.rq2VQ5mb9SDAFWbBIUIn")
        artist_name.click()
        time.sleep(2)
        album = driver.find_element(By.CSS_SELECTOR, "span.kbIsPl")
        album.click()
        time.sleep(2)
        latest_album = driver.find_element(By.CSS_SELECTOR, "div.tsv7E_RBBw6v0XTQlcRo")
        latest_album.click()
        
Spotify.window()
Spotify.entrance()
Spotify.search()
Spotify.song()
Spotify.info()
Spotify.suggestion()
