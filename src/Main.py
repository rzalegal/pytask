from continent.Continent import Continent
from counrty.Country import Country
from q.MyQueue import MyQueue


def main():
    numbers = MyQueue()
    countries = MyQueue()

    numbers.add(5)
    numbers.add(4)
    numbers.add(3)
    numbers.add(2)
    numbers.add(1)

    countries.add(Country("Russia", Continent.Asia))
    countries.add(Country("Sweden", Continent.Europe))
    countries.add(Country("Poland", Continent.Europe))
    countries.add(Country("Germany", Continent.Europe))
    countries.add(Country("Peru", Continent.South_America))

    print(numbers.to_list())
    print(countries.to_list())