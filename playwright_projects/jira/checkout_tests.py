from playwright.sync_api import expect


def test_checkout(page):
    try:

        # Open cart
        page.locator(".shopping_cart_link").click()

        expect(page).to_have_url(
            "https://www.saucedemo.com/cart.html"
        )

        # Verify item name
        expect(
            page.locator(".inventory_item_name")
        ).to_have_text("Sauce Labs Backpack")

        # Verify quantity
        expect(
            page.locator(".cart_quantity")
        ).to_have_text("1")

        # Verify price
        expect(
            page.locator(".inventory_item_price")
        ).to_have_text("$29.99")

        print("Cart displays correct item information")

        # Checkout
        page.locator("#checkout").click()

        expect(page).to_have_url(
            "https://www.saucedemo.com/checkout-step-one.html"
        )

        # Verify checkout fields
        expect(page.locator("#first-name")).to_be_visible()
        expect(page.locator("#last-name")).to_be_visible()
        expect(page.locator("#postal-code")).to_be_visible()

        print("Checkout form opened")

        # First name
        first_name = page.locator("#first-name")

        first_name.fill("John")

        expect(first_name).to_have_value("John")

        print("First name accepted")

        # Last name
        last_name = page.locator("#last-name")

        last_name.fill("Doe")

        expect(last_name).to_have_value("Doe")

        print("Last name accepted")

        # Postal code
        postal_code = page.locator("#postal-code")

        postal_code.fill("0150")

        expect(postal_code).to_have_value("0150")

        print("Postal code accepted")

        # Continue
        page.locator("#continue").click()

        expect(page).to_have_url(
            "https://www.saucedemo.com/checkout-step-two.html"
        )

        expect(
            page.locator(".inventory_item_name")
        ).to_have_text("Sauce Labs Backpack")

        expect(
            page.locator(".inventory_item_price")
        ).to_have_text("$29.99")

        expect(
            page.locator(".cart_quantity")
        ).to_have_text("1")

        expect(
            page.locator(".summary_subtotal_label")
        ).to_contain_text("$29.99")

        expect(
            page.locator(".summary_tax_label")
        ).to_be_visible()

        expect(
            page.locator(".summary_total_label")
        ).to_be_visible()

        print("Order overview verified")

        page.locator("#finish").click()

        expect(page).to_have_url(
            "https://www.saucedemo.com/checkout-complete.html"
        )

        expect(
            page.get_by_text("Thank you for your order!")
        ).to_be_visible()

        print("Order completed")

        return True

    except Exception as error:
        print(f"Checkout test failed: {error}")
        return False

def test_pdf_receipt(page):
    try:

        # Verify order completed
        expect(
            page.get_by_text(
                "Thank you for your order!"
            )
        ).to_be_visible()

        # Download PDF
        with page.expect_download() as download_info:

            page.get_by_role(
                "button",
                name="Generate PDF order"
            ).click()

        download = download_info.value

        pdf_path = download.path()

        print(f"PDF downloaded: {pdf_path}")

        return True

    except Exception as error:
        print(f"PDF test failed: {error}")
        return False