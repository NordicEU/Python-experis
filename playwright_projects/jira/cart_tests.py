from playwright.sync_api import expect


def test_add_to_cart(page):
    try:


        back_button = page.get_by_role("button", name="Back to products")

        if back_button.count() > 0:
            if back_button.is_visible():
                back_button.click()

        remove_button = page.locator("#remove-sauce-labs-backpack")

        if remove_button.count() > 0:
            if remove_button.is_visible():
                remove_button.click()
        
        # Add Backpack
        page.locator(
            "#add-to-cart-sauce-labs-backpack"
        ).click()

        # Button changed to Remove
        expect(
            page.locator(
                "#remove-sauce-labs-backpack"
            )
        ).to_be_visible()

        # Cart badge shows 1
        expect(
            page.locator(".shopping_cart_badge")
        ).to_have_text("1")

        print("Backpack added to cart")

        # Open cart
        page.locator(".shopping_cart_link").click()

        # Verify product details
        expect(
            page.locator(".inventory_item_name")
        ).to_have_text("Sauce Labs Backpack")

        expect(
            page.locator(".inventory_item_price")
        ).to_have_text("$29.99")

        expect(
            page.locator(".cart_quantity")
        ).to_have_text("1")

        print("Backpack appears correctly in cart")

        return True

    except Exception as error:
        print(f"Add to cart test failed: {error}")
        return False
