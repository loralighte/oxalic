import sys
from oxa_splitter import oxa_split
from oxa_python_codegen import oxa_py3_codegen
from oxa_python_write import oxa_py3_write

oxafile = sys.argv[1]
file = ""
with open(oxafile, "r") as oxa:
    for line in oxa:
        if line.endswith("\n"):
            line = line[:-1]
        file = file + line
    oxa_py3_write(oxa_py3_codegen(oxa_split(file)), oxafile + ".py")