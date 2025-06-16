# test_example.py
from playwright.async_api import async_playwright
import pytest
import nest_asyncio

nest_asyncio.apply() #type: ignore

@pytest.mark.asyncio
async def test_example1():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        page = await browser.new_page()
        await page.goto("https://example.com")
        assert "Example Domain" in await page.title()
        await browser.close()
