from state import Order


order = Order()

order.process()
order.next()
order.next()
order.next()
order.cancel()

print()

order = Order()

order.process()
order.next()
order.next()
order.cancel()

print()

order = Order()
order.process()
order.next()
order.cancel()

print()

order = Order()
order.process()
order.cancel()