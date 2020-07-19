import services
from exercise import Exercise

auth = services.Authentication()
# comment something something

db = services.Database()
ex = Exercise()


class Bot:

    email = ''
    password = ''
    user_data = {
        'name': '',
        'age': '',
        'gender': '',
    }

    @staticmethod
    def greet_user(greet, user_name):
        print('Bot - Greet User')
        print(greet, user_name)

    def ask_auth_mode(self):
        print('Bot - Auth Mode User')
        user_choice = input('Do u want to login or register ? 1 == login, 0 == register \n')

        if int(user_choice) == 1:
            self.user_input()
            if auth.check_for_password_length(self.password):
                self.sign_in_user()
            else:
                print('Check ur password length')
        elif int(user_choice) == 0:
            self.user_input()
            if auth.check_for_password_length(self.password):
                self.register_user()
                self.ask_for_user_data()
                print(self.user_data['name'])
                self.write_file(self.user_data['name'])
                self.store_user_data()
                self.ask_for_service()

            else:
                print('Check ur password length')
        else:
            print('Please choose a Valid Input')

    def user_input(self):
        print('Bot - User Input')
        self.email = input('Enter Your Email: ')
        self.password = input('Enter Your Password: ')

    def ask_for_user_data(self):
        print('Bot - User data')
        self.user_data['name'] = input('Your name: ')
        self.user_data['age'] = input('Your age: ')

        gender = input('gender \n M = Male \n F = Female \n')

        if gender == 'M':
            self.user_data['gender'] = 'Male'
        else:
            self.user_data['gender'] = 'Female'

    def register_user(self):
        print('Bot - Register User')
        auth.create_user_account(self.email, self.password)


    def sign_in_user(self):
        print('Bot - Sign In User')
        auth.log_user_account(self.email, self.password)

    def store_user_data(self):
        db.store_user_details(self.user_data)

    def read_file(self):
        user_logged_in = open('user_logged_in.txt', 'r')
        return user_logged_in.read()

    def write_file(self, name):
        user_logged_in = open('user_logged_in.txt', 'w')
        user_logged_in.write(name)

    def ask_for_service(self):
        ex.ask_for_user_input(self.user_data['name'])
        ex.ask_for_user_choice()


bot = Bot()
user_name = bot.read_file()
bot.greet_user('HI', user_name)
bot.ask_auth_mode()


