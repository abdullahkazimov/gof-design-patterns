from decorator import SimpleCoffee, MilkDecorator, SugarDecorator

coffee = SimpleCoffee()

print(coffee.ingredients())

coffee_with_milk = MilkDecorator(coffee)

print(coffee_with_milk.ingredients())

coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)

print(coffee_with_milk_and_sugar.ingredients())