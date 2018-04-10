import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials

class User:
    __reg_no = ""
    __name = ""
    __roll_no = ""
    __language = ""
    __status = "Not defined"
    __time = 0
    __score = 0.0
    __start_time = 0
    __path = os.path.abspath("..") + "/resources"

    def __init__(self):
        self.__reg_no = raw_input("Enter Regestration No : ")
        self.__name = raw_input("Enter Name : ")
        self.__roll_no = raw_input("Enter Roll number : ")
    	self.__language = raw_input("Enter Prefered Language : ")

    def __str__(self):
        return "Regestration No: " + str(self.__reg_no) + "\n" + "User Name: " + self.__name + "\n" + "Roll Number: " + str(self.__roll_no) + "\n" + "Language: " + self.__language + "\n" + "status: " + self.__status + "\n" + "Time Taken: " + str(self.__time) + " seconds" + "\n" + "Final Score : " + str(self.__score)

    def get_time(self):
       return self.__time

    def set_time(self, time_2b_set):
       self.__time =  time_2b_set

    def get_stime(self):
       return self.__start_time

    def set_stime(self, time_2b_set):
       self.__start_time =  time_2b_set

    def get_score(self) : 
        return self.__score

    def set_score(self,score):
        if self.__score < score :
            self.__score = score

    def get_status(self):
       return self.__status

    def set_status(self, status_after):
        if self.__status == "Not defined" :
            self.__status =  status_after
        elif self.__status == "compilation error" :
            self.__status =  status_after
        elif self.__status == "Compiled - Wrong Answer" and status_after == "Compiled and Accepted":
            self.__status =  status_after

    def get_lang(self):
        return self.__language

    def update_data(self):
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.__path+'/BlindCode-6a1c6b8f83f7.json', scope)
        gc = gspread.authorize(credentials)
        wks = gc.open("BlindCode").sheet1
        cells = "A" + str(int(self.__reg_no)+1) + ":G" + str(int(self.__reg_no)+1)
        cell_list = wks.range(cells)
        cell_list[0].value = self.__reg_no
        cell_list[1].value = self.__name
        cell_list[2].value = self.__roll_no
        cell_list[3].value = self.__language
        cell_list[4].value = self.__status
        cell_list[5].value = self.__time
        cell_list[6].value = self.__score
        wks.update_cells(cell_list)




   