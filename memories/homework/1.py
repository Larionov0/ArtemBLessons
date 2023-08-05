from pprint import pprint


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
    },
{
        "name": "Reliant Tech Powerbank RTY-06",
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


def power_bank_efficiency(powerbanks_data):
    power_bank_efficiency = 0
    power_bank_name = None
    for powerbank in powerbanks_data:
        if powerbank['capacity'] / powerbank['price'] > power_bank_efficiency:
            power_bank_efficiency = powerbank['capacity'] / powerbank['price']
            power_bank_name = powerbank['name']
    print(power_bank_name)


# power_bank_efficiency(powerbanks_data)


def price_filter(powerbanks_data, minprice, maxprice):
    allowed_powebanks = []
    for powerbank in powerbanks_data:
        if minprice <= powerbank['price'] <= maxprice:
            allowed_powebanks.append(powerbank['name'])
    print(allowed_powebanks)


# price_filter(powerbanks_data,100,180)


def color_filter(powerbanks_data):
    power_bank_colors = {}
    for powerbank in powerbanks_data:
        try:
            color = powerbank['color']
        except KeyError:
            continue

        if color in power_bank_colors:
            power_bank_colors[color] += 1
        else:
            power_bank_colors[color] = 1

    print(power_bank_colors)


# color_filter(powerbanks_data)


def sort_powerbanks(powerbanks_data, parameter):
    assert parameter in ['capacity', 'price', 'weight']

    powerbanks_data.sort(key=lambda powerbank: powerbank[parameter], reverse=True)

    # bubble sort
    # for ogr in range(len(powerbanks_data) - 1, 0, -1):
    #     for i in range(ogr):
    #         if powerbanks_data[i][parameter] > powerbanks_data[i + 1][parameter]:
    #             powerbanks_data[i], powerbanks_data[i + 1] = powerbanks_data[i + 1], powerbanks_data[i]

    return powerbanks_data


pprint(sort_powerbanks(powerbanks_data, 'price'))
