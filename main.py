#  --- instalações iniciais ---
# 1. pip install playwright
# 2. playwright install
# 3. --- importe de bibliotecas

# pip install pytest-playwright playwright -U
from playwright.sync_api import sync_playwright
from playwright._impl._errors import TargetClosedError
import time
from config import restartus_email, restartus_password  # Importando as credenciais do arquivo config.py



with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    page = navegador.new_page()

    # função espera a pagina carregar para executar proxima coordenada
    def wait_for_page_load(page):
        page.wait_for_load_state("load")
    try:
        # Abrir uma URL e esperar o carregamento completo
        page.goto("https://restartus.org/restartus_login/")
        wait_for_page_load(page)

        page.locator('xpath=//*[@id="eael-user-login"]').click()
        
        if restartus_email and restartus_password:
            page.fill('xpath=//*[@id="eael-user-login"]', restartus_email)
            wait_for_page_load(page)
            print("Digitou o e-mail")
            
            page.fill('xpath=//*[@id="eael-user-password"]', restartus_password)
            wait_for_page_load(page)
            print("Digitou a senha")
                
            time.sleep(1.5)
            page.wait_for_selector('//*[@id="eael-login-submit"]', state='visible')
            page.locator('//*[@id="eael-login-submit"]').click()
            print("Clicou no botão de login.")
            time.sleep(7)  
            
        else:
            print("Variáveis de ambiente para e-mail e/ou senha não estão definidas.")        
            # Esperar antes do fechamento do navegador ou da página
             
    except TargetClosedError:
        pass