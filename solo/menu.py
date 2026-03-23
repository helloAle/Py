# criar um menu


class Menu:
    def __init__(self):
        pass

    def inicio(self):
        choose = int(input(f'\nMenu:\n1) option 1\n2) option 2\n3) option 3\n           '))
        if choose == 1:
            print(f'option {choose}')
        elif choose == 2:
            print(f'option {choose}')
        elif choose == 3:
            print(f'option {choose}')
        else:
            print(f'{choose} invalid option\n\n')
            return self.inicio()


menu = Menu()
menu.inicio()