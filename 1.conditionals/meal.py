def main():
    # Prompt for time
    input_string = input('What is the time? ')
    time = convert(input_string)

    # Determine meal
    if 7 <= time <= 8:
        print('Breakfast')
    elif 12 <= time <= 13:
        print('Lunch')
    elif 18 <= time <= 19:
        print('Dinner')


def convert(time_string):
    base_hours = 0

    # Check for AM/PM
    meridiem_components = time_string.split(' ')

    # Convert string to time
    components = meridiem_components[0].split(':')
    hours = float(components[0])
    minutes = float(components[1])

    if len(meridiem_components) == 2:
        meridiem = meridiem_components[1].lower()

        if meridiem == 'pm':
            base_hours = 12

        # 12AM is 0 hours with base hours 0, 12PM is 0 hours with base hours 12
        if hours == 12:
            hours = 0

    return base_hours + hours + (minutes / 60)


if __name__ == "__main__":
    main()
