# --- instalações iniciais ---
# 1. pip install playwright
# 2. playwright install

# --- importe de bibliotecas
from playwright.sync_api import sync_playwright
import time
from config import restartus_email, restartus_password

print("Módulos importados corretamente.")

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
        page.fill('xpath=//*[@id="eael-user-login"]', restartus_email)
        wait_for_page_load(page)  # Aguardar o carregamento após o preenchimento
        print("Digitou o e-mail")

        # Preencher o campo de senha
        page.fill('xpath=//*[@id="eael-user-password"]', restartus_password)
        wait_for_page_load(page)  # Aguardar o carregamento após o preenchimento
        print("Digitou a senha")

        # Esperar o botão de login ficar visível
        page.wait_for_selector('//*[@id="eael-login-submit"]', state='visible')

        # Clicar no botão de login
        page.locator('//*[@id="eael-login-submit"]').click()
        print("Clicou no botão de login.")

        # Pausa após o clique
        time.sleep(7)

    else:
        print("Variáveis de ambiente para e-mail e/ou senha não estão definidas.")

    # Fechar a página e o navegador
    page.close()
    navegador.close()
