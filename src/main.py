from user import *
from hidden import *
from writer import *
from compiler import *

name=raw_input("enter Name : ")
roll_no=raw_input("enter Roll number : ")
lang=raw_input("enter Prefered Language : ")
user=User(name,roll_no,lang)
print "Enter $ to exit, start your code : "
code=hidden.blind_string()
writer.write_code(lang,code)
compiled=Operation.run_compiler(lang)
if compiled == True :
	print "code compiled succesfully"
	AC = Operation.check_ac()
	AC += 10
	if AC != 10.0 :
		print "code Accepted"
	else :
		print "Wrong Answer"
	print "score : %.2f " %(AC)
else :
	Operation.show_compilation_err()

