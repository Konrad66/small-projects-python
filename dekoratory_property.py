class FuelTank:

    def __init__(self):
        self.__capacity = 50
        self.__current_level = 0

    @property
    def capacity(self) -> float:
        return self.__capacity

    @property
    def current_level(self) -> float:
        return self.__current_level

    @current_level.setter
    def current_level(self, new_level) -> None:
        if 0 <= new_level <= self.__capacity:
            self.__current_level = new_level
        else:
            print(f"Poziom paliwa musi być między 0 a {self.__capacity}")

    def fill_up(self, __amount_fuel: float) -> None:
        if __amount_fuel <= self.__capacity:
            self.__current_level += __amount_fuel
        else:
            print(f"Poziom paliwa musi być między 0 a {self.__capacity}")

    def __str__(self) -> str:
        percent: float = (self.__current_level * 100) / self.__capacity
        return f"Bak: Pojemnosc zbiornika wynosi: {self.__capacity}, twój aktualny stan paliwa wynosi: {self.__current_level} co daje {percent}%"


class Engine:
    def __init__(self):
        self.__running = False

    @property
    def running(self) -> bool:
        return self.__running

    @running.setter
    def running(self, state) -> None:
        if isinstance(state, bool):
            self.__running = state
        else:
            raise ValueError("Running musi byc typu boolean")

    def turn_on(self) -> None:
        self.__running = True

    def turn_off(self) -> None:
        self.__running = False

    def __str__(self) -> str:
        return f"Silnik: wlaczony {self.__running}"


class Auto:
    def __init__(self):
        self.__engine = Engine()
        self.__tank = FuelTank()

    @property
    def engine(self) -> Engine:
        return self.__engine

    @property
    def fuel_tank(self) -> FuelTank:
        return self.__tank

    @engine.setter
    def engine(self, engine: Engine) -> None:
        self.__engine = engine

    @fuel_tank.setter
    def fuel_tank(self, tank: FuelTank) -> None:
        self.__tank = tank


    def fill_up(self, amount_fuel: float) -> None:
        self.__tank.fill_up(amount_fuel)

    def turn_on_engine(self) -> None:
        self.__engine.turn_on()

    def turn_off_engine(self) -> None:
        self.__engine.turn_off()

    def info(self) -> str:
        return f"Auto: {self.__engine}, {self.__tank}"

    def __str__(self) -> str:
        return f"Auto: {self.__engine}, {self.__tank}"


my_auto: Auto = Auto()
my_auto.get_fuel_tank().fill_up(50)
print(my_auto.get_fuel_tank().current_level)
print(my_auto.get_engine())
print(my_auto.info())
my_auto.turn_off_engine()
my_auto.fill_up(40)
my_auto.turn_on_engine()