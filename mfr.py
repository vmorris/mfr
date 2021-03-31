#!/usr/bin/env python

from functools import reduce


class Food:
    def __init__(self, icon: str, is_meat: bool, is_cooked: bool = False):
        self.icon = icon
        self.is_meat = is_meat
        self.is_cooked = is_cooked
        self.is_eaten = False

    def cook(self):
        if self.is_cooked:
            return self

        if self.icon == "🐮":
            self.icon = "🍖"
        elif self.icon == "🐔":
            self.icon = "🍗"
        elif self.icon == "🐟":
            self.icon = "🍢"
        elif self.icon == "🐷":
            self.icon = "🥩"
        elif self.icon == "🌽":
            self.icon = "🍿"
        elif self.icon == "🥔":
            self.icon = "🍟"

        self.is_cooked = True
        return self

    def is_vegitarian(self):
        return not self.is_meat

    def eat(self, other):
        if other.icon == "💩":
            raise Exception("Don't eat poop!")
        return Food(icon="💩", is_meat=False)

    def __repr__(self) -> str:
        return self.icon


if __name__ == "__main__":
    my_food = [
        Food(icon="🐮", is_meat=True),
        Food(icon="🐔", is_meat=True),
        Food(icon="🐟", is_meat=True),
        Food(icon="🐷", is_meat=True),
        Food(icon="🌽", is_meat=False),
        Food(icon="🥔", is_meat=False),
    ]

    print(">>> my_food")
    print(my_food)
    print(">>> list(map(Food.cook, my_food))")
    print(list(map(Food.cook, my_food)))
    print(">>> list(filter(Food.is_vegitarian, my_food))")
    print(list(filter(Food.is_vegitarian, my_food)))
    print(">>> reduce(Food.eat, my_food)")
    print(reduce(Food.eat, my_food))
