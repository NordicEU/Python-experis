from playwright.sync_api import sync_playwright, expect


URL = "https://demoqa.com/automation-practice-form"


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=300
        )

        page = browser.new_page()
        page.goto(URL)

        # Text fields
        page.locator("#firstName").fill("John")
        page.locator("#lastName").fill("Doe")
        page.locator("#userEmail").fill("john.doe@test.com")

        # Gender
        page.locator("label[for='gender-radio-1']").click()

        # Mobile number
        page.locator("#userNumber").fill("1234567890")

        # Date of Birth
        dob = page.locator("#dateOfBirthInput")
        dob.click()

        page.locator(".react-datepicker__year-select").select_option("1995")
        page.locator(".react-datepicker__month-select").select_option("4")  # May

        page.locator(
            ".react-datepicker__day--015:not(.react-datepicker__day--outside-month)"
        ).click()

        # Subjects
        page.locator("#subjectsInput").fill("Maths")
        page.locator("#subjectsInput").press("Enter")

        # Hobby
        page.get_by_text("Sports").click()

        # Picture upload
        page.locator("#uploadPicture").set_input_files({
            "name": "photo.txt",
            "mimeType": "text/plain",
            "buffer": b"dummy file"
        })

        # Current address
        page.locator("#currentAddress").fill(
            "Karl Johans gate 1, Oslo"
        )

        # State
        page.locator("#state").click()
        page.get_by_text("NCR", exact=True).click()

        # City
        page.locator("#city").click()
        page.get_by_text("Delhi", exact=True).click()

        # Submit
        page.locator("#submit").click()

        # Verification
        expect(
            page.get_by_text("Thanks for submitting the form")
        ).to_be_visible()

        expect(
            page.locator(".modal-content")
        ).to_contain_text("John Doe")

        print("Form submitted successfully!")

        browser.close()


if __name__ == "__main__":
    run()