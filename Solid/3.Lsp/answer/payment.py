from abc import ABC, abstractmethod

class OnlinePaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount:int) -> None:
        print(f'Processing payment of ${amount}')
        
class CreditCardPayment(OnlinePaymentProcessor):
    def process_payment(self, amount: int) -> None:
        super().process_payment(amount)
        
        print(f'Processing credit card payment of ${amount}')
        print('Validating credit card details...')
        print('Charging the credit card...')

class PayPalPayment(OnlinePaymentProcessor):
    def process_payment(self, amount: int) -> None:
        super().process_payment(amount)
        
        print(f'Processing PayPal payment of ${amount}')
        print('Redirecting to PayPal...')
        print('Completing Paypal transaction...')
        
class OfflinePaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount:int) -> None:
        print(f'Processing payment of ${amount}')
        
class CashPayment(OfflinePaymentProcessor):
    def process_payment(self, amount: int) -> None:
        super().process_payment(amount)
        
        print(f'Processing cash payment of ${amount}')
        print('Payment success...')

def handle_payment(
    payment_processor: OnlinePaymentProcessor|OfflinePaymentProcessor,
    amount: int
):
    payment_processor.process_payment(amount)