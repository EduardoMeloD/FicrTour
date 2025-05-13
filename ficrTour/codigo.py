from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os

caminho_html = "C:/Users/eduardo/Downloads/ficrTour/login.html"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(caminho_html)
time.sleep(4)
usuario = driver.find_element(By.ID, "usuario")
senha = driver.find_element(By.ID, "senha")
usuario.send_keys("admin")
senha.send_keys("123")
time.sleep(4)
usuario.clear()
senha.clear()
time.sleep(3)
button = driver.find_element(By.ID, "btnLogin")
button.click()
time.sleep(4)
print(f" a url atual é: {driver.current_url}")
url_home = "file:///C:/Users/eduardo/Downloads/ficrTour/index.html"
if driver.current_url == url_home:
    print("redirecionamento bem-sucedido!")
else:
    print(f"redirecionamento falhou. URL atual: {driver.current_url}")

checkbox = driver.find_element(By.ID, "aceite")
if not checkbox.is_selected():
    print("a caixa de selecao nao esta marcada inicialmente")
checkbox.click()
time.sleep(2)
if checkbox.is_selected():
    print("a caixa de selecao esta marcada")
time.sleep(30)
driver.quit()