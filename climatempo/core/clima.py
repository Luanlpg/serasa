from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from bs4 import BeautifulSoup as bs4

options = Options()
options.add_argument("--headless")

class ClimaTempo:
    def __init__(self, driver=webdriver.Firefox(firefox_options=options)):
        self.driver = driver
        self.url = 'http://google.com.br'
        self.search_bar = 'lst-ib' #id
        self.btn_lucky = 'btnI' #name
        self.btn_lucky_2 = 'lsb' #class
        self.clima = {}

    def navigate(self):

        self.driver.get(self.url)

    def search(self, word='None'):
        self.navigate()
        if 'google' in self.url:
            self.city = word.upper()
            self.driver.find_element_by_id(self.search_bar).send_keys('climatempo climatologia '+word)
            try:
                self.driver.find_element_by_name(self.btn_lucky).click()
            except:
                self.driver.find_element_by_class_name(self.btn_lucky_2).click()
                self.driver.find_element_by_class_name('LC20lb').click()
        return self.driver.page_source

    def parser(self, city):
        try:
            self.city = city
            page = bs4(self.search(city), 'html.parser')
            tbody = page.find_all('tbody')
            trs = tbody[1].find_all('tr')
            for tr in range(len(trs)):

                mes = trs[tr].find(
                    'td', {'class': 'text-center normal font14 txt-blue'}).text
                outros = trs[tr].find_all(
                    'td', {'class': 'text-center normal font14 txt-black'})
                self.clima[mes] = {
                    'Minima (Cº)': outros[0].text,
                    'Maxima (Cº)': outros[1].text,
                    'Precipitação (mm)': outros[2].text
                }
        except:
            self.retry()
        self.driver.quit()
        return self.clima

    def retry(self):
        url = self.driver.current_url
        self.url = url.replace('previsao-do-tempo/cidade','climatologia')
        self.parser(self.city)
