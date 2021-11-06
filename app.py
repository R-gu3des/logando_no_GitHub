from selenium import webdriver
from time import sleep

class Selenium_Chrome:
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acessar_github(self, site):
        self.chrome.get(site)

    def clica_sign_in(self):
        try:
            botao = self.chrome.find_element_by_link_text("Sign in")
            botao.click()
        except Exception as e:
            print('Erro ao clicar em Sign in:', e)
            self.chrome.quit()

    def sair(self):
        self.chrome.quit()
    
    def fazer_login(self):
        input_login = self.chrome.find_element_by_id('login_field')
        input_senha = self.chrome.find_element_by_id('password')
        botao_login = self.chrome.find_element_by_name('commit')
        input_login.send_keys('TestandoSelenium')
        sleep(1)
        input_senha.send_keys('97390767ruan')
        sleep(1)
        botao_login.click()

    def menu_logado(self):
        botao_perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary')
        botao_perfil.click()
    
    def visualizar_perfil(self):
        sleep(1)
        botao_perfil = self.chrome.find_element_by_link_text('Your profile')
        botao_perfil.click()

if __name__ == '__main__':
    Chrome = Selenium_Chrome()
    Chrome.acessar_github('https://github.com/')
    sleep(1)
    Chrome.clica_sign_in()
    Chrome.fazer_login()
    Chrome.menu_logado()
    Chrome.visualizar_perfil()
    sleep(15)
    Chrome.sair()

