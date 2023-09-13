def do_something(string):
    print('Doing something')


def valid(string):
    return True


def prompt():
    while True:
        input_string = input('Give me input: ')

        if valid(input_string):
            return input_string


def main():
    # Prompt
    input_string = prompt()
    do_something(input_string)


if __name__ == "__main__":
    main()
