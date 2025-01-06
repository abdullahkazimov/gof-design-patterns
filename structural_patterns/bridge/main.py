from bridge import WebPlatform, MobilePlatform, CashPayment, CardPayment

web_platform = WebPlatform()
mobile_platform = MobilePlatform()
cash_payment = CashPayment(web_platform)
card_payment = CardPayment(mobile_platform)

cash_payment.pay()
card_payment.pay()