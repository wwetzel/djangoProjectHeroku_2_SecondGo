class Product():
    def __init__(self, name, price, discountPercent):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent

    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

product1 = Product("Giant Goddamn Dildo", 15.00, 5)
product2 = Product("Raping Stick", 17.00, 20)

print("Name: {:s}".format(product1.name))
