import subprocess
import os

class Operation:

    __p = os.path.abspath("..") + "/resources"

    @staticmethod
    def run_compiler(lang):
        out = open(Operation.__p+"/out.txt","w")
        err = open(Operation.__p+"/err.txt","w")
        fin = open(Operation.__p+"/in.txt","r")
        rerr = open(Operation.__p+"/rerr.txt","w")
        err.flush()
        p1 = Operation.__p + "/code"
        if lang == "python":
            path1 = Operation.__p + "/code.py"
            subprocess.call(["python",path1],stdout=out,stderr=err,stdin=fin)
        if lang == "c++":
            path1 = Operation.__p + "/code.cpp"
            sr = subprocess.call(["g++",path1,"-o",p1],stderr=err)
            sr = subprocess.call([p1],stdout=out,stderr=rerr,stdin=fin)
        if lang == "java":
            path1 = Operation.__p + "/code.java"
            sr = subprocess.call(["javac",path1],stderr=err)
            sr = subprocess.call(["java","-cp",p,"code"],stdout=out,stderr=rerr,stdin=fin)
        if lang == "c":
            path1 = Operation.__p + "/code.c"
            sr = subprocess.call(["g++",path1,"-o",p1],stderr=err)
            sr = subprocess.call([p1],stdout=out,stderr=rerr,stdin=fin)
        out.close()
        err.close()
        fin.close()
        rerr.close()
        rerr = open(Operation.__p+"/rerr.txt","r")
        err = open(Operation.__p+"/err.txt","r")
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
        f1 = open(Operation.__p+"/out.txt","r")
        f2 = open(Operation.__p+"/output.txt","r")
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
        if compiled == "cm_err" :
            err = open(Operation.__p+"/err.txt","r")
        else :
            err = open(Operation.__p+"/rerr.txt","r")
        errors = err.read()
        print errors
        
