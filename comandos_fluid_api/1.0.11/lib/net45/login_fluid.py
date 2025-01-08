import sys
import asyncio
from playwright.async_api import Playwright, async_playwright, expect
import time
import os


async def run(playwright: Playwright) -> None:
    
    user_fluid = "rpa_0109_estornos"
    senha_fluid = "La976sh3aA"
    
    user_fluid = sys.argv[1]; senha_fluid = sys.argv[2]
    
    url_login = "https://0109.fluid.sicredi.io/sign-in"
    
    browser = await playwright.chromium.launch(headless=False,channel='msedge')
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto(url_login)
    await page.get_by_role("button", name="Acessar com minha conta").click()

    await page.get_by_placeholder("Usuário").fill(user_fluid)
    await page.get_by_placeholder("Senha").fill(senha_fluid)
    await page.get_by_role("button", name="Entrar").click()
    
    time.sleep(2)
    
    while True:
        time.sleep(2)
        
        
  
async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())   