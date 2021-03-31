from abc import ABC, abstractmethod
from functools import reduce
from operator import methodcaller
from typing import Sequence, Tuple, Union


class SupportsBellsAndWhistles(ABC):

    def __init__(self, name: str, icon: str):
        self._name = name
        self._icon = icon

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return self._icon


class MetabolicProduct(SupportsBellsAndWhistles):

    _processed: Tuple['Food', ...]

    def __init__(self, name: str, icon: str, processed: Tuple['Food', ...]):
        super().__init__(name, icon)
        self._processed = processed

    @abstractmethod
    def process(self, food: 'Food') -> 'MetabolicProduct':
        ...

class Hungry(MetabolicProduct):
  
    def __init__(self):
        super().__init__('hungry', '😋', ())

    def process(self, food: 'Food') -> 'Poop':
        return Poop((food, ))

HUNGRY = Hungry()

class Food(SupportsBellsAndWhistles):
    def __init__(self, name: str, icon: str, is_meat: bool, is_cooked: bool):
        super().__init__(name, icon)
        self._is_meat = is_meat
        self._is_cooked = is_cooked

    @abstractmethod
    def cook(self) -> 'Food':
        ...

    def is_vegetarian(self) -> bool:
        return not self._is_meat

class RawFood(Food):
    def __init__(self, name: str, icon: str, is_meat: bool):
        super().__init__(name, icon, is_meat, False)
        

class CookedFood(Food):
    def __init__(self, name: str, icon: str, is_meat: bool):
        super().__init__(name, icon, is_meat, True)

    def cook(self) -> 'CookedFood':
        return self

class Poop(MetabolicProduct):

    def __init__(self, processed: Tuple[Food, ...]):
        super().__init__("poop", "💩", processed)

    def process(self, food: 'Food') -> Union['Poop', 'ShitHeap']:
        digested = (*self._processed, food)
        return Poop(digested) if len(digested) < 5 else ShitHeap(digested)

class ShitHeap(MetabolicProduct):

    def __init__(self, processed: Tuple[Food, ...]):
        super().__init__("shit heap", "💩💩", processed)

    def process(self, food: 'Food') -> 'ShitHeap':
        return ShitHeap((*self._processed, food))


class Beef(CookedFood):
    def __init__(self):
        super().__init__("beef", "🍖", True)

BEEF = Beef()        

class Drumstick(CookedFood):
    def __init__(self):
        super().__init__("drumstick", "🍗", True)

DRUMSTICK = Drumstick()        

class Porkchop(CookedFood):
    def __init__(self):
        super().__init__("porkchop", "🥩", True)

PORKCHOP = Porkchop()        

class Oden(CookedFood):
    def __init__(self):
        super().__init__("oden", "🍢", True)

ODEN = Oden()        

class Popcorn(CookedFood):
    def __init__(self):
        super().__init__("popcorn", "🍿", True)

POPCORN = Popcorn()        

class Fries(CookedFood):
    def __init__(self):
        super().__init__("fries", "🍟", True)

FRIES = Fries()        

class Cow(RawFood):
    def __init__(self):
        super().__init__("cow", "🐮", True)

    def cook(self) -> Beef:
        return BEEF

COW = Cow()

class Chicken(RawFood):
    def __init__(self):
        super().__init__("chicken", "🐔", True)

    def cook(self) -> Drumstick:
        return DRUMSTICK

CHICKEN = Chicken()

class Fish(RawFood):
    def __init__(self):
        super().__init__("fish", "🐟", True)

    def cook(self) -> Oden:
        return ODEN

FISH = Fish()

class Pig(RawFood):
    def __init__(self):
        super().__init__("pig", "🐷", True)

    def cook(self) -> Porkchop:
        return PORKCHOP

PIG = Pig()

class Corn(RawFood):
    def __init__(self):
        super().__init__("corn", "🌽", False)

    def cook(self) -> Popcorn:
        return POPCORN

CORN = Corn()

class Potato(RawFood):
    def __init__(self):
        super().__init__("potato", "🥔", False)

    def cook(self) -> Fries:
        return FRIES

POTATO = Potato()

def cook(food: Food) -> Food:
    return food.cook()

def is_vegetarian(food: Food) -> bool:
    return food.is_vegetarian()

def eat(intermediate_product: MetabolicProduct, food: Food) -> MetabolicProduct:
    return intermediate_product.process(food)

if __name__ == "__main__":

    MY_FOOD: Sequence[Food] = (
        COW,
        CHICKEN,
        FISH,
        PIG,
        CORN,
        POTATO
    )

    print(">>> MY_FOOD")
    print(MY_FOOD)
    print(">>> tuple(map(cook, MY_FOOD))")
    print(tuple(map(cook, MY_FOOD)))

    print(">>> tuple(filter(is_vegitarian, MY_FOOD))")
    print(tuple(filter(is_vegetarian, MY_FOOD)))

    print(">>> reduce(eat, vegetarian)")
    print(reduce(eat, filter(is_vegetarian, MY_FOOD), HUNGRY))

    print(">>> reduce(eat, everything)")
    print(reduce(eat, MY_FOOD, HUNGRY))

    # sanity checks for the happy programmer
    assert str(COW) == str(Cow())
    assert str(BEEF) == str(Beef())

    # same as above but without a helper function

    print("---- no helper functions")

    print(">>> MY_FOOD")
    print(MY_FOOD)
    print(">>> tuple(map(cook, MY_FOOD))")
    print(tuple(map(methodcaller('cook'), MY_FOOD)))

    print(">>> tuple(filter(is_vegitarian, MY_FOOD))")
    print(tuple(filter(methodcaller('is_vegetarian'), MY_FOOD)))

    print(">>> reduce(eat, vegetarian)")
    print(reduce(eat, filter(methodcaller('is_vegetarian'), MY_FOOD), HUNGRY))

    # I am not aware of any built-in way
    #print(">>> reduce(eat, everything)")
    #print(reduce(methodcaller('process'), MY_FOOD, HUNGRY))
    