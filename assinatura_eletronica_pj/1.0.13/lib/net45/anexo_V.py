
import requests
from bs4 import BeautifulSoup
import os, re, time
import sys
import asyncio
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    

    # id_processo = '688594'
    # diretorio_anexos = (r'C:\Users\alfeu_souza\Downloads\Automacao_Assinaturas_PJ')
    
    diretorio_anexos = sys.argv[1]
    id_processo = sys.argv[2]
    
    url_login = "https://0109.fluid.sicredi.io/sign-in"
    user = "rpa_0109_estornos"
    passw = "La976sh3aA"
    url_process = "https://0109.fluid.sicredi.io/process/visualizar/index/id/"+ id_processo
    nome_anexo = "Anexo_V_"+id_processo+".pdf"
    
    browser = await playwright.chromium.launch(headless=True, channel='chrome')
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto(url_login)
    await page.get_by_role("button", name="Acessar com minha conta").click()

    await page.get_by_placeholder("Usuário").fill(user)
    await page.get_by_placeholder("Senha").fill(passw)
    await page.get_by_role("button", name="Entrar").click()
    
    try:
        await expect(page.get_by_role("button", name="Acessar com minha conta")).not_to_be_visible()
    except:
        time.sleep(3)
    
    time.sleep(3)
    
    if await page.get_by_role("button", name="Acessar com minha conta").is_visible():
        await page.get_by_role("button", name="Acessar com minha conta").click()
    
    try:    
        await expect(page.get_by_text("- Caixa de entrada")).to_be_visible()
    except:
        raise Exception()
    
    #await page.goto("https://0109.fluid.sicredi.io/processes")
    await page.goto(url_process)
    await page.get_by_text("Documentos Impressos").nth(0).click()
    
    # expect(page.get_by_text("Visualizar Processo")).to_be_visible()
    #document.querySelectorAll("#app > div:nth-child(2) > section > div > div:nth-child(3) > div:nth-child(2) > div.m-0.p-0 > div")[12].children[0].children[0].children[0].children[1].children[0]
    #await expect(page.locator("#app")).to_contain_text("Anexo V")
    await expect(page.locator("body > div.bg-gray > div:nth-child(5) > section > div > div:nth-child(3) > div:nth-child(2) > div.m-0.p-0")).to_contain_text("Anexo V")
    try:
        async with page.expect_download() as download_info:
            async with page.expect_popup() as page1_info:
                #await page.get_by_text("Anexo V - Declaração IOF Empresa Optante pelo Simples Nacional", exact=True).get_attribute()
                await page.locator(".tooltip-trigger > .has-text-black").last.click()
                page1 = await page1_info.value
                #await page1.keyboard.press('Control+s')
                #await page.locator("#app").get_by_text("Anexo V *").click()


        download = await download_info.value
        # Wait for the download process to complete
        print(await download.path())
        # Save downloaded file somewhere
        await download.save_as(diretorio_anexos+"\\"+nome_anexo)
        
    except Exception as e:
        print(e)
        
    file_path = os.path.join(diretorio_anexos, nome_anexo) 
    output = diretorio_anexos+"\\output"+ id_processo +".txt" 
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
