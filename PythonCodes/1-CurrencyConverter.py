def main():
    print('\nThis program converts USD to GBP.\n')

    dollars = eval(input('\nEnter the ammount of USD: '))

    pounds = convert_to_pounds(dollars)

    print(f'\nThat is {pounds} pounds.')


def convert_to_pounds(dollars): return dollars * 0.82
# convert_to_pounds = lambda dollars: dollars * 0.82


main()
