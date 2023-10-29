import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm
import time

# Insira aqui o Path do Chromedriver
chromedriver_path = r'(path)chromedriver.exe'

# Insira aqui o Path do arquivo
csv_file_path = r'(path)prestadoras_servicos_telecomunicacoes_cleaned.csv'

# Inicializar o navegador Chrome
driver = webdriver.Chrome(executable_path=chromedriver_path)

# Abrir o site
driver.get("https://www.donodozap.com/")

# Ler o arquivo CSV
df = pd.read_csv(csv_file_path)

# Crie um DataFrame vazio para armazenar os resultados
resultados = pd.DataFrame(columns=['Telefone', 'Nome'])

# Loop pelas entradas do CSV com uma barra de progresso
for index, row in tqdm(df.iterrows(), total=len(df), desc="Progresso"):
    telefone = row['Telefone']

    def is_valid_telefone(telefone):
        if len(telefone) != 3:
            return True
        else:
            return False

    if not is_valid_telefone(telefone):
        print(f"Telefone inválido na linha {index}: {telefone}")
        continue

    # Encontrar o elemento de entrada e preencher com o número de telefone
    telefone_input = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/div/input')
    telefone_input.clear()
    telefone_input.send_keys(telefone)

    driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/div/button').click()

    time.sleep(2)

    try:
        # Esperar pela resposta
        resposta_element = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[1]/div[2]/div/div[2]/div/div')
        resposta = resposta_element.text
    except:
        resposta = "Não encontrado"

    registro = {'Telefone': telefone, 'Nome': resposta}

    resultados = resultados.append(registro, ignore_index=True)

    driver.refresh()

resultados.to_csv('resultados.csv', index=False)

driver.quit()
