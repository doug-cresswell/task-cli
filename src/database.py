import csv
from src.deadlined_reminders import DeadlinedReminder

def list_reminders():
    f = open("reminders.csv", "r")

    with f:
        reader = csv.reader(f)

        for row in reader:
            print()
            for e in row:
                print(e.ljust(32), end=' ')
        print()

def add_reminder(text, date, ReminderClass):
    if not issubclass(ReminderClass, DeadlinedReminder):
        msg = "Invalid Reminder Class"
        raise TypeError(msg)
    reminder = ReminderClass(text, date)
    with open('reminders.csv', 'a+', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow(reminder)

