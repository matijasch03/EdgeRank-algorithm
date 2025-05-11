from login import *

if __name__ == '__main__':

    logged_person = login()

    if logged_person:
        view_menu()
        option = input('\nChoose the number of option you wish: ')

        while option != 'x' and option != 'X':
            if option == '1':
                view_posts()
            elif option == '2':
                search()
            else:
                print('Error. You chose a wrong option.')

            view_menu()
            option = input('\nChoose the number of option you want: ')

        print('\nYou logged out successfully. Goodbye.')
