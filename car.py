class FuelTank:

    def __init__(self):
        self.__capacity = 50
        self.__current_level = 0
        # self.current_level = current_level

    def fill_up(self, amount_fuel: float) -> None:
        self.__current_level += amount_fuel
        if self.__current_level > self.__capacity:
            self.__current_level = self.__capacity

    def get_capacity(self) -> float:
        return self.__capacity

    def get_current_level(self) -> str:
        percent: float = (self.__current_level * 100) / self.__capacity
        return f"{percent}%"

    def __str__(self) -> str:
        return f"Bak: Pojemnosc zbiornika wynosi: {self.__capacity}, twój aktualny stan paliwa wynosi: {self.get_current_level()}"


class Engine:
    def __init__(self):
        self.__running = False

    def turn_on(self) -> None:
        self.__running = True

    def turn_off(self) -> None:
        self.__running = False

    def __str__(self) -> str:
        return f"Silnik: wlaczony {self.__running}"


class Auto:
    # pass  # -> piszemy jeżeli chcemy aby klasa przez jakiś czas była pusta
    # , dotyczy to metod, klass (ciało po : z wcięciem )
    def __init__(self):
        self.__engine = Engine()
        self.__tank = FuelTank()

    # todo zrobic wszystkie pomocnicze metody

    def info(self) -> str:
        return f"Auto: {self.__engine}, {self.__tank}"

    # todo lepsze bo nie trzeba jawnie tego wywoływać
    def __str__(self) -> str:
        return f"Auto: {self.__engine}, {self.__tank}"


my_fuel_tank: FuelTank = FuelTank()
# todo pokazać w taki sposób bez użycia toStringa
# print(fuel_tank.capacity)
my_engine: Engine = Engine()
my_auto: Auto = Auto()
my_fuel_tank.fill_up(15)
my_engine.turn_off()
print(my_fuel_tank)
print(my_engine)
print(my_auto)
