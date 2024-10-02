from notification import SendNotification
from service import SMSService, EmailService

if __name__ == '__main__':
    notification = SendNotification(service=SMSService())
    notification.send_notification('Hi Mom!')
    
    
    notification = SendNotification(service=EmailService())
    notification.send_notification('Hi Dad!')