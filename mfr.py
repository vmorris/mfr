#!/usr/bin/env python

from functools import reduce


class Food:
    def __init__(self, name: str, icon: str, is_meat: bool, is_cooked: bool = False):
        self.name = name
        self.icon = icon
        self.is_meat = is_meat
        self.is_cooked = is_cooked
        self.is_eaten = False

    def cook(self):
        if self.is_cooked:
            return self

        if self.name == "cow":
            self.name = "beef"
            self.icon = "🍖"
        elif self.name == "chicken":
            self.name = "drumstick"
            self.icon = "🍗"
        elif self.name == "fish":
            self.name = "oden"
            self.icon = "🍢"
        elif self.name == "pig":
            self.name = "porkchop"
            self.icon = "🥩"
        elif self.name == "corn":
            self.name = "popcorn"
            self.icon = "🍿"
        elif self.name == "potato":
            self.name = "fries"
            self.icon = "🍟"
        self.is_cooked = True
        return self

    def is_vegitarian(self):
        return not self.is_meat

    def eat(self, other):
        return Food(name="poop", icon="💩", is_meat=False)

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return self.icon


if __name__ == "__main__":
    my_food = [
        Food(name="cow", icon="🐮", is_meat=True),
        Food(name="chicken", icon="🐔", is_meat=True),
        Food(name="fish", icon="🐟", is_meat=True),
        Food(name="pig", icon="🐷", is_meat=True),
        Food(name="corn", icon="🌽", is_meat=False),
        Food(name="potato", icon="🥔", is_meat=False),
    ]

    print(">>> my_food")
    print(my_food)
    print(">>> list(map(Food.cook, my_food))")
    print(list(map(Food.cook, my_food)))
    print(">>> list(filter(Food.is_vegitarian, my_food))")
    print(list(filter(Food.is_vegitarian, my_food)))
    print(">>> reduce(Food.eat, my_food)")
    print(reduce(Food.eat, my_food))
