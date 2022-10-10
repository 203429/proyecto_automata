import transitions as dfa
import os

validated_lines = []
path_items = []

def get_paths():
    path = ".\examples"
    for dir, subdir, files in os.walk(path):
        for file in files:
            filepath = os.path.join(dir, file)
            validated_lines.append(filepath)
            read_file(filepath)
            validated_lines.append("<>")

def read_file(filepath):
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            validate_automata(line.strip())
            line = fp.readline()

def validate_automata(text):
    if dfa.dfa.accepts_input(text):
        validated_lines.append(text)

def separate_list():
    temp = []
    for x in range(len(validated_lines)):
        if validated_lines[x] != '<>':
            temp.append(validated_lines[x])
        else:
            path_items.append(temp)
            temp = []

def write_txt():
    f = open("Reporte.txt","a+")
    for x in path_items:
        for j in range(len(x)):
            if j==0:
                f.write("Importaciones encontradas en: " + x[0] + "\n")
            else:
                w = x[j].split()
                if w[0] == 'import':
                    for l in w:
                        if l != 'import':
                            if ',' in l:
                                l = l.replace(",","")
                            f.write("> " + l + "\n")
                else:
                    a = []
                    for l in w:
                        a_temp = l.replace("from",">")
                        f.write(a_temp + " ")
                    # f.write(a)
                    f.write("\n")
                    # f.write(x[j] + "\n")
    f.write("-----------------------------------------------------------------------------------")
    f.close()

get_paths()
separate_list()
write_txt()