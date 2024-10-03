import unittest
from unittest.mock import patch
from service import EmailService, SMSService
from notification import SendNotification

class TestSendNotification(unittest.TestCase):

    @patch('builtins.print')
    def test_send_notification_with_email_service(self, mock_print):
        email_service = EmailService()

        notification = SendNotification(service=email_service)

        message = "Test notification via Email"

        notification.send_notification(message)

        mock_print.assert_called_once_with(f"Sending email with message: {message}")

    @patch('builtins.print')
    def test_send_notification_with_sms_service(self, mock_print):
        sms_service = SMSService()

        notification = SendNotification(service=sms_service)

        message = "Test notification via SMS"

        notification.send_notification(message)

        mock_print.assert_called_once_with(f"Sending SMS with message: {message}")

if __name__ == "__main__":
    unittest.main()
