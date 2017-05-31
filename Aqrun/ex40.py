# -- coding: utf-8 --
"""
习题 40: 字典, 可爱的字典
"""

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return 'Not Found.'

# ok pay attension!
cities['_find'] = find_city

while True:
    print('State? (ENTER to quit)')
    state = raw_input("> ")

    if not state: break

    # this line is the most important ever! study!
    city_found = cities['_find'](cities, state)
    print(city_found)


