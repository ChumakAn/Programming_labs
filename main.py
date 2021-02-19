class cartonOfMilk:
    typeOfMilk = "Whole milk"

    def __init__(self, manufacturer="Unknown", fatContent="0%", amount="0 ml", calories=" 0 kcal"):
        self.manufacturer = manufacturer
        self.fatContent = fatContent
        self.amount = amount
        self.calories = calories

    def __del__(self):
        del self

    def __str__(self):
        return "manufacturer: " + self.manufacturer + "\nfat content:" \
               + self.fatContent + "\namount: " + self.amount + "\ncalories: " + self.calories

    @staticmethod
    def get_static_value():
        return cartonOfMilk.typeOfMilk


if __name__ == '__main__':
    milk1 = cartonOfMilk("Selyanochka", "3.8%", "250 ml", "53 kcal")
    print(milk1.__str__())
    print("\n")
    milk2 = cartonOfMilk()
    print(milk2.__str__())
    print("\n")
    milk3 = cartonOfMilk("Galychyna", "2.9%")
    print(milk3.__str__())
    print("\n")
