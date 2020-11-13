from continent.Continent import Continent


class Country:

    def __init__(self, name: str, continent: Continent):
        self.__name = name
        self.__continent = continent

    @property
    def name(self):
        return self.__name

    @property
    def continent(self):
        return self.__continent

    def __str__(self):
        return "{} ({})".format(self.name, self.continent.name)