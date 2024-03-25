# --- instalações iniciais ---
# 1. pip install playwright
# 2. playwright install

# --- importe de bibliotecas
import logging
from playwright.sync_api import sync_playwright
import time
import os

# Configuração do logger
logging.basicConfig(filename='execution.log', level=logging.INFO)

restartus_email = os.getenv("RESTARTUS_EMAIL")
restartus_password = os.getenv("RESTARTUS_PASSWORD")

logging.info("Módulos importados corretamente.")

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    page = navegador.new_page()

    # Função espera a página carregar para executar a próxima ação
    def wait_for_page_load(page):
        page.wait_for_load_state("load")

    # Abrir a URL e esperar o carregamento completo
    page.goto("https://restartus.org/restartus_login/")
    wait_for_page_load(page)

    # Localizar e clicar no elemento de login
    page.locator('xpath=//*[@id="eael-user-login"]').click()

    if restartus_email and restartus_password:
        # Preencher o campo de e-mail
        page.fill('xpath=//*[@id="eael-user-login"]', RESTARTUS_EMAIL)
        wait_for_page_load(page)  # Aguardar o carregamento após o preenchimento
        print("Digitou o e-mail")
        logging.info("Digitou o e-mail")

        # Preencher o campo de senha
        page.fill('xpath=//*[@id="eael-user-password"]', RESTARTUS_PASSWORD)
        wait_for_page_load(page)  # Aguardar o carregamento após o preenchimento
        print("Digitou a senha")
        logging.info("Digitou a senha")
        
        # Esperar o botão de login ficar visível
        page.wait_for_selector('//*[@id="eael-login-submit"]', state='visible')

        time.sleep(1.5)
        # Clicar no botão de login
        page.locator('//*[@id="eael-login-submit"]').click()
        print("Clicou no botão de login.")
        logging.info("Clicou no botão de login.")
        
        # Pausa após o clique
        time.sleep(1)
        # Função para obter e acumular os valores das divs
        def obter_e_acumular_valores(page):
            
            divs = page.query_selector_all(".gamipress-user-points-amount")
            for div in divs:
                valor = int(div.inner_text())
                
                # print(valor)
            return valor
        amount = obter_e_acumular_valores(page)
        print(amount,"$RTC")

        logging.info(f"Valor obtido e acumulado: {amount}")
        print(f"::set-env name=AMOUNT::{amount}")
        
        time.sleep(7)

    else:
        print("Variáveis de ambiente para e-mail e/ou senha não estão definidas.")

    # Fechar a página e o navegador
    page.close()
    navegador.close()

    logging.info("Fim da execução do script.")
