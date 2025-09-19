class PayPalPayment:
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"

class StripePayment:
    def process_payment(self, amount):
        return f"Processing ${amount} via Stripe"

class CreditCardPayment:
    def process_payment(self, amount):
        return f"Processing ${amount} via Credit Card"

class GooglePayPayment:
    def process_payment(self, amount):
        return f"Processing ${amount} via Google Pay"

# Factory class to create payment processors
class PaymentFactory:
    @staticmethod
    def get_payment_processor(payment_method):
        if payment_method == "paypal":
            return PayPalPayment()
        elif payment_method == "stripe":
            return StripePayment()
        elif payment_method == "credit_card":
            return CreditCardPayment()
        elif payment_method == "google_pay":
            return GooglePayPayment()
        else:
            raise ValueError(f"Unknown payment method: {payment_method}")

def checkout(payment_method, amount):
    # Use factory to get the appropriate payment processor
    processor = PaymentFactory.get_payment_processor(payment_method)
    return processor.process_payment(amount)

if __name__ == "__main__":
    try:
        print(checkout("paypal", 100))  # Output: Processing \$100 via PayPal
        print(checkout("stripe", 200))  # Output: Processing \$200 via Stripe
        print(checkout("credit_card", 300))  # Output: Processing \$300 via Credit Card
        print(checkout("google_pay", 400))  # Output: Processing \$400 via Google Pay
    except ValueError as e:
        print(e)
