import datetime

class Time_Calculator:
    def __init__(self, time=None, formatted_time=None, Time_in_hour_minute=None):
        self.time = time
        self.formatted_time = formatted_time
        self.Time_in_hour_minute = Time_in_hour_minute


class Time_Increaser(Time_Calculator):
    def __init__(self,time=None, formatted_time=None, Time_in_hour_minute=None, seconds=None,minutes=None,hours=None):
        super().__init__(time,formatted_time,Time_in_hour_minute)
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
    
    def new_time_seconds(self):
        new_time = self.formatted_time + datetime.timedelta(seconds = int(self.seconds))
        print(f"Original time: {self.Time_in_hour_minute}")
        print(f"New time is: {new_time.time()}")

    def new_time_minutes(self):
        new_time = self.formatted_time + datetime.timedelta(minutes = int(self.minutes))
        print(f"Original time: {self.Time_in_hour_minute}")
        print(f"New time is: {new_time.time()}")

    def new_time_hours(self):
        new_time = self.formatted_time + datetime.timedelta(hours = int(self.hours))
        print(f"Original time: {self.Time_in_hour_minute}")
        print(f"New time is: {new_time.time()}")


class Time_Add(Time_Calculator):
    def __init__(self, time=None, formatted_time=None, Time_in_hour_minute=None,time2=None, formatted_time2=None,Time_in_hour_minute2=None, time2_delta=None):
        super().__init__(time,formatted_time,Time_in_hour_minute)
        self.time2 = time2
        self.formatted_time2 = formatted_time2
        self.Time_in_hour_minute2 = Time_in_hour_minute2
        self.time2_delta = time2_delta

    def print_new_time(self):
        print(f"First time value: {self.Time_in_hour_minute}\nSecond time value: {self.Time_in_hour_minute2}\nAddition of the two time values:"
              f"{(self.formatted_time + self.time2_delta).time()}")
        

class Time_Difference(Time_Calculator):
    def __init__(self, time=None, formatted_time=None, Time_in_hour_minute=None, time2=None, formatted_time2=None, Time_in_hour_minute2=None, time2_delta=None):
        super().__init__(time,formatted_time,Time_in_hour_minute)
        self.time2 = time2
        self.formatted_time2 = formatted_time2
        self.Time_in_hour_minute2 = Time_in_hour_minute2
        self.time2_delta = time2_delta

    def print_new_time(self):
        print(f"First time value: {self.Time_in_hour_minute}\nSecond time value: {self.Time_in_hour_minute2}\nDifference of the two time values:"
              f"{(self.formatted_time - self.time2_delta).time()}")


alltime = input("Enter times in HH:MM\n").split()

for time in alltime:
    hour,min = [int(i) for i in time.split(":")]

formatted_time = datetime.datetime(2024, 10, 8, hour, min)
Time_in_hour_minute = formatted_time.time()
base_time = Time_Calculator(alltime,formatted_time,Time_in_hour_minute)

choice = 0
while choice == 0:
    user_choice = input("1.  to increase time by seconds/minutes/hours\n2.  to add two time values\n3.  to get difference of two time values\n4. to exit\n")
    while user_choice == "1":
        addition_type = input("a.  to increase time by seconds\nb.  to increase time by minutes\nc.  to increase time by hours\n2.  to exit\n")
        if addition_type == "a":
            inp_seconds = input("Enter seconds: ")
            time_adder = Time_Increaser(alltime,formatted_time,Time_in_hour_minute,seconds=inp_seconds)
            time_adder.new_time_seconds()

        if addition_type == "b":
            inp_minutes = input("Enter minutes: ")
            time_adder = Time_Increaser(alltime,formatted_time,Time_in_hour_minute,minutes=inp_minutes)
            time_adder.new_time_minutes()

        if addition_type == "c":
            inp_hours = input("Enter hours: ")
            time_adder = Time_Increaser(alltime,formatted_time,Time_in_hour_minute,hours=inp_hours)
            time_adder.new_time_hours()

        if addition_type == "2":
            user_choice = 2


    if user_choice == "2":
        fst_ad_tm_value = input("Enter first time value to add in HH:MM format\n").split()
        for time in fst_ad_tm_value:
            hour1, min1 = [int(i) for i in time.split(":")]
        first_add_value = datetime.datetime(2024, 10, 8, hour1, min1)
        first_add_value_time = first_add_value.time()

        add_time_value = Time_Add(time=fst_ad_tm_value, formatted_time=first_add_value, Time_in_hour_minute=first_add_value_time)

        scnd_ad_tm_value = input("Enter second time value to add in HH:MM:SS format\n").split()
        for time in scnd_ad_tm_value:
            hour2, min2, sec2 = [int(i) for i in time.split(":")]
        scnd_add_value = datetime.datetime(2024, 10, 8, hour2, min2)
        scnd_add_value_time = scnd_add_value.time()
        scnd_add_value_delta = datetime.timedelta(hours=hour2, minutes=min2, seconds=sec2)

        add_time_value = Time_Add(time=fst_ad_tm_value, formatted_time=first_add_value,Time_in_hour_minute = first_add_value_time,\
                                  time2 = scnd_ad_tm_value, formatted_time2 = scnd_add_value, Time_in_hour_minute2=scnd_add_value_time,\
                                  time2_delta=scnd_add_value_delta)
        
        add_time_value.print_new_time()


    if user_choice == "3":
        fst_sbt_tm_value = input("Enter first time value to add in HH:MM\n").split()
        for time in fst_sbt_tm_value:
            hour3, min3 = [int(i) for i in time.split(":")]
        first_sbt_value = datetime.datetime(2024, 10, 8, hour3, min3)
        first_sbt_value_time = first_sbt_value.time()

        time_diff_value = Time_Difference(time=fst_sbt_tm_value, formatted_time=first_sbt_value, Time_in_hour_minute=first_sbt_value_time)

        scnd_sbt_tm_value = input("Enter second time value to add in HH:MM:SS\n").split()
        for time in scnd_sbt_tm_value:
            hour4, min4, sec4 = [int(i) for i in time.split(":")]
        scnd_sbt_value = datetime.datetime(2024, 10, 8, hour4, min4)
        scnd_sbt_value_time = scnd_sbt_value.time()
        scnd_sbt_value_delta = datetime.timedelta(hours=hour4, minutes=min4, seconds=sec4)

        time_diff_value = Time_Difference(time=fst_sbt_tm_value, formatted_time=first_sbt_value, Time_in_hour_minute=first_sbt_value_time,\
                                          time2 = scnd_sbt_tm_value, formatted_time2 = scnd_sbt_value, Time_in_hour_minute2=scnd_sbt_value_time,\
                                          time2_delta=scnd_sbt_value_delta)

        time_diff_value.print_new_time()


    if user_choice == "4":
        choice = 1