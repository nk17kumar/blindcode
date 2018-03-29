import subprocess
import sys
import os

class Operation:

    path = os.path.abspath("../resources")

    @staticmethod
    def run_compiler(lang):
        p = Operation.path
        out = open(p+"/out.txt","w")
        err = open(p+"/err.txt","w")
        fin = open(p +"/in.txt","r")
        rerr = open(p+ "/rerr.txt","w")
        err.flush()
        p1 = p + "/code"
        if lang == "python":
            path1 = p + "/code.py"
            subprocess.call(["python",path1],stdout=out,stderr=err,stdin=fin)
        if lang == "c++":
            path1 = p + "/code.cpp"
            sr = subprocess.call(["g++",path1,"-o",p1],stderr=err)
            sr = subprocess.call([p1],stdout=out,stderr=rerr,stdin=fin)
        if lang == "java":
            path1 = p + "/code.java"
            sr = subprocess.call(["javac",path1],stderr=err)
            sr = subprocess.call(["java","-cp",p,"code"],stdout=out,stderr=rerr,stdin=fin)
        if lang == "c":
            path1 = p + "/code.c"
            sr = subprocess.call(["g++",path1,"-o",p1],stderr=err)
            sr = subprocess.call([p1],stdout=out,stderr=rerr,stdin=fin)
        out.close()
        err.close()
        fin.close()
        rerr.close()
        rerr = open(p+"/rerr.txt","r")
        err = open(p+"/err.txt","r")
        compiling_err = ""
        compiling_err = err.read()
        run_err = ""
        run_err = rerr.read()
        if compiling_err == "" and run_err == "":
            return "no_err"
        if run_err == "" :
            return "cm_err"
        return "rn_err"

    @staticmethod
    def check_ac():
        p = Operation.path
        f1 = open(p+"/out.txt","r")
        f2 = open(p+"/output.txt","r")
        # s1 = f1.read().strip()
        # s2 = f2.read().strip()
        # if(s1 == s2):
        #     return True
        # else:
        #     return False
        count = 0
        total = 0
        for line1 in f2 :
            total+=1
            if line1 == f1.readline() :
                count+=1
                print "testcase %d : Accepted" %(total)
            else :
                print "testcase %d : Wrong Answer" %(total)
        score = 100*(float(count)/total)
        return score

    @staticmethod
    def show_compilation_err(compiled):
        p = Operation.path
        if compiled == "cm_err" :
            err = open(p+"/err.txt","r")
        else :
            err = open(p+"/rerr.txt","r")
        errors = err.read()
        print errors
        
