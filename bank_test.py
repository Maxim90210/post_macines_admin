import unittest
from app import BankAccount, InsufficientFunds

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(1000)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_withdraw(self):
        self.account.withdraw(300)
        self.assertEqual(self.account.get_balance(), 700)

        with self.assertRaises(InsufficientFunds):
            self.account.withdraw(1500)

        with self.assertRaises(ValueError):
            self.account.withdraw(-100)

    def test_transfer(self):
        other_account = BankAccount(500)
        self.account.transfer(other_account, 200)
        self.assertEqual(self.account.get_balance(), 800)
        self.assertEqual(other_account.get_balance(), 700)

        with self.assertRaises(TypeError):
            self.account.transfer("not_an_account", 100)

        with self.assertRaises(InsufficientFunds):
            self.account.transfer(other_account, 1500)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)
