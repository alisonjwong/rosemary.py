from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Flour, Egg, Milk, Butter, Salt

# Instructions for pancakes
# Ingredients: 250 grams of Flour, 2 eggs, 500 ml milk, butter, salt.
# 1. Whisk the eggs until frothy.
# 2. Add a dash of salt.
# 3. Add flour in batches of 50 grams while mixing.
# 4. First mix half the milk, then the remaining half.
# 5. Pre-grease the pan with butter. 
# 6. Make 8 pancakes. 
# 7. Flip the pancakes. 
# 8. Cook for 60 seconds per side.

bowl = Bowl.use(name='batch')
for i in range(2):
    egg = Egg.take()
    egg.crack()
    bowl.add(egg)
bowl.add(Salt.take('dash'))
bowl.mix()

for i in range(5):
    flour = Flour.take(grams=50)
    bowl.add(flour)
bowl.mix()

for i in range (2):
    milk = Milk.take(ml=250)
    bowl.add(milk)
bowl.mix()

Rosemary.taste(bowl)
plate = Plate.use(name = 'pancakes')

for i in range (8):
    greased_pan = Pan.use(name = 'pancake')
    greased_pan.add(Butter.take('slice'))
    greased_pan.add(bowl.take('1/8'))
    greased_pan.cook(minutes = 1)
    greased_pan.flip()
    greased_pan.cook(minutes = 1)
    plate.add(greased_pan.take())

Rosemary.serve(plate)
