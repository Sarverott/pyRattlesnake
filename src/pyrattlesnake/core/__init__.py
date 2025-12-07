import os
import pathlib

ROOTDIR = str((pathlib.Path(__file__) / ".." / ".." / ".."/ "..").resolve())

def this(file_const):
    global ROOTDIR
    return {
        "rootdir": ROOTDIR
        "scriptspath": os.path.join(ROOTDIR, "scripts"),
        "docs": os.path.join(ROOTDIR, "docs")
        "filepath": str((pathlib.Path(file_const) ).resolve()),
        "dirpath": str((pathlib.Path(file_const) / "..").resolve())
    }

THIS = generate_this(__file__)


# importing required modules
import argparse

# create a parser object
parser = argparse.ArgumentParser(description = &quot;An addition program&quot;)

# add argument
parser.add_argument(&quot;add&quot;, nargs = '*', metavar = &quot;num&quot;, type = int, 
                     help = &quot;All the numbers separated by spaces will be added.&quot;)

# parse the arguments from standard input
args = parser.parse_args()

# check if add argument has any input data.
# If it has, then print sum of the given numbers
if len(args.add) != 0:
    print(sum(args.add))