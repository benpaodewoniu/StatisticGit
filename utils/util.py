from collections import OrderedDict
from operator import *


def sort_dict(data):
    for key, items in data.items():
        print(OrderedDict(sorted(items.items(), key=lambda x: getitem(x[2], 'all'))))
    print(1)
