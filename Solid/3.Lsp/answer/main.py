from payment import CashPayment, CreditCardPayment, PayPalPayment, handle_payment

if __name__ == '__main__':
    handle_payment(CreditCardPayment(), 50_000)
    print()
    
    handle_payment(PayPalPayment(), 69_000)
    print()
    
    handle_payment(CashPayment(), 42_000)    
    print()