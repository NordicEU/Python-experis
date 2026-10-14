from playwright.sync_api import expect

URL = "https://www.saucedemo.com/"
PASSWORD = "secret_sauce"


def test_valid_login(page, username):
    page.goto(URL)

    # Username
    username_field = page.locator("#user-name")
    username_field.fill(username)

    expect(username_field).to_have_value(username)

    # Password
    password_field = page.locator("#password")
    password_field.fill(PASSWORD)

    expect(password_field).to_have_value(PASSWORD)
    expect(password_field).to_have_attribute("type", "password")

    # Login
    page.locator("#login-button").click()

    try:
        # Verify successful login
        expect(page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )

        expect(
            page.get_by_text("Products")
        ).to_be_visible()

        print(f"{username} logged in successfully")

        return True

    except Exception:
        error = page.locator("[data-test='error']")

        if error.is_visible():
            print(f"{username}: {error.text_content()}")
        else:
            print(f"{username}: Login failed")

        return False