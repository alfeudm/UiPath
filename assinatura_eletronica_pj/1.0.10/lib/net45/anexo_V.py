
import requests
from bs4 import BeautifulSoup
import os, re, time
import sys
import asyncio
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    
    diretorio_anexos = sys.argv[1]
    id_processo = sys.argv[2]
    #id_processo = '612275'
    #diretorio_anexos = (r'C:\Users\alfeu_souza\Downloads')
    
    url_login = "https://0109.fluid.prd.sicredi.cloud/usuario"
    user = "rpa_0109_estornos@sicredi.com.br"
    passw = "123456"
    url_process = "https://0109.fluid.prd.sicredi.cloud/process/visualizar/index/id/"+ id_processo
    nome_anexo = "Anexo_V_"+id_processo+".pdf"
    
    browser = await playwright.chromium.launch(headless=True, channel='chrome')
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto(url_login)
    await page.get_by_placeholder("usuario@email.com").fill(user)
    await page.get_by_placeholder("••••••••••").fill(passw)
    await page.get_by_role("button", name="Acessar", exact=True).click()

    await page.goto(url_process)
    await page.get_by_text("Documentos Impressos").nth(0).click()
    
    try:
        async with page.expect_download() as download_info:
            async with page.expect_popup() as page1_info:
                await page.locator(".tooltip-trigger > .has-text-black").first.click()
            page1 = await page1_info.value

        download = await download_info.value
        # Wait for the download process to complete
        print(await download.path())
        # Save downloaded file somewhere
        await download.save_as(diretorio_anexos+"\\"+nome_anexo)
        
        
    except Exception as e:
        print(e)
        
    file_path = os.path.join(diretorio_anexos, nome_anexo) 
    # Wait for 10 seconds for the file to exist 
    for _ in range(10):     
        if os.path.exists(file_path):         
            # File exists, create a .txt file with the whole path
            output = diretorio_anexos+"\\output"+ id_processo +".txt"         
            with open(output, 'w') as output:             
                output.write(file_path)         
                print(f"The file '{nome_anexo}' exists in the directory '{diretorio_anexos}'.")         
            break     
        else:         
            time.sleep(1)  
            # Wait for 1 second before checking again 
    else:     # File does not exist after waiting for 10 seconds, create a .txt file with a message     
        with open(output, 'w') as output:         
            output.write("Sem Anexo V")     
            print("The file was not found after waiting for 10 seconds. Created a message file.")    
    
    await context.close()
    await browser.close()

async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())