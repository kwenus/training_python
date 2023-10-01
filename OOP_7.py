from math import radians, sin, cos, acos

class Point:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    # рассчет растояния между двумя точками
    def distance(self, other):
        cos_d = sin(self.latitude) * sin(other.latitude) + cos(self.latitude) * cos(other.latitude) * cos(self.longitude) * cos(other.longitude)
        return 6371 * acos(cos_d)

class City(Point):
    def __init__(self, latitude, longitude, name, population):
        super().__init__(latitude, longitude)
        self.name = name
        self.population = population

    def show(self):
        print(f'City {self.name}, population {self.population}')

class Mountain(Point):
    def __init__(self, latitude, longitude, name, height):
        super().__init__(latitude, longitude)
        self.name = name
        self.height = height

    def show(self):
        print(f'Height of mountain {self.name} is {self.height}.')

# функция для вывода расстояния
def print_how_far(geo_object_1, geo_object_2):
    print(f'Distance from point 1 "{geo_object_1.name}" to point 2 "{geo_object_2.name}" - {geo_object_1.distance(geo_object_2)}km')

geo_object_1 = City(55.7522200, 37.6155600, 'Moscow', 13104177)
geo_object_2 = Mountain(27.98791, 86.92529, 'Everest', 8848)
geo_object_3 = City(55.154, 61.4291,'Chelyabinsk', 1182517)

geo_object_1.show()
geo_object_2.show()
geo_object_3.show()
print_how_far(geo_object_1, geo_object_2)
print_how_far(geo_object_1, geo_object_3)



