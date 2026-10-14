def test_sorting(page):
    try:
        # Name A-Z
        page.locator(".product_sort_container").select_option("az")

        names = page.locator(
            ".inventory_item_name"
        ).all_text_contents()

        assert names == sorted(names)

        print("Name (A to Z)")

        # Name Z-A
        page.locator(".product_sort_container").select_option("za")

        names = page.locator(
            ".inventory_item_name"
        ).all_text_contents()

        assert names == sorted(names, reverse=True)

        print("Name (Z to A)")

        # Price Low-High
        page.locator(".product_sort_container").select_option("lohi")

        prices = [
            float(p.replace("$", ""))
            for p in page.locator(
                ".inventory_item_price"
            ).all_text_contents()
        ]

        assert prices == sorted(prices)

        print("Price (low to high)")

        # Price High-Low
        page.locator(".product_sort_container").select_option("hilo")

        prices = [
            float(p.replace("$", ""))
            for p in page.locator(
                ".inventory_item_price"
            ).all_text_contents()
        ]

        assert prices == sorted(
            prices,
            reverse=True
        )

        print("Price (high to low)")

        return True

    except Exception as error:
        print(f"Sorting test failed: {error}")
        return False