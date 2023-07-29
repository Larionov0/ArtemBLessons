powerbanks_data = [
    {
        "name": "Quasar Powerbank QTEJ-01",
        "capacity": 10000,
        "price": 100,
        "weight": 200,
        "color": "black",
        "is_wireless": False,
        "is_waterproof": False,
        "is_quick_charge": True,
        "is_led_indicator": True,
    },
    {
        "name": "Xenon Xtreme Powerbank XYZ-02",
        "capacity": 20000,
        "price": 150,
        "weight": 350,
        "color": "white",
        "is_wireless": True,
        "is_waterproof": False,
        "is_quick_charge": False,
        "is_led_indicator": True,
    },
    {
        "name": "HyperCharge Powerbank HJH-03",
        "capacity": 15000,
        "price": 130,
        "weight": 250,
        "color": "red",
        "is_wireless": False,
        "is_waterproof": True,
        "is_quick_charge": True,
        "is_led_indicator": False,
    },
    {
        "name": "Kinetix Lite Powerbank KLP-04",
        "capacity": 5000,
        "price": 70,
        "weight": 120,
        "color": "blue",
        "is_wireless": True,
        "is_waterproof": False,
        "is_quick_charge": False,
        "is_led_indicator": False,
    },
    {
        "name": "Reliant Tech Powerbank RTY-05",
        "capacity": 30000,
        "price": 200,
        "weight": 400,
        "color": "silver",
        "is_wireless": False,
        "is_waterproof": True,
        "is_quick_charge": True,
        "is_led_indicator": True,
    }
]


max_capacity = 0
# Find the most capable powerbank
for powerbank in powerbanks_data:
    if powerbank['capacity'] > max_capacity:
        max_capacity = powerbank['capacity']

print(max_capacity)
