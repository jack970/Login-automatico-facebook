import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

class LogarFacebook:
    def __init__(self, driver):
        self.driver = driver

    def logar_com_credenciais(self, usuario, senha):
        self.open_page('https://www.facebook.com/')
        self.logar(usuario, senha)

    def logar_com_credenciais_arquivo(self):
        usuario = os.getenv("USUARIO")
        senha = os.getenv("SENHA")
        self.logar_com_credenciais(usuario, senha)

    def open_page(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
    
    def logar(self, usuario, senha):
        self.driver.find_element(By.NAME, 'email').send_keys(usuario)
        self.driver.find_element(By.NAME, 'pass').send_keys(senha)
        self.driver.find_element(By.NAME, 'pass').send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        # self.driver.find_element_by_xpath('//*[@id="userNavigationLabel"]').click()

class InicializarDriver:
    def __init__(self, chrome_driver_path):
        self.driver_path = chrome_driver_path
        self.driver = self.inicializar_driver()

    def inicializar_driver(self):
        options = self.opcoes_driver()
        self.driver = webdriver.Chrome(service=Service(self.driver_path), options=options)
        self.driver.implicitly_wait(10)
        return self.driver

    def opcoes_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        return chrome_options

if __name__ == '__main__':
    relative_path = os.path.dirname(__file__)
    env_file = os.path.join(relative_path, 'configs/.env')
    load_dotenv(env_file)
    download_driver = ChromeDriverManager().install()
    driver = InicializarDriver(download_driver).driver
    LogarFacebook(driver).logar_com_credenciais_arquivo()