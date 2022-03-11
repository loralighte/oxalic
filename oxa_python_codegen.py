def oxa_py3_codegen(file):
    # Codegen Stage 1: Replace syntax
    python_codegen = []
    for i in file:
        if " " in i:
            i = i.replace(" ", "_")
            python_codegen.append(i)
        elif i == ":":
            i = i.replace(":", "=")
            python_codegen.append(i)
        elif i == "=":
            i = i.replace("=", "==")
            python_codegen.append(i)
        elif i == ";":
            # Will be used later
            python_codegen.append(i)
        elif i.startswith("\"") and i.startswith("\""):
            python_codegen.append(i)
        elif i == "[":
            i = i.replace("[", "print(")
            python_codegen.append(i)
        elif i == "]":
            i = i.replace("]", ")")
            python_codegen.append(i)
        else:
            python_codegen.append(i)
    
    # Codegen Stage 2: Creating print
    python_printline = []
    is_print = False
    python_print = ''
    for i in python_codegen:
        if not is_print and i == "print(":
            is_print = True
            python_print = python_print + i
        elif is_print and i == ")":
            is_print = False 
            python_print = python_print + i
        elif is_print and i != "print(" and i != ")":
            python_print = python_print + i + ","
        elif not is_print and python_print and i != "print(" and i != ")":
            python_printline.append(python_print)
            python_print = ''
            python_printline.append(i)
        elif not is_print and not python_print and i != "print(" and i != ")":
            python_printline.append(i)

        for x in python_printline:
            python_printline[python_printline.index(x)] = x.replace(",)",")")
            x = x.replace(",)",")")
            python_printline[python_printline.index(x)] = x.replace(",+,","+")
            x = x.replace(",+,","+")
            python_printline[python_printline.index(x)] = x.replace(",*,","*")
            x = x.replace(",*,","*")
            python_printline[python_printline.index(x)] = x.replace("*,","*")
            x = x.replace("*,","*")
            python_printline[python_printline.index(x)] = x.replace(",/,","/")
            x = x.replace(",/,","/")
            python_printline[python_printline.index(x)] = x.replace(",-,","-")
            x = x.replace(",-,","-")
            python_printline[python_printline.index(x)] = x.replace(",**,","**")
            x = x.replace(",**,","**")
            
            

    # Codegen Stage 3: Python final file
    python_file = []
    python_line = ''
    for i in python_printline:
        if i != ";":
            python_line = python_line + i
        elif i == ";":
            python_file.append(python_line)
            python_line=''

    return python_file
