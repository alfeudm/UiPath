import sys
import asyncio
from playwright.async_api import Playwright, async_playwright, expect
import time
import os


async def run(playwright: Playwright) -> None:
    
    #diretorio_anexos = sys.argv[1]
    #id_processo = sys.argv[2]

    diretorio_anexos = (r'C:\Temp')
    url_fluid = str('https://0109.fluid.sicredi.io')
    url_login = "https://0109.fluid.sicredi.io/sign-in"
    user_fluid = "rpa_0109_estornos"
    senha_fluid = "La976sh3aA"

    id_relatorio_fluid = '1168'
    data_inicio = '07/12/2023'
    data_final = '07/12/2023'
    situacao = 0
    file_path = r'c:\temp\teste.xls'
        
    user_fluid = sys.argv[5]; senha_fluid = sys.argv[6]; id_relatorio_fluid = sys.argv[1]
    data_inicio = sys.argv[3]; data_final = sys.argv[4]; situacao = 0; file_path = sys.argv[2]

    user_fluid = str(user_fluid)
    senha_fluid = str(senha_fluid)
    file_path = file_path.rstrip('\\')
    
    
    id_relatorio = str(id_relatorio_fluid)
    rel_inicio = str(data_inicio)
    rel_final = str(data_final)
    
    url_relatorio = f'{url_fluid}/relatorio/visualizar/processo/id/{id_relatorio}?dt_ini={rel_inicio}&dt_fim={rel_final}&situacao={situacao}&itens_pagina=1000000&go=true'


    browser = await playwright.chromium.launch(headless=True,channel='msedge')
    context = await browser.new_context()
    page = await context.new_page()
    
    print('Iniciando login via ldap...')
    
    await page.goto(url_login)
    await page.get_by_role("button", name="Acessar com minha conta").click()

    await page.get_by_placeholder("Usuário").fill(user_fluid)
    await page.get_by_placeholder("Senha").fill(senha_fluid)
    await page.get_by_role("button", name="Entrar").click()
    print('Aguardando resposta Fluid...')
    time.sleep(2)
    await page.goto("https://0109.fluid.sicredi.io/processes")

    print('Login Realizado com sucesso!')
    
    print('Buscando Relatório...')
    await page.goto(url_relatorio)
    time.sleep(2)
    
    await page.get_by_role("link", name="Exportar").click()
    await page.get_by_text("Adicionar todos").click()
    
    print('Aguardando Download...')
    async with page.expect_download() as download_info:
        await page.get_by_role("button", name="Download").click()
    download = await download_info.value
    
    #print(await download.path())
    await download.save_as(file_path)
    print(file_path)
    
    for _ in range(10):     
        if os.path.exists(file_path):         
            # File exists, create a .txt file with the whole path
            output = diretorio_anexos+"\\output"+ id_relatorio_fluid +".txt"         
            with open(output, 'w') as output:             
                output.write(file_path)         
                print(f"Relatório salvo com sucesso")         
            break     
        else:         
            time.sleep(1)  
            # Wait for 1 second before checking again 
    else:     # File does not exist after waiting for 10 seconds, create a .txt file with a message     
        with open(output, 'w') as output:         
            output.write("The file was not found")     
            print("The file was not found after waiting for 10 seconds. Created a message file.")   
    await context.close()
    await browser.close()

async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())            
            
            
            
            
            
            
            
             
    
    
    
    
    
    
    
    
    
    
    