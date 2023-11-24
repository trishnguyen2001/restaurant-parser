class Restaurant():
    def __init__(self):
        self.balance = 1000.00
        self.ingredient_inventory = []
        self.dish_inventory = []

    def setBalance(self, balance):
        self.balance = balance

    def setIngrList(self, ingredient_inventory):
        self.ingredient_inventory = ingredient_inventory

    def setDishList(self, dish_inventory):
        self.dish_inventory = dish_inventory

    # Restaurant cooks a new dish
    def cook(self, name, ingr_list, price, cooking_method, temp, cooking_time):
        self.dish_inventory.append(
            Dish(name, ingr_list, price, cooking_method, temp, cooking_time))

    # Restaurant buys an ingredient for a certain price
    def buy(self, ingredient, price):
        self.ingredient_inventory.append(ingredient)
        self.balance -= price

    # Restaurant sells a dish for a certain price
    def sell(self, dish, price):
        if (self.dish_inventory.__contains__(dish)):
            self.dish_inventory.remove(dish)
            self.balance += price

    # Returns all ingredients and dishes the restaurant has
    def get_inventory(self):
        return self.ingredient_inventory.append(self.dish_inventory)


class Dish():
    def __init__(self, name, ingr_list, price, cooking_method, temp, cooking_time):
        self.name = name
        self.ingr_list = ingr_list
        self.price = price
        self.cooking_method = cooking_method
        self.temp = temp
        self.cooking_time = cooking_time
