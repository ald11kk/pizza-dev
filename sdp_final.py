class TruckDelivery:
    def send_goods(self):
        return "Грузовик"

class TruckAdapter:
    def __init__(self, truck_delivery):
        self.truck_delivery = truck_delivery

    def deliver(self):
        return self.truck_delivery.send_goods()

# Singleton Pattern - конфигуратор пиццы
class PizzaConfigurator:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(PizzaConfigurator, cls).__new__(cls)
            cls._instance.ingredients = []
            cls._instance.delivery_strategy = None
        return cls._instance

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def set_delivery_strategy(self, delivery_strategy):
        self.delivery_strategy = delivery_strategy

    def get_pizza_configuration(self):
        return f"Ваша пицца с {', '.join(self.ingredients)}."

# Strategy Pattern - способы доставки
class BicycleDelivery:
    def deliver(self):
        return "Доставка на велосипеде"

class CarDelivery:
    def deliver(self):
        return "Доставка на автомобиле"

# Decorator Pattern - изменение начинки пиццы
class PizzaDecorator:
    def __init__(self, pizza, extra_ingredient):
        self.pizza = pizza
        self.extra_ingredient = extra_ingredient

    def get_pizza_configuration(self):
        return f"{self.pizza.get_pizza_configuration()} с {self.extra_ingredient}"

# Observer Pattern - уведомление об успешной оплате
class PaymentObserver:
    def update(self, message):
        print(f"Уведомление: {message}")

# Factory Pattern - создание новых видов начинки для пиццы
class PizzaFactory:
    def create_ingredient(self, name):
        return name


def main():
    pizza_configurator = PizzaConfigurator()
    delivery_strategy = None
    payment_observer = PaymentObserver()

    pizza_factory = PizzaFactory()

    print("Здравствуйте, Добро пожаловать в PizzaDev. Выберите начинку для пиццы.")
    print("1. Сыр 2. Ветчина 3. Курица 4. Красный лук 5. Огурчики")
    
    ingredients_input = input("Введите числа через пробел (например, 1 3 4): ").split()
    selected_ingredients = [pizza_factory.create_ingredient(ingredient) for ingredient in ingredients_input]

    for ingredient in selected_ingredients:
        pizza_configurator.add_ingredient(ingredient)

    print("Выберите способ доставки: 1. Велосипед 2. Автомобиль 3. Грузовик")
    delivery_choice = input("Введите 1, 2 или 3: ")

    if delivery_choice == '1':
        delivery_strategy = BicycleDelivery()
    elif delivery_choice == '2':
        delivery_strategy = CarDelivery()
    elif delivery_choice == '3':
        truck_delivery = TruckDelivery()
        delivery_strategy = TruckAdapter(truck_delivery)

    pizza_configurator.set_delivery_strategy(delivery_strategy)
    print(delivery_strategy.deliver())

    # Итог
    print("\n------------------------------------------")
    print("\nИтог заказа:")
    print(f"Ваш заказ: {pizza_configurator.get_pizza_configuration()}")

    
    if delivery_strategy:
        print(f"Способ доставки: {delivery_strategy.deliver()}")
        print("\n------------------------------------------")


    # Оплата
    print("\nВыберите способ оплаты: 1. Наличными 2. Картой")

    payment_choice = input("Введите 1 или 2: ")

    if payment_choice == '2':
        while True:
            card_number = input("Введите 16-значный номер карты: ")
            if len(card_number) == 16 and card_number.isdigit():
                break
            else:
                print("Ошибка! Введите корректный 12-значный номер карты.")

        payment_observer.update("Оплата прошла успешно.")

if __name__ == "__main__":
    main()
