#Base Classes
class Effect:
    def __init__(self, name: str, multiplier: float):
        self.name = name
        self.multiplier = multiplier





class Ingredient:
    def __init__(self, name: str, effect: str, replaces: list[tuple[str]]):
        self.name = name
        self.effect = effect
        self.replaces = replaces





class Base:
    def __init__(self, name: str, classification: str, price: int, effects: list[str]):
        self.name = name
        self.classification = classification
        self.price = price
        self.effects = effects






#Variables
Bases = [
    Base('OG Kush', 'Weed', 35, ['Calming']),
    Base('Sour Diesel', 'Weed', 35, ['Refreshing']),
    Base('Green Crack', 'Weed', 35, ['Energizing']),
    Base('Granddaddy Purple', 'Weed', 35, ['Sedating']),
    Base('Meth', 'Meth', 70, []),
    Base('Cocaine', 'Cocaine', 150, [])

]
Bases = {i.name : i for i in Bases}



Effects = [
    Effect('Shrinking', 0.6),
    Effect('Zombifying', 0.58),
    Effect('Cyclopean', 0.56),
    Effect('Anti-Gravity', 0.54),
    Effect('Long Faced', 0.52),
    Effect('Electrifying', 0.50),
    Effect('Glowing', 0.48),
    Effect('Tropic Thunder', 0.46),
    Effect('Thought-Provoking', 0.44),
    Effect('Jennerising', 0.42),
    Effect('Bright-Eyed', 0.40),
    Effect('Spicy', 0.38),
    Effect('Foggy', 0.36),
    Effect('Slippery', 0.34),
    Effect('Athletic', 0.32),
    Effect('Balding', 0.30),
    Effect('Calorie-Dense', 0.28),
    Effect('Sedating', 0.26),
    Effect('Sneaky', 0.24),
    Effect('Energizing', 0.22),
    Effect('Gingeritis', 0.20),
    Effect('Euphoric', 0.18),
    Effect('Focused', 0.16),
    Effect('Refreshing', 0.14),
    Effect('Munchies', 0.12),
    Effect('Calming', 0.10),
    Effect('Disorienting', 0),
    Effect('Explosive', 0),
    Effect('Laxative', 0),
    Effect('Lethal', 0),
    Effect('Paranoia', 0),
    Effect('Schizophrenic', 0),
    Effect('Seizure-Inducing', 0),
    Effect('Smelly', 0),
    Effect('Toxic', 0)
]
Effects = {i.name : i for i in Effects}



Ingredients = [
    Ingredient('Cuke', 'Energizing', [('Euphoric', 'Laxative'), ('Foggy', 'Cyclopean'), ('Gingeritis', 'Thought-Provoking'), ('Munchies', 'Athletic'), ('Slippery', 'Munchies'), ('Sneaky', 'Paranoia'), ('Toxic', 'Euphoric')]),
    Ingredient('Banana', 'Gingeritis', [('Calming', 'Sneaky'), ('Cyclopean', 'Thought-Provoking'), ('Disorienting', 'Focused'), ('Energizing', 'Thought-Provoking'), ('Focused', 'Seizure-Inducing'), (4, 'Refreshing'), ('Paranoia', 'Jennerising'), ('Smelly', 'Anti-Gravity'), ('Toxic', 'Smelly')]),
    Ingredient('Paracetamol', 'Sneaky', [('Calming', 'Slippery'), ('Electrifying', 'Athletic'), ('Energizing', 'Paranoia'), ('Focused', 'Gingeritis'), ('Foggy', 'Calming'), ('Glowing', 'Toxic'), ('Munchies', 'Anti-Gravity'), ('Paranoia', 'Balding'), ('Spicy', 'Bright-Eyed'), ('Toxic', 'Tropic Thunder')]),
    Ingredient('Donut', 'Calorie-Dense', [('Anti-Gravity', 'Slippery'), ('Balding', 'Sneaky'), ('Calorie-Dense', 'Explosive'), ('Focused', 'Euphoric'), ('Jennerising', 'Gingeritis'), ('Munchies', 'Calming'), ('Shrinking', 'Energizing')]),
    Ingredient('Viagor', 'Tropic Thunder', [('Athletic', 'Sneaky'), ('Disorienting', 'Toxic'), ('Euphoric', 'Bright-Eyed'), ('Laxative', 'Calming')]),
    Ingredient('Mouth Wash', 'Balding', [('Calming', 'Anti-Gravity'), ('Calorie-Dense', 'Sneaky'), ('Explosive', 'Sedating'), ('Focused', 'Jennerising')]),
    Ingredient('Flu Medicine', 'Sedating', [('Athletic', 'Munchies'), ('Calming', 'Bright-Eyed'), ('Cyclopean', 'Foggy'), ('Electrifying', 'Refreshing'), ('Euphoric', 'Toxic'), ('Focused', 'Calming'), ('Laxative', 'Euphoric'), ('Munchies', 'Slippery'), ('Shrinking', 'Paranoia'), ('Thought-Provoking', 'Gingeritis')]),
    Ingredient('Gasoline', 'Toxic', [('Energizing', 'Spicy'), ('Disorienting', 'Glowing'), ('Electrifying', 'Disorienting'), ('Euphoric', 'Energizing'), ('Gingeritis', 'Smelly'), ('Jennerising', 'Sneaky'), ('Laxative', 'Foggy'), ('Munchies', 'Sedating'), ('Paranoia', 'Calming'), ('Shrinking', 'Focused'), ('Sneaky', 'Tropic Thunder')]),
    Ingredient('Energy Drink', 'Athletic', [('Disorienting', 'Electrifying'), ('Euphoric', 'Energizing'), ('Focused', 'Shrinking'), ('Foggy', 'Laxative'), ('Glowing', 'Disorienting'), ('Schizophrenic', 'Balding'), ('Sedating', 'Munchies'), ('Spicy', 'Euphoric'), ('Tropic Thunder', 'Sneaky')]),
    Ingredient('Motor Oil', 'Slippery', [('Energizing', 'Munchies'), ('Euphoric', 'Sedating'), ('Foggy', 'Toxic'), ('Munchies', 'Schizophrenic'), ('Paranoia', 'Anti-Gravity')]),
    Ingredient('Mega Bean', 'Foggy', [('Athletic', 'Laxative'), ('Calming', 'Glowing'), ('Energizing', 'Cyclopean'), ('Focused', 'Disorienting'), ('Jennerising', 'Paranoia'), ('Seizure-Inducing', 'Focused'), ('Shrinking', 'Electrifying'), ('Slippery', 'Toxic'), ('Sneaky', 'Calming'), ('Cyclopean', 'Thought-Provoking'), ('Thought-Provoking', 'Energizing')]),
    Ingredient('Chili', 'Spicy', [('Anti-Gravity', 'Tropic Thunder'), ('Athletic', 'Euphoric'), ('Laxative', 'Long Faced'), ('Munchies', 'Toxic'), ('Shrinking', 'Refreshing'), ('Sneaky', 'Bright-Eyed')]),
    Ingredient('Battery', 'Bright-Eyed', [('Cyclopean', 'Glowing'), ('Electrifying', 'Euphoric'), ('Euphoric', 'Zombifying'), ('Laxative', 'Calorie-Dense'), ('Munchies', 'Tropic Thunder'), ('Shrinking', 'Munchies')]),
    Ingredient('Iodine', 'Jennerising', [('Calming', 'Balding'), ('Calorie-Dense'), ('Euphoric', 'Seizure-Inducing'), ('Foggy', 'Paranoia'), ('Refreshing', 'Thought-Provoking'), ('Toxic', 'Sneaky')]),
    Ingredient('Addy', 'Thought-Provoking', [('Explosive', 'Euphoric'), ('Foggy', 'Energizing'), ('Glowing', 'Refreshing'), ('Long Faced', 'Electrifying'), ('Sedating', 'Gingeritis')]),
    Ingredient('Horse Semen', 'Long Faced', [('Anti-Gravity', 'Calming'), ('Gingeritis', 'Refreshing'), ('Thought-Provoking', 'Electrifying')])
]
Ingredients = {i.name : i for i in Ingredients}






#Product Classes
class Recipe:
    def __init__(self, name: str, base: str, ingredients: list[str]):
        self.name = name
        self.base = base
        self.ingredients = ingredients
    

    @property
    def effects(self) -> list:
        allEffects = Bases[self.base].effects[:]

        for ingredient in self.ingredients:
            replacements = [replacement for replacement in Ingredients[ingredient].replaces if replacement[0] in allEffects]
            for replacement in replacements:
                allEffects.remove(replacement[0])
                allEffects.append(replacement[1])
            allEffects.append(Ingredients[ingredient].effect)
        return list(set(allEffects))
    

    @property
    def actualPrice(self) -> float:
        allEffects = self.effects
        
        multiplier = 1 + sum([Effects[effect].multiplier for effect in allEffects])
        return Bases[self.base].price * multiplier
    

    @property
    def price(self) -> str:
        price = self.actualPrice
        if str(price).split('.')[-1] == '5': price += 0.01

        priceA = int(price)
        priceB = int(round(price))

        if priceA == priceB: return f'${priceA}.0'
        return f'${priceA}.0 - {priceB}.0'
    


    def __str__(self) -> str:
        return f'{self.name}\n\nMarket Value: {self.price}\n\n\nRecipe: {', '.join(self.ingredients)}\n\n\nEffects: {', '.join(self.effects)}'