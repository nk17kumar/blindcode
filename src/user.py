import time

class User:
    'Common base class for all employees'
    __status = "Not defined"
    __time = 0000000000
    __score = 0.0
    def __init__(self, name, roll_no, language):
        self.name = name
        self.roll_no = roll_no
    	self.language = language

    def __str__(self):
        return "User Name: " + self.name + "\n" + "Roll Number: " + str(self.roll_no) + "\n" + "Language: " + self.language + "\n" + "status: " + self.__status + "\n" + "Time Taken: " + str(self.__time) + " seconds" + "\n" + "Score : " + str(self.__score)

    def get_time(self):
       return self.__time

    def set_score(self,score):
        if self.__score < score :
            self.__score = score 

    def set_time(self, time_2b_set):
       self.__time =  time_2b_set

    def get_status(self):
       return self.__status

    def set_status(self, status_after):
        self.__status =  status_after

