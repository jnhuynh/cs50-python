def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output_string = ''

    for c in string:
        if c not in vowels:
            output_string += c

    return output_string


def main():
    # Prompt
    input_string = input('Input: ')
    output_string = remove_vowels(input_string)
    print(f'Output: {output_string}')


if __name__ == "__main__":
    main()
