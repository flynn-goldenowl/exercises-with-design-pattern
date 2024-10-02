from abc import ABC, abstractmethod

class Service(ABC):
    @abstractmethod
    def send(self, message:str) -> None:
        raise NotImplementedError
    
class EmailService(Service):
    def send(self, message: str) -> None:
        print(f'Sending email with message: {message}')
        
class SMSService(Service):
    def send(self, message: str) -> None:
        print(f'Sending SMS with message: {message}')