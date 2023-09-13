def to_snake(string):
    snake = ''
    for i, c in enumerate(string):
        formatted_c = c.lower()

        # Do not prefit first character with underscore
        if i != 0 and c.isupper():
            formatted_c = f'_{c.lower()}'

        snake += formatted_c

    return snake


def main():
    # Prompt
    input_string = input('camelCase: ')
    print(f'snake_case: {to_snake(input_string)}')


if __name__ == "__main__":
    main()
