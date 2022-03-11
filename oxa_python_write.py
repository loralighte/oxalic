def oxa_py3_write(filecontent, filename):
    with open(filename,"w") as oxa_py3_output:
        for i in filecontent:
            oxa_py3_output.write(i + "\n")