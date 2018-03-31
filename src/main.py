import subprocess
import os

class project_path:

	__path = "/home/csevirus/project/blindcode/src"

	@staticmethod
	def set_path(path):
		project_path.__path = path

	@staticmethod
	def get_path():
		return project_path.__path

path = project_path.get_path()
os.chdir(path)

from user import *
from hidden import *
from writer import *
from compiler import *

user=User()
sr = subprocess.call(["clear"])
time_left = 300
while time_left > 0 :
	print "Enter $ to exit, start your code you have %d seconds to complete : " %(time_left)
	writer.write_code(user.get_lang(),hidden.blind_string(user))
	compiled=Operation.run_compiler(user.get_lang())
	time_left = 300 - user.get_time()
	print ""
	if compiled == "no_err" :
		AC = Operation.check_ac()
		AC += 10
		if AC != 10.0 :
			if time_left > 0 :
				AC += 0.1*float(time_left)
			print "Compiled and accepted"
			user.set_status("Compiled and Accepted")
		else :
			print "compiled - Wrong Answer"
			user.set_status("Compiled - Wrong Answer")
		print "score : %.2f " %(AC)
		user.set_score(AC)
	elif compiled == "cm_err" :
		print "Compilation Error"
		Operation.show_compilation_err(compiled)
		user.set_status("compilation error")
		print "Try Again"
	else :
		print "Runtime Error"
		Operation.show_compilation_err(compiled)
		user.set_status("Runtime Error")
		AC = Operation.check_ac()
		AC += 10
		if time_left > 0 :
			AC += 0.1*float(time_left)
		print "score : %.2f " %(AC)
		user.set_score(AC)
	writer.open_file()
	print "Time left : %d seconds" %(time_left)
	loop = raw_input("Want to continue Y/N : ")
	sr = subprocess.call(["clear"])
	if loop == 'N' or loop == 'n' :
		break
user.update_data()
print user
z = raw_input("Press Any Key then enter to exit")