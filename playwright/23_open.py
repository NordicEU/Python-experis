from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://example.com")

    time.sleep(5)
    print(page.title())

    page.screenshot(path="screenshot.png")
    browser.close
