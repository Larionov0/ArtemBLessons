class Powerbank:
    def __init__(self, name, capacity, price, weight, color, is_waterproof, is_quick_charge, is_led_indicator):
        self.name = name
        self.capacity = capacity
        self.current_capacity = capacity
        self.price = price
        self.weight = weight
        self.color = color
        self.is_waterproof = is_waterproof
        self.is_quick_charge = is_quick_charge
        self.is_led_indicator = is_led_indicator

    def charge(self, amount):
        self.current_capacity += amount
        if self.current_capacity > self.capacity:
            self.current_capacity = self.capacity

    def discharge(self, amount):
        """
        returns amount of energy that was transferred
        """
        if self.current_capacity - amount < 0:
            amount = self.current_capacity
            self.current_capacity = 0
            return amount
        else:
            self.current_capacity -= amount
            return amount

    def __str__(self):
        return f"Powerbank {self.name} with capacity {self.current_capacity} / {self.capacity} mAh"

    def __repr__(self):
        return f'<{self.__str__()}>'

    def __eq__(self, other):
        return self.capacity == other.capacity

    def __gt__(self, other):  # >
        return self.capacity > other.capacity

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __ge__(self, other):
        return self.capacity >= other.capacity

    def __le__(self, other):
        return self.capacity <= other.capacity

    def __ne__(self, other):
        return self.capacity != other.capacity


class WirelessPowerbank(Powerbank):
    def __init__(self, name, capacity, price, weight, color, is_waterproof, is_quick_charge, is_led_indicator,
                 coeficient):
        super().__init__(name, capacity, price, weight, color, is_waterproof, is_quick_charge, is_led_indicator)
        self.coeficient = coeficient

    def wireless_discharge(self, amount):
        """
        returns amount of energy that was transferred
        """
        returns = self.discharge(amount)
        return returns * self.coeficient

    def __str__(self):
        return f"Wireless powerbank {self.name} with capacity {self.current_capacity} / {self.capacity} mAh (coeficient {self.coeficient})"


powerbank1 = Powerbank("Xenon Xtreme Powerbank XYZ-02", 20000, 150, 350, "white", True, False, False, )
powerbank2 = Powerbank("HyperCharge Powerbank HJH-03", 15000, 130, 250, "red", False, True, True, )
powerbank3 = Powerbank("Kinetix Lite Powerbank KLP-04", 5000, 70, 120, "blue", True, False, False, )
powerbank4 = WirelessPowerbank("Reliant Tech Powerbank RTY-05", 10000, 200, 400, "silver", True, True, True, 0.8)

powerbanks = [powerbank1, powerbank2, powerbank3]

powerbank1.current_capacity = 10000

powerbank1.charge(1000)

# print(powerbank1.current_capacity)


print(powerbank4)
print(powerbank4.wireless_discharge(1000))
print(powerbank4)

