"""
file for argparse
"""
import argparse

parser = argparse.ArgumentParser(description="the example parser for argparse")   # first create a parser

parser.add_argument("-a", type=int, help="the a number for adding")   # type for the input
parser.add_argument("-b", type=int, help="the b number for adding")   # help for the -h or --help argument

parser.add_argument("-s", "--sum", nargs="+", type=int)   # nargs for numbers
parser.add_argument("-r", "--required", required=True)   # you must provide this argument
parser.add_argument("-t", "--true", action="store_true")   # if have this argument, it will store True in the value

args = parser.parse_args()   # get all arguments
print(args)

print(args.a + args.b)

res = 0
for i in args.sum:
    res += i
print(res)
