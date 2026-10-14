from playwright.sync_api import sync_playwright, expect
import re

URL = "https://www.selenium.dev/selenium/web/web-form.html"

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()
        page.goto(URL)

        expect(page).to_have_title("Web form")

        page.get_by_label("Text input").fill("John Doe")
        page.get_by_label("password").fill("Secret")
        page.get_by_label("Textarea").fill("First row\nSecond row\nThird row")

        expect(page.locator("input[name='my-disabled']")).to_be_disabled()
        expect(page.locator("input[name='my-readonly']")).not_to_be_editable()

        page.locator("select[name='my-select']").select_option(label="Two")

        page.locator("input[name='my-datalist']").fill("Seattle")

        page.locator("input[name='my-file']").set_input_files({
            "name": "cv.pdf",
            "mimeType": "text/pdf",
            "buffer": b"Hello CV"
        })

        page.get_by_label("Checked checkbox").uncheck()
        page.get_by_label("Default checkbox").check()

        page.get_by_label("Default radio").check()
        expect(page.get_by_label("Checked radio")).not_to_be_checked()

        page.locator("input[name='my-colors']").fill("#ff0000")

        date = page.locator("input[name='my-date']")
        date.click()
        date.press("Control+A")
        date.type("10/10/2026")

        page.locator("input[name='my-range']").fill("8")

        page.get_by_role("button", name="Submit").click()

        expect(page).to_have_url(re.compile(r"submitted-form\.html"))
        expect(page.get_by_role("heading", name="Form submitted")).to_be_visible()
        expect(page.locator("#message")).to_have_text("Received!")

        print(f"Submitted URL: {page.url}")

        browser.close()


if __name__ == "__main__":
    run()