class CartonOfMilk:
    typeOfMilk = "Whole milk"
    __manufacturer = None
    __fatContent = None
    __amount = None
    __callories = None

    @staticmethod
    def get_static_value():
        return CartonOfMilk.typeOfMilk

    def __init__(self, manufacturer="Unknown", fatContent="0%", amount="0 ml", calories=" 0 kcal"):
        self.__manufacturer = manufacturer
        self.__fatContent = fatContent
        self.__amount = amount
        self.__calories = calories

    def __del__(self):
        del self

    def __str__(self):
        return "manufacturer: " + self.__manufacturer + "\nfat content:" \
               + self.__fatContent + "\namount: " + self.__amount + "\ncalories: " + self.__calories


def main():
    milk1 = CartonOfMilk("Selyanochka", "3.8%", "250 ml", "53 kcal")
    print(milk1.__str__())
    print("\n")
    milk2 = CartonOfMilk()
    print(milk2.__str__())
    print("\n")
    milk3 = CartonOfMilk("Galychyna", "2.9%")
    print(milk3.__str__())
    print("\n")


if __name__ == '__main__':
    main()
