class PizzaMaker:
    def make_pizza(self):
        self.step1()
        self.step2()
        self.step3()
        self.step4()
        print("Your pizza is ready!")

    def step1(self):
        pass

    def step2(self):
        pass

    def step3(self):
        pass

    def step4(self):
        pass

class ItalianPizzaMaker(PizzaMaker):
    def step1(self):
        print("Step 1 Italiano")

class MexicanPizzaMaker(PizzaMaker):
    def step3(self):
        print("Step 3 Mexicano")
    
    def step5(self):
        print("Step 5 Mexicano")