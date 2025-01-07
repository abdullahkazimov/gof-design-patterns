from strategy import VisaPayment, PaypalPayment, Context

visa = VisaPayment()
paypal = PaypalPayment()

context = Context(visa)
context.run()
context.set_strategy(paypal)
context.run()