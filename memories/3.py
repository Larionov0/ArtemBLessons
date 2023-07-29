from collections import OrderedDict


def count_all_symbols(string):
    """
    :param string: str
    :return: dict
    :return example:
    {
        'a': 5,
        'v': 2,
        '.': 7,
        ...
    }

    alihfnaoerin oaeirnfalerinfglaerugnaleiu nearliugnabiauhg ihrelgrehgliuaher

    a 2
    l 1

    """

    counts = {}
    for symbol in string:
        if symbol in counts:
            counts[symbol] += 1
        else:
            counts[symbol] = 1

    return counts


def add_to_each_number(lst, *args, number=4, **kwargs):
    print(lst)
    print(args)
    print(number)
    print(kwargs)


print(count_all_symbols('aleoirg ;aerog;aeorga;eoirga e;oringiusehbyrgiulwoa lieurhg'))

add_to_each_number([1, 5, 2, 4], 'afe', 12, [4], 'awef', number=10, k=1, goafe=19, lists=[[], []])
