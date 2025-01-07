from visitor import Book, Journal, TaxCalculator, CostCalculator

book = Book('a', 12, 'a', 12)
journal = Journal('b', 10, 'b', 10)

tax_calculator = TaxCalculator()
cost_calculator = CostCalculator()

taxes = book.accept(tax_calculator) + journal.accept(tax_calculator)
costs = book.accept(cost_calculator) + journal.accept(cost_calculator)

print(taxes)
print(costs)