import unittest

from Unittesting_project.BankAccount import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(100)

    def test_deposit(self):
        self.account.deposit(50)

        self.assertEqual(
            self.account.get_balance(),
            150
        )

    def test_withdraw(self):
        self.account.withdraw(25)

        self.assertEqual(
            self.account.get_balance(),
            75
        )

    def test_invalid_deposit(self):
        before = self.account.get_balance()

        with self.assertRaises(ValueError):
            self.account.deposit(-10)

        self.assertEqual(
            self.account.get_balance(),
            before
        )

    def test_invalid_withdraw(self):
        before = self.account.get_balance()

        with self.assertRaises(ValueError):
            self.account.withdraw(500)

        self.assertEqual(
            self.account.get_balance(),
            before
        )

if __name__ == "__main__":
    unittest.main()
