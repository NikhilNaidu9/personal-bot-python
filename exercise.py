import services
import time


class Exercise:
    personal_info = {
        'height': '',
        'weight': '',
    }

    db = services.Database()

    exercise_list = ['biceps', 'triceps', 'abs', 'legs', 'fat burning', 'weight gain', 'meditation', 'yoga']

    def ask_for_user_input(self, name):
        self.personal_info['height'] = float(input('Enter your height :'))
        self.personal_info['weight'] = float(input('Enter your weight :'))
        self.db.store_user_personal_info(self.personal_info, name)
        print('added succesfully')

    def ask_for_user_choice(self):
        print('Which exercise you want to prefer :')
        print(self.exercise_list)

        choice = input('Enter your choice : ')
        print(choice)

        if choice == self.exercise_list[0]:
            print('welcome to the biceps training')
        elif choice == self.exercise_list[1]:
            print('welcome to the triceps training')
        elif choice == self.exercise_list[2]:
            print('welcome to the abs training')
            self.abs_routine()
        elif choice == self.exercise_list[3]:
            print('welcome to the legs training')
        elif choice == self.exercise_list[4]:
            print('welcome to the weight gaining training')
        elif choice == self.exercise_list[5]:
            print('welcome to the burning training')
        elif choice == self.exercise_list[6]:
            print('welcome to the meditation training')
        elif choice == self.exercise_list[7]:
            print('welcome to the yoga training')
        else:
            print('Please enter a valid choice')

    def abs_routine(self):
        print('Jumping Jacks - 20 Seconds')
        self.timer(20)
        print('Break - 15 Seconds')
        self.timer(15)

    @staticmethod
    def timer(timer):
        i = 1
        while i <= timer:
            print(i)
            time.sleep(1)
            i += 1
