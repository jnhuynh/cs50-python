def is_valid(s):
    valid = True

    # Max 6 characters
    valid = valid and len(s) < 6
    # Min 2 characters
    valid = valid and len(s) > 2
    # First 2 characters are letters
    valid = valid and s[0].isalpha() and s[1].isalpha()

    digits_only = False
    # No numbers between letters
    for c in s:
        if c.isdigit():
            if not digits_only:
                digits_only = True

                if int(c) == 0:
                    valid = False
        elif c.isalpha():
            # Found letter after digit, invalid
            if digits_only:
                valid = False
        # Not a digit or letter so invalid
        else:
            valid = False

    return valid


def main():
    # Prompt
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')


if __name__ == "__main__":
    main()
