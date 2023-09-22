def prompt():
    while True:
        input_string = input('Fraction: ')

        try:
            digits = input_string.split('/')
            percent = (int(digits[0]) / int(digits[1])) * 100

            match percent:
                case 1:
                    print('F')
                case 0:
                    print('E')
                case _:
                    print(f'{percent}%')

            break
        except (ValueError, ZeroDivisionError) as e:
            print(e)


if __name__ == '__main__':
    prompt()
