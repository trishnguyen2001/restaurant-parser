class Restaurant():
    ingredient_prices = {
        "beef" : 10.50,
        "potato" : 0.99, 
        "rice" :  4.99,
        "chicken" : 7.99,
        "asparagus" : 4.99,
        "lettuce" : 3.99,
        "tomato" : 0.99,
        "cucumber" : 0.99,
        "broccoli" : 1.99,
        "salmon" : 8.99,
        "pasta" : 5.35,
    }

    cooking_method = {
        1 : "sear",
        2 : "boil",
        3 : "bake"
    }

    def __init__(self):
        self.balance = 1000.00
        self.ingredient_inventory = ["salt", "pepper", "sugar"]
        self.dish_inventory = []
        

    def setBalance(self, balance):
        self.balance = float(balance)

    def setIngrList(self, ingredient_inventory):
        self.ingredient_inventory = ingredient_inventory

    def setDishList(self, dish_inventory):
        self.dish_inventory = dish_inventory

    # Restaurant cooks a new dish
    # OP_NEWDISH
    def cook(self, name, ingr_list, price, cooking_method, temp, cooking_time):
        self.dish_inventory.append(
            Dish(name, ingr_list, price, cooking_method, temp, cooking_time))

    # Restaurant buys an ingredient for a certain price
    # OP_BUY
    def buy(self, quantity, ingredient):
        i = 0
        while(i < quantity):
            self.ingredient_inventory.append(ingredient)
            i+=1
        self.balance -= quantity * self.ingredient_prices[ingredient]
        return "Bought " + ingredient + " (" + str(quantity) + ")"

    # Restaurant sells a dish for a certain price
    # OP_SELL
    def sell(self, dish, price):
        if (self.dish_inventory.__contains__(dish)):
            self.dish_inventory.remove(dish)
            self.balance += price

    # Returns all ingredients and dishes the restaurant has
    def get_inventory(self):
        return self.ingredient_inventory
    
    def new_dish(self, price, temperature):
        self.dish_inventory.append(
            Dish( price, temperature))


class Dish():
    def __init__(self, price, temp):
        #self.name = name
        # self.ingr_list = ingr_list
        self.price = price
        #self.cooking_method = cooking_method
        self.temp = temp
        #self.cooking_time = cooking_time
