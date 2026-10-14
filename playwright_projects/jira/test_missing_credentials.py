from playwright.sync_api import expect

URL = "https://www.saucedemo.com/"


def test_missing_credentials(page):
    page.goto(URL)

    # Step 1
    # Click login with empty fields
    page.locator("#login-button").click()

    expect(page.locator("[data-test='error']")).to_be_visible()

    expect(page.locator("[data-test='error']")).to_contain_text(
        "Username is required"
    )

    expect(page).to_have_url(URL)

    print("Empty login validation passed")


def test_missing_password(page):
    page.goto(URL)

    # Step 2
    username = page.locator("#user-name")
    username.fill("standard_user")

    expect(username).to_have_value("standard_user")

    # Step 3
    page.locator("#login-button").click()

    expect(page.locator("[data-test='error']")).to_be_visible()

    expect(page.locator("[data-test='error']")).to_contain_text(
        "Password is required"
    )

    expect(page).to_have_url(URL)

    print("Missing password validation passed")


def test_password_only(page):
    page.goto(URL)

    # Step 4
    page.locator("#user-name").clear()

    password = page.locator("#password")
    password.fill("secret_sauce")

    expect(password).to_have_value("secret_sauce")

    expect(password).to_have_attribute(
        "type",
        "password"
    )

    page.locator("#login-button").click()

    expect(page.locator("[data-test='error']")).to_be_visible()

    expect(page.locator("[data-test='error']")).to_contain_text(
        "Username is required"
    )

    expect(page).to_have_url(URL)

    print("Password only validation passed")