import unittest
from unittest.mock import patch
from service import EmailService, SMSService

class TestService(unittest.TestCase):

    @patch('builtins.print')
    def test_email_service_send(self, mock_print):
        email_service = EmailService()
        email_service.send("Hello via Email!")
        
        mock_print.assert_called_once_with("Sending email with message: Hello via Email!")

    @patch('builtins.print')
    def test_sms_service_send(self, mock_print):
        sms_service = SMSService()
        sms_service.send("Hello via SMS!")
        
        mock_print.assert_called_once_with("Sending SMS with message: Hello via SMS!")

if __name__ == "__main__":
    unittest.main()
