
class AlarmClock:

    def __init__(self):
        self.current_time = "1200"                                                      
        self.alarm_on = False
        self.alarm_time = "1200"

    def set_current_time(self, new_time):
        self.current_time = new_time
        print(f'The current time is now: {self.current_time}') 

    def toggle_alarm(self):
        self.alarm_on = not self.alarm_on
        if self.alarm_on:
            print("Your alarm is on!")
        else:
            print("Your alarm is off!") 
    
    def set_alarm_time(self, new_time):
        self.alarm_time = new_time
        print(f"Enter new alarm time: {self.alarm_time}")



    