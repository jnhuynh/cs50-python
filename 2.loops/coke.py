def main():
    amount_due = 50

    while amount_due > 0:
        print(f'Amount Due: {amount_due}')
        input_string = input('Insert Coin: ')

        input_amount = int(input_string)

        match input_amount:
            case 5 | 10 | 25:
                amount_due -= input_amount
            case _:
                input_amount = 0

    print(f'Change Owed: {abs(amount_due)}')


if __name__ == "__main__":
    main()
