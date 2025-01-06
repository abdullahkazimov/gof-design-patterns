from proxy import RealBank, BankProxy

real_bank = RealBank()
bank_proxy_authenticated = BankProxy(True, real_bank)
bank_proxy_not_authenticated = BankProxy(False, real_bank)

bank_proxy_authenticated.operation()

bank_proxy_not_authenticated.operation()