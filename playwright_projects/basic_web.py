from playwright.sync_api import sync_playwright, expect


def test_text_box(page):
    page.goto("https://demoqa.com/text-box")

    page.locator("#userName").fill("John Doe")
    page.locator("#userEmail").fill("john@doe.com")
    page.locator("#currentAddress").fill("Oslo, Norway")
    page.locator("#permanentAddress").fill("Karl Johans gate")

    page.get_by_role("button", name="Submit").click()

    expect(page.locator("#output")).to_contain_text("John Doe")
    expect(page.locator("#output")).to_contain_text("john@doe.com")


def test_checkbox(page):
    page.goto("https://demoqa.com/checkbox")

    # Expand Home
    page.locator("span.rc-tree-switcher").first.click()

    desktop_checkbox = page.get_by_role(
        "checkbox",
        name="Select Desktop"
    )

    desktop_checkbox.click()

    expect(page.locator("#result")).to_contain_text("desktop")



def test_radio_button(page):
    page.goto("https://demoqa.com/radio-button")

    page.locator("label[for='yesRadio']").click()

    expect(page.locator(".text-success")).to_have_text("Yes")


def test_webtables(page):
    page.goto("https://demoqa.com/webtables")

    page.get_by_role("button", name="Add").click()

    page.locator("#firstName").fill("John")
    page.locator("#lastName").fill("Doe")
    page.locator("#userEmail").fill("john@doe.com")
    page.locator("#age").fill("25")
    page.locator("#salary").fill("50000")
    page.locator("#department").fill("QA")

    page.get_by_role("button", name="Submit").click()

    expect(
        page.locator("table.table-striped")
    ).to_contain_text("John")

    expect(
        page.locator("table.table-striped")
    ).to_contain_text("Doe")
    


def test_buttons(page):
    page.goto("https://demoqa.com/buttons")

    page.locator("#doubleClickBtn").dblclick()
    expect(page.locator("#doubleClickMessage")).to_have_text(
        "You have done a double click"
    )

    page.locator("#rightClickBtn").click(button="right")
    expect(page.locator("#rightClickMessage")).to_have_text(
        "You have done a right click"
    )

    page.get_by_text("Click Me", exact=True).click()
    expect(page.locator("#dynamicClickMessage")).to_have_text(
        "You have done a dynamic click"
    )


def test_links(page):
    page.goto("https://demoqa.com/links")

    page.locator("#created").click()

    expect(page.locator("#linkResponse")).to_contain_text("201")
    expect(page.locator("#linkResponse")).to_contain_text("Created")


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=1300
        )

        page = browser.new_page()

        test_text_box(page)
        test_checkbox(page)
        test_radio_button(page)
        test_webtables(page)
        test_buttons(page)
        test_links(page)

        print("All tests completed successfully.")

        browser.close()


if __name__ == "__main__":
    run()