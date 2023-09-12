# Get input
raw_input = input('Enter an emoticon: ')

# Format input
formatted_input = raw_input.replace(':)', '🙂')
formatted_input = formatted_input.replace(':(', '😐')

# Print formatted input
print(f"Emojied: {formatted_input}")
