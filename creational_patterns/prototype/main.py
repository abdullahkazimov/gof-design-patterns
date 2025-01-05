from prototype import Phone, PrototypeRegistry

phone = Phone(10)
pr = PrototypeRegistry()

pr.add_item("phone", phone)

print(pr.get_item_deep_clone("phone"))