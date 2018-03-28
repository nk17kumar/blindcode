from user import *
from hidden import *
from writer import *
from compiler import *

name=raw_input("enter Name : ")
roll_no=raw_input("enter Roll number : ")
lang=raw_input("enter Prefered Language : ")
user=User(name,roll_no,lang)
print "Enter $ to exit, start your code you have 300 seconds to complete : "
code=hidden.blind_string(user)
writer.write_code(lang,code)
compiled=Operation.run_compiler(lang)
if compiled == True :
	print "code compiled succesfully"
	AC = Operation.check_ac()
	AC += 10
	if AC != 10.0 :
		print "code Accepted"
		user.set_status("Compiled and accepted")
	else :
		print "Wrong Answer"
		user.set_status("compiled - Wrong Answer")
	print "score : %.2f " %(AC)
else :
	Operation.show_compilation_err()
	user.set_status("compilation error")
print user


