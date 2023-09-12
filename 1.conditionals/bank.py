def greeting_payment(greeting=''):
    # Cleanup input
    greeting = greeting.lower().strip()

    # Find occurence of hello
    if greeting.startswith('hello'):
        return 0

    # Find occurence of leading `h`
    if greeting.startswith('h'):
        return 20

    # Improper greeting, pay full amount
    return 100


def main():
    # Prompt for greeting
    greeting = input('What is your greeting? ')

    amount = greeting_payment(greeting)
    print(f'${amount}')


main()
