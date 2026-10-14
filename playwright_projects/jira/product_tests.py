from playwright.sync_api import expect

import re

def test_product_details(page):
    try:
        # Click Sauce Labs Backpack
        page.get_by_text(
            "Sauce Labs Backpack",
            exact=True
        ).click()

        # Product details page opened
        expect(page).to_have_url(
            re.compile(r".*inventory-item.*")
        )

        # Product name
        expect(
            page.locator(".inventory_details_name")
        ).to_have_text("Sauce Labs Backpack")

        # Description exists
        expect(
            page.locator(".inventory_details_desc")
        ).to_be_visible()

        # Image exists
        expect(
            page.locator(".inventory_details_img")
        ).to_be_visible()

        # Price
        expect(
            page.locator(".inventory_details_price")
        ).to_have_text("$29.99")

        print("Product details displayed correctly")

        # Back to products
        page.get_by_role(
            "button",
            name="Back to products"
        ).click()

        expect(page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )

        expect(
            page.get_by_text("Products")
        ).to_be_visible()

        print("Returned to inventory page")

        return True

    except Exception as error:
        print(f"Product details test failed: {error}")
        return False