from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os

caminho_html = "C:/Users/Administrador/Desktop/ficrTour/login.html"
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
url_home = "file:///C:/Users/Administrador/Desktop/ficrTour/index.html"
if driver.current_url == url_home:
    print("redirecionamento bem-sucedido!")
else:
    print(f"redirecionamento falhou. URL atual: {driver.current_url}")
time.sleep(5)
url_roteiro = "file:///C:/Users/Administrador/Desktop/ficrTour/roteiro.html"
driver.get(url_roteiro)
time.sleep(4)
if driver.current_url == url_roteiro:
    print("redirecionamento para roteiro bem-sucedido!")
else:
    print(f"redirecionamento para roteiro falhou. URL atual: {driver.current_url}")
time.sleep(5)
ids_checkboxes = ["casal", "verao", "aventura", "hotel-incluso"]

for checkbox_id in ids_checkboxes:
    checkbox = driver.find_element(By.ID, checkbox_id)
    if not checkbox.is_selected():
        print(f"A caixa de seleção '{checkbox_id}' não está marcada inicialmente")
        checkbox.click()
        time.sleep(1)
    else:
        print(f"A caixa de seleção '{checkbox_id}' já estava marcada")
    if checkbox.is_selected():
        print(f"A caixa de seleção '{checkbox_id}' está marcada agora")
    else:
        print(f"A caixa de seleção '{checkbox_id}' **não** foi marcada corretamente")
    time.sleep(1)

time.sleep(5)
driver.quit()
