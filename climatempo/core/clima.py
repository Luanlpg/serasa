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
        """
        Navega até url pré-definina.
        """
        self.driver.get(self.url)

    def search(self, word='None'):
        """
        Faz busca de informações climaticas por nome de cidade.
        """
        self.navigate()
        if 'google' in self.url:
            self.city = word.upper()
            # faz busca no google com o btn "estou com sorte" para entrar
            # diretamente na url correta, apenas com o nome da cidade.
            self.driver.find_element_by_id(self.search_bar).send_keys('climatempo climatologia '+word)
            try:
                self.driver.find_element_by_name(self.btn_lucky).click()
            # caso ocorra erro, isso quer dizer que a url esta incorreta
            except:
                # cucaremos no google a primeiro resultado com a combinação de palavras chaves
                self.driver.find_element_by_class_name(self.btn_lucky_2).click()
                self.driver.find_element_by_class_name('LC20lb').click()
        # retorna a pagina html
        return self.driver.page_source

    def parser(self, city):
        """
        Método que faz a raspagem de dados.
        """
        try:
            self.city = city
            page = bs4(self.search(city), 'html.parser')
            tbody = page.find_all('tbody')
            # pega todas as linhas apartir da segunda
            trs = tbody[1].find_all('tr')
            # itera tds as linhas
            for tr in range(len(trs)):
                # para cada linha, pega tds as informações e tranforma em um dic
                # chamado mes, com as keys: Minima, Maxima e Precipitação
                mes = trs[tr].find(
                    'td', {'class': 'text-center normal font14 txt-blue'}).text
                outros = trs[tr].find_all(
                    'td', {'class': 'text-center normal font14 txt-black'})
                self.clima[mes] = {
                    'Minima (Cº)': outros[0].text,
                    'Maxima (Cº)': outros[1].text,
                    'Precipitação (mm)': outros[2].text
                }
        # caso ocorra algum erro, isso quer dizer que a url continua errada,
        # portanto, aciono o metodo retry.
        except:
            self.retry()
        # caso esteja td ok, fecho o driver e retorno o objeto clima
        self.driver.quit()
        return self.clima

    def retry(self):
        """
        Metodo que verifica a url atual e altera para a url correta.
        """
        url = self.driver.current_url
        self.url = url.replace('previsao-do-tempo/cidade','climatologia')
        self.parser(self.city)
