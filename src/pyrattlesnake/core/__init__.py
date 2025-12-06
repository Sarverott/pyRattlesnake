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