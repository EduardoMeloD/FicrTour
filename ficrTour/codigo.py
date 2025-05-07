from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os

# Caminho absoluto para o arquivo HTML
#aqui voce vai por de acordo com seu pc
caminho_html = 'C:\Users/eduardo/Downloads/ficrTour/index.html'

# Iniciar o Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Abrir o HTML local
driver.get(caminho_html)

# Esperar um pouco para visualizar
time.sleep(2)

# Fechar o navegador
driver.quit()