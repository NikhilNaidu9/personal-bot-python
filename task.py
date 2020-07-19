import time
import threading

class Task:
    task = []
    reminder = []

    current_time = time.time()

    def add_task(self):
        print('Enter your tasks: ')
        print('Type quit to exit')
        while True:
            temp_task = input('Task: ')
            if temp_task == "quit":
                break
            else:
                self.task.append(temp_task)
                print(self.task)

    def remove_task(self):
        print('Your tasks: ', self.task)
        print('Remove task: ')
        print('Type quit to exit')
        while True:
            num = input('Enter task number to remove: ')
            if num == 'quit':
                break
            else:
                self.task.pop(int(num) - 1)
                print(self.task)



    """def add_reminder(self):
        print('Add Remainder')
        hr = input('Enter the hour: 1 - 24')
        minute = input('Enter the min: 1 - 60')
        converted_seconds = int(hr) * 3600 + int(minute) * 60
        reminder_end_time = self.current_time + converted_seconds
        self.reminder.append(reminder_end_time)
        t1 = threading.Thread(target=self.time_check)
        t1.setDaemon(True)
        t1.start()

    def time_check(self):
        current_time = time.time()
        while True:
            if current_time < self.reminder[0]:
                print('checking')
            elif self.reminder[0] >= self.current_time:
                print('time up')
                break
            current_time = time.time()"""


task = Task()
# task.add_task()
# task.remove_task()
