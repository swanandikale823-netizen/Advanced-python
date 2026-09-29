class Stock:
    def __init__(self, price):
        self.price = price
        self.users = []

    def add(self, user):
        self.users.append(user)

    def remove(self, user):
        self.users.remove(user)

    def update(self, price):
        self.price = price
        print("Stock price updated:", price)

        for user in self.users:
            print("Notify:", user)


stock = Stock(100)

stock.add("Rahul")
stock.add("Aman")
stock.add("Gaurav")

stock.update(120)

stock.remove("Aman")

stock.update(150)
