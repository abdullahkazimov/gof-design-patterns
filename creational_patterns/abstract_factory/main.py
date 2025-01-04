from abstract_factory import BrandFactory, Laptop, Phone, AppleFactory, SamsungFactory

def create_brand_products(factory: BrandFactory):
    smartphone = factory.create_smartphone()
    laptop = factory.create_laptop()

    print(smartphone.call())
    print(laptop.start())

create_brand_products(AppleFactory())
create_brand_products(SamsungFactory())