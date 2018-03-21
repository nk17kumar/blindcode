import sys
import getch


class hidden:
    @staticmethod
    def blind_string():
        passwor = ''
        text = ''
        while True:
            x = getch.getch()
            if x == '\r':
                text = text + passwor + "\n"
                passwor = ''
            if x == '$':
                break
            print "*",
            passwor +=x
            text+=passwor
        return passwor
