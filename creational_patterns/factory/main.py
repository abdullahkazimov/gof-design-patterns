from factory import Kitchen, AsianCuisine, ItalianCuisine

def run(kitchen: Kitchen):
    print(kitchen.operation())

run(AsianCuisine())

run(ItalianCuisine())