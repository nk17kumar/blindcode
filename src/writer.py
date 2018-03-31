import os
import subprocess

class writer:

    __filename = os.path.abspath("..") + "/resources/code."
    __ext = ""

    @staticmethod
    def write_code(lang,code):
        if lang == "python":
            writer.__ext = "py"
        if lang == "c++":
            writer.__ext = "cpp"
        if lang == "java":
            writer.__ext = "java"
        if lang == "c":
            writer.__ext = "c"
        fin = open(writer.__filename+writer.__ext,"w")
        fin.write(code)
        fin.close()

    @staticmethod
    def open_file():
        # filename = os.path.abspath("..") + "/resources/code."
        # ext = ""
        # if lang == "python":
        #     ext = "py"
        # if lang == "c++":
        #     ext = "cpp"
        # if lang == "java":
        #     ext = "java"
        # if lang == "c":
        #     ext = "c"
        sr = subprocess.call(["gedit",writer.__filename+writer.__ext])
        
        
        
