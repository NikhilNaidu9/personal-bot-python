import authenticate

auth = authenticate.Authentication()


class Bot:

    email = ''
    password = ''

    @staticmethod
    def greet_user(greet):
        print('Bot - Greet User')
        print(greet)

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
            else:
                print('Check ur password length')
        else:
            print('Please choose a Valid Input')

    def user_input(self):
        print('Bot - User Input')
        self.email = input('Enter Your Email: ')
        self.password = input('Enter Your Password: ')

    def register_user(self):
        print('Bot - Register User')
        auth.create_user_account(self.email, self.password)

    def sign_in_user(self):
        print('Bot - Sign In User')
        auth.log_user_account(self.email, self.password)


bot = Bot()
bot.greet_user('HI')
bot.ask_auth_mode()

