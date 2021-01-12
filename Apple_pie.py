from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl, Oven, Fridge, PieDish
from kitchen.ingredients import Water, Flour, Salt, Butter, Apple, Sugar, Lemon, Cornstarch, Cinnamon, Egg 

# Instructions for chocolate chip cookies
# Ingredients: Chilled water, 300 grams of flour, a teaspoon salt, 250 grams of butter, 6 apples, one lemon, 150 grams + 1 spoon of sugar, a spoonful of cornstarch, a pinch of salt, a teaspoon of cinnamon, one egg. 
# 1. Preheat the oven at 180 degrees celcius.
# 2. Prepare some cold water.
# 3. Mix 300 grams of flour together with a teaspoon of salt, and gradually add 250 grams of butter while kneading the dough.
# 4. Gradually add the chilled water.
# 5. Leave the dough to chill in the fridge. 
# 6. Peel 6 apples, and zest and juice a lemon. 
# 7. Add the sliced applies, 150 grams of sugar, a spoonful of cornstarch, a pinch of salt, a teaspoon of cinnamon, and parts of the lemon juice and zest together. 
# 8. Cover the bottom of a pie dish with 3/4 of the chilled crust dough.
# 9. Add filling, and add remainder of dough on top.
# 10. In another bowl, crax and mix an egg, add a spoon of sugar, and the remainder of the lemon zest over the top of the pie. 
# 11. Put in the oven for 60 minutes.   

fridge = Fridge.use()
bowl_water = Bowl.use(name = 'water')
bowl_water.add(Water.take(ml = 200))
fridge.add(bowl_water)
chilled_water = fridge.take() 

bowl_dough = Bowl.use(name = 'dough')
bowl_dough.add(Flour.take(grams = 300))
bowl_dough.add(Salt.take('a teaspoon'))
for i in range (5):
    butter = Butter.take(grams = 50)
    bowl_dough.add(butter)
    bowl_dough.mix()
bowl_dough.add(bowl_water.take())

Rosemary.taste(bowl_dough)

chilled_dough = fridge.add(bowl_dough)

bowl_filling = Bowl.use(name = "filling")
for i in range (6):
    apple = Apple.take()
    apple.peel()
    apple.slice()
    bowl_filling.add(apple)

lemon = Lemon.take()
zest = lemon.zest()
juice = lemon.squeeze()
bowl_filling.add(zest)
bowl_filling.add(juice)
bowl_filling.add(Sugar.take(grams = 150))
bowl_filling.add(Cornstarch.take('a spoonful'))
bowl_filling.add(Salt.take('a pinch'))
bowl_filling.add(Cinnamon.take('a teaspoon'))
bowl_filling.mix()

Rosemary.taste(bowl_filling)

plate  = Plate.use(name = 'hot apple pie')

preheated_oven = Oven.use(degrees=180)
pie_dish = PieDish.use(name = 'apple pie')
pie_dish.add(bowl_filling)

bowl_topping = Bowl.use(name = 'topping')
egg = Egg.take()
egg.crack()
bowl_topping.add(egg)
bowl_topping.add(zest)
bowl_topping.add(juice)
bowl_topping.add(Sugar.take('a spoonful'))
bowl_topping.mix()

Rosemary.taste(bowl_topping)

pie_dish.add(bowl_topping)

preheated_oven.add(pie_dish)
preheated_oven.bake(minutes=60)
plate.add(pie_dish.take())

Rosemary.taste(pie_dish)



bowl_topping = Bowl.use(name = 'topping')
egg = Egg.take()
egg.crack()
bowl_topping.add(egg)
bowl_topping.add(zest)
bowl_topping.add(juice)
bowl_topping.add(Sugar.take('a spoonful'))
bowl_topping.mix()

Rosemary.taste(bowl_topping)
