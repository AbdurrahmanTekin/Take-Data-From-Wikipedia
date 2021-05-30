import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys



options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome('D:\\Desktop\\chromedriver.exe',options=options)

driver.get("https://www.wikipedia.org/")
time.sleep(2)
English_button= driver.find_element_by_xpath('//*[@id="js-link-box-en"]/strong')
English_button.click()
time.sleep(1)
search_place= driver.find_element_by_xpath('//*[@id="searchInput"]')
search_place.send_keys("Atmosphere of Earth")
search_button= driver.find_element_by_xpath('//*[@id="searchButton"]')
search_button.click()
data= driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]')
updated_data = data.text
updated_data = updated_data.split("\n")
useful_data = []
for i in updated_data:
    if i == "See also":
        break
    elif len(i) > 20:
        useful_data.append(i)
    else:
        pass


def translate(useful_data):
    driver.get("https://translate.google.com/?hl=tr&sl=en&tl=tr&op=translate")
    for a in useful_data:
        sentence = a.split('.')
        for b in sentence:
            english_place = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea')
            english_place.send_keys(b+".")
            time.sleep(4)
            turkish_place = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[5]/div/div[1]')
            turkish = turkish_place.text
            time.sleep(2)

            print("""--{}
++{}""".format(b+".",turkish))
            english_place.clear()

translate(useful_data)