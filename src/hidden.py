import sys
import getch
import time
from user import *


class hidden:
    @staticmethod
    def blind_string(user):
        passwor = ''
        text = ''
        start_time = int(time.time()) - user.get_time()
        time_now = int(time.time())-start_time
        while time_now <= 300 :
            x = getch.getch()
            if x == '\r':
                text = text + passwor + "\n"
                passwor = ''
            if x == '$':
                break
            print "*",
            passwor +=x
            text+=passwor
            time_now = int(time.time())-start_time
        time_now = int(time.time())-start_time
        user.set_time(time_now)
        return passwor
