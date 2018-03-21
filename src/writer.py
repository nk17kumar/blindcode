class writer:

    @staticmethod
    def write_code(lang,code):
        ext = ""
        if lang == "python":
            ext = "py"
        if lang == "c++":
            ext = "cpp"
        if lang == "java":
            ext = "java"
        if lang == "c":
            ext = "c"
        filename = "resources/code." + ext
        fin = open(filename,"w")
        fin.write(code)
        fin.close()
