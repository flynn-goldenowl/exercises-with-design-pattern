from service import Service

class SendNotification():
    def __init__(self, service: Service) -> None:
        self.service = service
        
    def send_notification(self, message: str) -> None:
        self.service.send(message)
        
