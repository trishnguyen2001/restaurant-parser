class Restaurant():
    ingredient_prices = {
        "beef" : 5.50,
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
        "flour" : 1.99
    }

    dish_prices = {
        "Tee's Salmon" : 19.50, 
        "Trish's Chicken" : 18.00, 
        "Spaghetti" : 16.00, 
        "Ravioli" : 17.00, 
        "TNT Burger" : 18.35, 
        "Skinny Salad" : 17.25,
    }

    recipes = {
        "Tee's Salmon" : ["salmon", "asparagus", "rice"], 
        "Trish's Chicken" : ["chicken", "broccoli", "rice"], 
        "Spaghetti" : ["pasta", "beef", "tomato"], 
        "Ravioli" : ["beef", "pasta", "tomato"], 
        "TNT Burger" : ["beef", "lettuce", "tomato"], 
        "Skinny Salad" : ["lettuce", "cucumber", "tomato", "chicken"],
    }

    temps = {
        "Tee's Salmon" : [380, 420], 
        "Trish's Chicken" : [550, 650],
        "Spaghetti" : [212, 212], 
        "Ravioli" : [212, 212], 
        "TNT Burger" : [550, 650], 
        "Skinny Salad" : [0, 0],
    }

    cooking_methods = {
        "Tee's Salmon" : "bake", 
        "Trish's Chicken" : "sear",
        "Spaghetti" : "boil", 
        "Ravioli" : "boil", 
        "TNT Burger" : "sear", 
        "Skinny Salad" : "none",
    }

    cooking_times = {
        "Tee's Salmon" : 25, 
        "Trish's Chicken" : 15,
        "Spaghetti" : 8, 
        "Ravioli" : 8, 
        "TNT Burger" : 12, 
        "Skinny Salad" : 0,
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
    def new_dish(self, dish, cooking_method, temp, cooking_time):
        verdict = self.check_cooking(dish, cooking_method, temp, cooking_time)

        if(verdict == "Wow! You cooked that dish perfectly!"):
            if(self.has_ingredients(dish)):
                self.dish_inventory.append(dish)
                for i in self.recipes[dish]:
                    self.ingredient_inventory.remove(i)
                return verdict + " (1 " + dish + " has been added to your inventory)"
            else:
                verdict = "You don't have the necessary ingredients"
        return verdict + " (Cooking failed)"

    # Helper method to check if user has all necessary ingredients
    def has_ingredients(self, dish):
        for i in self.recipes[dish]:
            if(i not in self.ingredient_inventory):
                return False
        return True
    
    # Helper method to check cooking method, temp, and time for a dish
    def check_cooking(self, dish, method, temp, time):
        if(dish == "Skinny Salad" and temp != 0):
            return "Why are you trying to make a salad over heat...?"
        if(method != self.cooking_methods[dish]):
            return "That's not the right way to cook this dish... Try again with a different cooking method"
        if(temp < self.temps[dish][0] - 10): #buffer of 10 degrees
            return "You're going to undercook this dish... Try again with a higher temperature"
        if(temp > self.temps[dish][1] + 10): #buffer of 10 degrees
            return "You're going to overcook this dish... Try again with a lower temperature"
        if(time < self.cooking_times[dish] - 2): #buffer of 2 mins
            return "You need to cook this dish for longer..."
        if(time > self.cooking_times[dish] + 2): #buffer of 2 mins
            return "You need to cook this dish for a shorter amount of time..."
        return "Wow! You cooked that dish perfectly!"

    # Restaurant buys an ingredient for a certain price
    # OP_BUY
    def buy(self, quantity, ingredient):
        i = 0
        if(ingredient in self.ingredient_prices):
            while(i < quantity):
                self.ingredient_inventory.append(ingredient)
                i+=1
            self.balance -= quantity * self.ingredient_prices[ingredient]
            return "Bought " + ingredient + " (" + str(quantity) + ")"
        else:
            return "Ingredient not in our approved ingredients list."
        

    # Restaurant sells a dish for a certain price
    # OP_SELL
    def sell(self, quantity, dish):
        i = 0
        sold = 0
        disclaimer = ""

        if (dish in self.dish_inventory):
            while(i < quantity):
                sold+=1
                self.dish_inventory.remove(dish)
                self.balance += self.dish_prices[dish]
            i+=1
        
        if(sold == 0):
            return "You don't have that dish in your inventory!"
        
        if(sold < quantity):
            disclaimer = " (Only had " + str(sold) + "/" + str(quantity) + " in your inventory)"
        
        return "Sold " + str(sold) + " " + dish + disclaimer
        

    # Returns all ingredients and dishes the restaurant has
    def get_inventory(self):
        return self.ingredient_inventory + self.dish_inventory

