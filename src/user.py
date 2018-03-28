class User:
    'Common base class for all employees'
    __status = "Not defined"
    __time = 10000000000
    def __init__(self, name, roll_no, language):
        self.name = name
        self.roll_no = roll_no
    	self.language = language

    def __str__(self):
        return "User Name: " + self.name + "\n" + "Roll Number: " + str(self.roll_no) + "\n" + "Language: " + self.language

    def get_time(self):
       return self.__time

    def set_time(self, time_2b_set):
       self.__time =  time_2b_set

    def get_status(self):
       return self.__status

    def set_status(self, status_after):
        self.__status =  status_after

