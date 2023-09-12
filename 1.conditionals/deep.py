# Prompt for input
user_input = input(
    'What is the Answer to the Great Question of Life, the Universe, and Everything? ')

# Convert to lowercase, won't impact int
user_input = user_input.lower()

# Remove all spaces
user_input = user_input.replace(' ', '')

match user_input:
    case '42' | 'forty-two' | 'fortytwo':
        print('Yes')
    case _:
        print('No')
