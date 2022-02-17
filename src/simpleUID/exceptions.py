from colorama import init, Fore

class length_value_too_long(Exception):
    def __init__(self, length=None):

        #### Init colorama
        init(autoreset=True)

        #### Create error message
        if not length == None:
            self.message = 'Randomly generated ID is longer than the maximum of {}.'.format(length)
        else:
            self.message = 'Randomly generated ID is longer than the maximum allowed length.'

        self.message += " This can be ignored but this is not recommended."
        
        super().__init__(Fore.RED + self.message)