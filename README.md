# MFR (Map, Filter, Reduce)

Just a silly example of using `map`, `filter`, and `reduce` in python...


```
$ python mfr.py 
>>> my_food
[🐮, 🐔, 🐟, 🐷, 🌽, 🥔]
>>> list(map(Food.cook, my_food))
[🍖, 🍗, 🍢, 🥩, 🍿, 🍟]
>>> list(filter(Food.is_vegitarian, my_food))
[🍿, 🍟]
>>> reduce(Food.eat, my_food)
💩
```
