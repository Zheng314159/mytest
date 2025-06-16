from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # 可改为 True
    
    page = browser.new_page()
    page.goto("https://example.com")
    page.screenshot(path="example.png")
    page.pdf(path="example.pdf")
    browser.close()
