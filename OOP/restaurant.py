class Restaurant():
    """Простая модель ресторана."""

    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибуты restaurant_name, cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, quantity):
        """Устанавливает количество обслуженых клиентов"""
        self.number_served = quantity


    def increment_number_served(self, quan):
        self.number_served += quan
        print(quan)

    def read(self):
        print(str(self.number_served))


    def describe_restaurant(self):
        """Описывает ресторан"""
        print('Our restaurant ' + self.restaurant_name.title() + ' like ' + self.cuisine_type + ' cuisine')

    def open_restaurant(self):
        """Информирует что ресторан открыт"""
        print('Restaurant ' + self.restaurant_name.title() + ' is open now!!!')

class IceCreamStand(Restaurant):
    """Простая модель киоска с мороженым"""

    def __init__(self, restaurant_name, cuisine_type):
        self.flavours = ['d', 'f', 'g']
        super().__init__(restaurant_name, cuisine_type)

    def describe_flavors(self):
        print(self.flavours)



restaurant = Restaurant('clode monet', 'Franch')
restaurant.set_number_served(55)
restaurant.increment_number_served(45)

restaurant.read()
restaurant7 = IceCreamStand('EDFE', 'WEDQ')

restaurant7.describe_flavors()
