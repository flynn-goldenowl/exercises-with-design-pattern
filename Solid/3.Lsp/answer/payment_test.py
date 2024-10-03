import unittest
from unittest.mock import patch, call
from payment import CreditCardPayment, PayPalPayment, CashPayment, handle_payment

class TestPaymentProcessing(unittest.TestCase):

    @patch('builtins.print')
    def test_credit_card_payment(self, mock_print):
        processor = CreditCardPayment()
        handle_payment(processor, 100)

        expected_calls = [
            call('Processing payment of $100'),
            call('Processing credit card payment of $100'),
            call('Validating credit card details...'),
            call('Charging the credit card...'),
        ]
        assert mock_print.mock_calls == expected_calls

    @patch('builtins.print')
    def test_paypal_payment(self, mock_print):
        processor = PayPalPayment()
        handle_payment(processor, 200)

        expected_calls = [
            call('Processing payment of $200'),
            call('Processing PayPal payment of $200'),
            call('Redirecting to PayPal...'),
            call('Completing Paypal transaction...')
        ]
        assert mock_print.mock_calls == expected_calls

    @patch('builtins.print')
    def test_cash_payment(self, mock_print):
        processor = CashPayment()
        handle_payment(processor, 50)

        expected_calls = [
            call('Processing payment of $50'),
            call('Processing cash payment of $50'),
            call('Payment success...')
        ]
        assert mock_print.mock_calls == expected_calls

if __name__ == "__main__":
    unittest.main()
