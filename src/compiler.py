import subprocess
import sys
import os

class Operation:

    path = os.path.abspath("../resources")

    @staticmethod
    def run_compiler(lang):
        p = Operation.path
        out = open(p+"/out.txt","w")
        err = open(p+"/err.txt","r+")
        fin = open(p +"/in.txt","r")
        if lang == "python":
            path1 = p + "/code.py"
            subprocess.call(["python",path1],stdout=out,stderr=err,stdin=fin)
        if lang == "c++":
            p1 = p + "/code"
            path1 = p + "/code.py"
            sr = subprocess.call(["g++",path1,"-o",p1],stdout=out,stderr=err,stdin=fin)
        if lang == "java":
            path1 = p + "/code.java"
            sr = subprocess.call(["javac",path],stdout=out,stderr=err,stdin=fin)
        if lang == "c":
            path1 = p + "/code.c"
            sr = subprocess.call(["g++",path,"-o",p1],stdout=out,stderr=err,stdin=fin)

        if(lang == "java"):
            sr = subprocess.call(["java",p+"/code"])

        compiling_err = err.read()

        if compiling_err == "":
            return True
        else:
            return False

    @staticmethod
    def check_ac():
        p = Operation.path
        f1 = open(p+"/out.txt","r")
        f2 = open(p+"/output.txt","r")
        s1 = f1.read().strip()
        s2 = f2.read().strip()
        if(s1 == s2):
            return True
        else:
            return False

    @staticmethod
    def show_compilation_err():
        p = Operation.path
        err = open(p+"/err.txt","r")
        errors = err.read()
        print errors
        
print Operation.run_compiler("python")
print Operation.check_ac()
