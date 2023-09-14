FRUIT_MAP = {
    'apple': 130,
    'avocado': 50,
    'banana': 110,
    'cantaloupe': 50,
    'grapefruit': 60,
    'grapes': 90,
    'honeydew melon': 50,
    'kiwifruit': 90,
    'lemon': 15,
    'lime': 20,
    'nectarine': 60,
    'orange': 80,
    'peach': 60,
    'pear': 100,
    'pineapple': 50,
    'plums': 70,
    'strawberries': 50,
    'sweet cherries': 100,
    'tangerine': 50,
    'watermelon': 80
}


def find_calories(string):
    fruit_key = string.lower().strip()
    if fruit_key in FRUIT_MAP:
        return FRUIT_MAP[fruit_key]
    else:
        return None


def main():
    # Prompt
    input_string = input('Fruit: ')
    calories = find_calories(input_string)

    if calories is None:
        print('Fruit not found')
    else:
        print(f'Calories: {calories}')


if __name__ == '__main__':
    main()
