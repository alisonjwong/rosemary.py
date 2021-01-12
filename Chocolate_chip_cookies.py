from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl, Oven, BakingTray
from kitchen.ingredients import Butter, Sugar, Egg, Salt, Flour, ChocolateChips, BakingPowder

# Instructions for chocolate chip cookies
# Ingredients: One part butter, 200 grams of sugar, two eggs, pinch of salt, 300 grams of flour, 200 grams of chocolate chips, and baking powder.
# 1. Preheat the oven at 175 degrees celcius.
# 2. Place one part butter in a bowl.
# 3. Add little bits of sugar at a time into the bowl.
# 4. Mix with the butter until the batter is smooth.
# 5. Add two eggs in the bowl and mix. 
# 6. Add a pinch of salt in the bowl. 
# 7. Add 300 grams of flour and mix. Do this in batches.
# 8. Add 200 grams of chocolate chips and mix.
# 9. Add baking powder.
# 10. Scoop the batter and place on baking tray, leaving some room between each. 
# 11. Cook for 10 minutes on 175 degrees celcius. 
# 12. Let it cool before serving.  

bowl = Bowl.use(name='batter')
for i in range(4):
    butter = Butter.take(grams=100)
    bowl.add(butter)
bowl.mix()

for i in range (4):
     sugar = Sugar.take(grams=50)
     bowl.add(sugar)
bowl.add(Salt.take('a pinch'))
bowl.mix()

for i in range(5):
    flour = Flour.take(grams=60)
    bowl.add(flour)
bowl.mix()

for i in range(5):
    chocolatechips = ChocolateChips.take(grams=40)
    bowl.add(chocolatechips)
bowl.add(BakingPowder.take('a pinch'))
bowl.mix()

Rosemary.taste(bowl)

plate  = Plate.use(name = 'baked chocolate chip cookies')

preheated_oven = Oven.use(degrees=175)
baking_tray = BakingTray.use(name = 'chocolate chip cookies')
for i in range (16):
    baking_tray.add(bowl.take('1/16'))

preheated_oven.add(baking_tray)
preheated_oven.bake(minutes=10)
plate.add(baking_tray.take())

Rosemary.serve(plate)
