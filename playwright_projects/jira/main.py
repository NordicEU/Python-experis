from playwright.sync_api import sync_playwright

from sorting_tests import test_sorting
from product_tests import test_product_details
from cart_tests import test_add_to_cart
from checkout_tests import test_checkout, test_pdf_receipt

from test_missing_credentials import (
    test_missing_credentials,
    test_missing_password,
    test_password_only,
)

from test_valid_login import test_valid_login


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=300
        )

        page = browser.new_page()
        page.set_default_timeout(15000)

        test_missing_credentials(page)
        test_missing_password(page)
        test_password_only(page)
        for user in [
            "standard_user",
            "problem_user",
            "performance_glitch_user",
            "error_user",
            "visual_user",
            "locked_out_user"
        ]:
            page = browser.new_page()
            
            if test_valid_login(page, user):
                if not test_sorting(page):
                    print(f"Sorting failed for {user}")
                if not test_product_details(page):
                    print(f"Product-details failed for {user}")
                cart_success = test_add_to_cart(page)

                if not cart_success:
                    print(f"Add to cart failed for {user}")

                if cart_success:
                    if test_checkout(page):
                        if not test_pdf_receipt(page):
                            print(f"PDF receipt failed for {user}")
                    else: 
                        print(f"Checkout failed for {user}")
            page.close()

        browser.close()


if __name__ == "__main__":
    run()